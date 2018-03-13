from flask import Flask, render_template, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home(name=None):
  return render_template('index.html')

def ini_handler(data):
  print(str(data))

def chat_handler(data):
  print(str(data))
  socketio.emit('mensaje', data)

if __name__ == '__main__':
  socketio.on_event('chat', ini_handler)
  socketio.on_event('send', chat_handler)
  socketio.run(app, host='0.0.0.0')

  url_for('static', filename='chat.png')
  url_for('static', filename='chat.ico')
  url_for('static', filename='style.css')
  url_for('static', filename='chat.js')