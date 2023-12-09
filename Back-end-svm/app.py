import base64
import os
import librosa
import numpy as np
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

# Load the SVM model and scaler
svm_model = joblib.load('modeltest.pkl')
scaler = joblib.load('scalertest.pkl')
expected_features_svm = 57  # Expected number of features

# Function to extract and encode features
def extract_and_encode_features(file_path, num_features=expected_features_svm):
    y, sr = librosa.load(file_path, mono=True)

    # Extract and limit the number of MFCCs to expected_features_svm
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=num_features)

    # Encode the MFCCs in base64
    mfccs_base64 = base64.b64encode(mfccs.tobytes()).decode('utf-8')
    return mfccs_base64

# Function to decode features from base64 string
def decode_features(base64_string):
    bytes_data = base64.b64decode(base64_string)
    features = np.frombuffer(bytes_data, dtype=np.float32)
    return features

# Route to handle prediction
@app.route('/predict', methods=['POST','GET'])
def predict():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio_file']

    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the audio file temporarily
    temp_file_path = 'audio_to_predict.wav'
    audio_file.save(temp_file_path)

    # Extract and encode features from the audio file
    new_audio_features = extract_and_encode_features(temp_file_path)

    # Decode features from the base64 string
    features = decode_features(new_audio_features)

    if features.shape[0] >= expected_features_svm:
        # Reduce features to match the expected number
        features = features[:expected_features_svm]

        # Predict the genre using the SVM model
        predicted_genre = svm_model.predict(features.reshape(1, -1))

        return jsonify({'predicted_genre': predicted_genre[0]})
    else:
        return jsonify({'error': 'Number of features in the audio file does not match the expected number'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
