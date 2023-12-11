#12. Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from random import random
from threading import Lock
from datetime import datetime

"""
Background Thread
"""
thread = None
thread_lock = Lock()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'donsky!'
socketio = SocketIO(app, cors_allowed_origins='*')

"""
Get current date time
"""
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

"""
Generate random sequence of dummy sensor values and send it to our clients
"""
def background_thread():
    print("Generating random sensor values")
    while True:
        dummy_sensor_value = round(random() * 100, 3)
        socketio.emit('updateSensorData', {'value': dummy_sensor_value, "date": get_current_datetime()})
        socketio.sleep(1)

"""
Serve root index file
"""
@app.route('/')
def index():
    return render_template('index8.html')

"""
Decorator for connect
"""
@socketio.on('/connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected', request.sid)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    # socketio.run(app)