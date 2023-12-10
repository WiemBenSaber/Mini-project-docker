import os
import unittest
import requests
from werkzeug.datastructures import FileStorage

class TestPredictionEndpoints(unittest.TestCase):
    def setUp(self):
        # Les URL des services backend pour les tests
        self.svm_backend_url = 'http://127.0.0.1:8081/predict'
        self.vgg19_backend_url = 'http://127.0.0.1:8082/vgg'

        # Charger un fichier audio de test pour les deux modèles
        self.audio_file_path = os.path.join(os.path.dirname(__file__), '../Front-end/audio_to_predict.wav')
        self.audio_file = FileStorage(stream=open(self.audio_file_path, "rb"), filename="audio_to_predict.wav")

    def test_svm_prediction_endpoint(self):
        # Créer un dictionnaire avec le fichier audio
        files = {'audio_file': self.audio_file}

        # Effectuer une requête POST vers l'endpoint SVM
        response = requests.post(self.svm_backend_url, files=files)

        # Appeler une méthode générique pour tester la réponse
        self._test_prediction_endpoint(response)

    def test_vgg19_prediction_endpoint(self):
        # Créer un dictionnaire avec le fichier audio
        files = {'audio_file': self.audio_file}

        # Effectuer une requête POST vers l'endpoint VGG19
        response = requests.post(self.vgg19_backend_url, files=files)

        # Appeler une méthode générique pour tester la réponse
        self._test_prediction_endpoint(response)

    def _test_prediction_endpoint(self, response):
        # Vérifier si la réponse est réussie (code d'état HTTP 200)
        self.assertEqual(response.status_code, 200)

        # Vérifier si la réponse contient le genre prédit
        data = response.json()
        self.assertIn('predicted_genre', data)

        # Ajouter d'autres assertions spécifiques en fonction du comportement de votre application

if __name__ == '__main__':
    unittest.main()
