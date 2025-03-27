from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict_disease(file_path):
    # Placeholder function to simulate disease prediction
    return "No disease detected"  # Replace this with actual logic

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'ecgReport' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['ecgReport']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = predict_disease(file_path)

    return jsonify({'message': result}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
