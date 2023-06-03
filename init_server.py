from flask import Flask, render_template, request, Response, jsonify,make_response 
import time
from lib import data

app = Flask(__name__, template_folder='templates')

app_data = data.Data()
time.sleep(2.0)

@app.route("/")
def home():
    app_data.read_sensor()
    app_data.update_time()
    templateData = {
        'title' : 'Room Status',
        'time': app_data.get_time_string(),
        'temp': app_data.get_formated_temp(),
        'humi': app_data.get_formated_humi()
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5555, debug=True)
