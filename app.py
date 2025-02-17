from flask import Flask, request, jsonify
from flask import Flask, send_from_directory
from flask import Flask, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("models/random_forest.pkl")

'''@app.route('/predict', methods=['POST'])

@app.route('/')
def predict():
    # Your prediction logic here
    return 'Prediction made'

@app.route('/predict', methods=['POST'])
def predict():
    return "First function"

@app.route('/predict_alternate', methods=['GET'])  #  Unique function name
def predict_alternate():
    return "Second function"


@app.route('/predict_v2', methods=['GET', 'POST'])  # change route name
def predict_v2():
    return "Prediction 2"

def predict_v2():
    if request.method == 'POST':
        # Handle POST request
        return 'Prediction Endpoint'
@app.route('/predict', methods=['POST'], endpoint="predict_post")
def predict():
    return "This is the predict function"'''

@app.route('/')
def home():
    return "Desease Prediction Tool!"

if __name__ == '__main__':
    app.run(debug=True)
#from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "Desease prediction"
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)

def predict_v2():
    data = request.json['input']
    prediction = model.predict(np.array(data).reshape(1, -1))
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"
    
    file = request.files["file"]
    if file.filename == "":
        return "No selected file"
    
    # Save file
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return f"File '{file.filename}' uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)



 
