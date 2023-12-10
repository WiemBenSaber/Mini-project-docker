import os
import unittest
import requests
from werkzeug.datastructures import FileStorage

class TestPredictionEndpoints(unittest.TestCase):
    def setUp(self):
        # Les URL des services backend pour les tests
        self.svm_backend_url = 'http://127.0.0.1:8081/predict'  # Mise à jour avec la bonne URL
        self.vgg19_backend_url = 'http://127.0.0.1:8082/vgg'  # Mise à jour avec la bonne URL

    def test_svm_prediction_endpoint(self):
        # Charger un fichier audio de test pour SVM
        audio_file_path = os.path.join(os.path.dirname(__file__), '../Front-end/audio_to_predict.wav')
        audio_file = FileStorage(stream=open(audio_file_path, "rb"), filename="audio_to_predict.wav")

        # Créer un dictionnaire avec le fichier audio
        files = {'audio_file': audio_file}

        # Effectuer une requête POST vers l'endpoint SVM
        response = requests.post(self.svm_backend_url, files=files)

        # Vérifier si la réponse est réussie (code d'état HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Vérifier si la réponse contient le genre prédit
        data = response.json()
        self.assertIn('predicted_genre', data)

        # Ajouter d'autres assertions spécifiques en fonction du comportement de votre application
        # Par exemple, vous voudrez peut-être vérifier si le genre prédit est l'un des genres attendus.

    def test_vgg19_prediction_endpoint(self):
        # Charger un fichier audio de test pour VGG19
        audio_file_path = os.path.join(os.path.dirname(__file__), '../Front-end/audio_to_predict.wav')
        audio_file = FileStorage(stream=open(audio_file_path, "rb"), filename="audio_to_predict.wav")

        # Créer un dictionnaire avec le fichier audio
        files = {'audio_file': audio_file}

        # Effectuer une requête POST vers l'endpoint VGG19
        response = requests.post(self.vgg19_backend_url, files=files)

        # Vérifier si la réponse est réussie (code d'état HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Vérifier si la réponse contient le genre prédit
        data = response.json()
        self.assertIn('predicted_genre', data)

        # Ajouter d'autres assertions spécifiques en fonction du comportement de votre application

if __name__ == '__main__':
    unittest.main()
