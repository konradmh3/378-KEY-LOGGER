# 378-KEY-LOGGER
378 semester project

## Domain
 - http://ssh.378lab.cool:11023/
 
## Project
In order to replicate our keylogger there are three main components
    - The keylogger
    - The server
    - The client

- The keylogger
    - The Keylogger is the program that will be running on the victim's computer. It will be responsible for logging the keystrokes and sending them to the server via Python's requests library.
    - The keylogger was written in Python. It is a simple script that uses the pynput library to listen for key presses and releases. When a key is pressed or released, it adds the key to a log variable. This repeats untill every 5 seconds, the log is sent to the server via a POST request. The log is then cleared and the process repeats.
    - In the process_key_press(key) function of the keylogger, the key pressed by the victim is checked to see if it is a special key that needs adjustments. For example the pynput library will record the backspace key as key.backspace, however we want it to actually delete the last key pressed, like what the user sees. 

- The server
    - The server is the program that will be running on the attacker's computer. It will be responsible for receiving the keystrokes from the keylogger and storing them in a database. The server uses the Flask framework to create a web server that will receive the keystrokes from the keylogger. We have 2 endpoints, @app.route('/postLog', methods=['POST']), and @app.route('/clearLog', methods=['POST']). The first endpoint, called by the malware/keylogger, is responsible for receiving the keystrokes from the keylogger and storing them in our log.txt file. The second endpoint is responsible for clearing the log.txt file and will be called from the html page on press of a button.
    <!-- add pic of html page -->

- The html page/js functions
    - The html page is the page that will be use to display the keystrokes saved in the log.txt file to the attacker for demonstration purposes, however saving the key strokes to the file on the server and viewing that same file later via terminal would suffice. The html page uses javascript functions to make a request to the server to clear the log.txt file on press of the "clear log" button. The html page also uses javascript functions to make a request to the server to get the contents of the log.txt file and display it on the page.

- Both the keylogger and html page operate apart from each other and are both use the server in there own unique way. The keylogger will send the keystrokes to the server and the html page will make a request to the server to get the contents of the log.txt file and display it on the page.