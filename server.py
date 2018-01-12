from flask import Flask, render_template
from flask_socketio import SocketIO,emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_source(message):
    ##text = json_data['message'].encode('ascii', 'ignore')
    socketio.emit('echo', {'rep':'Server Says...'+message['data']})

@socketio.on('connect')
def test_connect():
    emit('my_response', {'data': 'Connected', 'count': 0})
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0',debug=True)