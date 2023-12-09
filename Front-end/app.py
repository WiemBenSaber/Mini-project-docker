import requests
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Define the URLs for the backend services
svm_backend_url = 'http://192.168.1.20:8081/predict'
vgg19_backend_url = 'http://192.168.1.20:8082/vgg'

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    predicted_genre = None

    if request.method == 'POST':
        # Get the selected prediction type
        prediction_type = request.form.get('prediction_type')

        # Determine the backend URL based on the prediction type
        backend_url = svm_backend_url if prediction_type == 'svm' else vgg19_backend_url

        # Perform a POST request to the backend
        audio_file = request.files['audio_file']
        files = {'audio_file': (audio_file.filename, audio_file.stream, audio_file.content_type)}
        response = requests.post(backend_url, files=files)

        # Get the predicted data from the backend response
        predicted_genre = response.json().get('predicted_genre') if response.ok else 'Error fetching prediction'

    return render_template('index.html', predicted_genre=predicted_genre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
