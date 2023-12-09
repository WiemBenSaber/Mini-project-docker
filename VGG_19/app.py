import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from keras.models import load_model
import librosa
import librosa.display
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})
# Load the VGG19 model
model = load_model('vgg19_model.h5')

# Function to preprocess an audio file and make predictions
def predict_genre(audio_path):
    # Load the audio file
    y, sr = librosa.load(audio_path, sr=None)

    # Create a mel spectrogram
    spec = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=512)
    spec_db = librosa.power_to_db(spec, ref=np.max)

    # Resize the spectrogram to match the expected input shape of VGG19
    spec_db = np.resize(spec_db, (224, 224, 3))

    # Reshape the input for prediction
    input_data = np.expand_dims(spec_db, axis=0)

    # Make predictions
    predictions = model.predict(input_data)

    # Assuming you have a list of genres used during training
    genres = ["pop", "jazz", "metal", "blues", "disco", "classical", "country", "hiphop", "reggae", "rock"]

    # Get the predicted genre
    predicted_genre = genres[np.argmax(predictions)]

    print(f"Predicted Genre: {predicted_genre}")

    return predicted_genre

# Endpoint for making predictions
@app.route('/vgg', methods=['POST','GET'])
def make_prediction():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio_file']

    try:
        predicted_genre = predict_genre(audio_file)
        return jsonify({'predicted_genre': predicted_genre})
    except Exception as e:
        return jsonify({'error': f'Error making prediction: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
