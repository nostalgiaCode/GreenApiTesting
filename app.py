
from flask import Flask, jsonify, render_template, request
from views import getSettings, getStateInstance, sendTextMessage, sendFileByURL

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + lastname
        if firstname and lastname:
            return jsonify({'output':'Your Name is ' + output + ', right?'})
        return jsonify({'error' : 'Missing data!'})
    return render_template('index.html')

@app.route('/get_settings', methods=['GET', 'POST'])
def get_settings():
    if request.method == 'POST':
        idInstance = request.form.get('idInstance')
        apiTokenInstance = request.form.get('apiTokenInstance')
        print(f"id {idInstance}, api {apiTokenInstance}")
        data = getSettings(" https://1103.api.green-api.com", idInstance, apiTokenInstance)

        return(data, 201)

@app.route('/get_state_instance', methods=['GET', 'POST'])
def get_state_instance():
    if request.method == 'POST':
        idInstance = request.form.get('idInstance')
        apiTokenInstance = request.form.get('apiTokenInstance')
        print(f"id {idInstance}, api {apiTokenInstance}")
        data = getStateInstance(" https://1103.api.green-api.com", idInstance, apiTokenInstance)

        return(data, 201)
    
@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        idInstance = request.form.get('idInstance')
        apiTokenInstance = request.form.get('apiTokenInstance')
        phoneNumber1 = request.form.get('phoneNumber1')
        messageText = request.form.get('messageText')
        data = sendTextMessage(" https://1103.api.green-api.com", idInstance, apiTokenInstance, phoneNumber1, messageText)

        return(data, 201)

@app.route('/send_media', methods=['GET', 'POST'])
def send_media():
    if request.method == 'POST':
        idInstance = request.form.get('idInstance')
        apiTokenInstance = request.form.get('apiTokenInstance')
        phoneNumber2 = request.form.get('phoneNumber2')
        messageMedia = request.form.get('messageMedia')
        data = sendFileByURL("https://1103.api.green-api.com", idInstance, apiTokenInstance, phoneNumber2, messageMedia)

        return(data, 201)

if __name__ == '__main__':
    app.run(debug=True)