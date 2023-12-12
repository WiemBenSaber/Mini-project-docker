import unittest
import requests
import os

class TestPredictions(unittest.TestCase):

    def test_backend_prediction(self):
        # Chemin vers un fichier audio existant sur votre système
        audio_file_path = 'Front-end/audio_to_predict.wav'

        # Vérifiez que le fichier audio existe
        self.assertTrue(os.path.exists(audio_file_path), f"Le fichier audio {audio_file_path} n'existe pas.")

        # Chargez le fichier audio dans la requête POST
        with open(audio_file_path, 'rb') as audio_file:
            files = {'audio_file': ('Front-end/audio_to_predict.wav', audio_file, 'audio/wav')}
            response = requests.post("http://127.0.0.1:8081/predict", files=files)

        self.assertEqual(response.status_code, 200)
        predicted_genre = response.json().get("predicted_genre")
        self.assertIsNotNone(predicted_genre, "La clé 'predicted_genre' n'est pas présente dans la réponse JSON.")
        self.assertEqual(predicted_genre, "expected_prediction_backend")

    def test_vgg19_backend_prediction(self):
        # Chemin vers un fichier audio existant sur votre système
        audio_file_path = 'Front-end/audio_to_predict.wav'

        # Vérifiez que le fichier audio existe
        self.assertTrue(os.path.exists(audio_file_path), f"Le fichier audio {audio_file_path} n'existe pas.")

        # Chargez le fichier audio dans la requête POST
        with open(audio_file_path, 'rb') as audio_file:
            files = {'audio_file': ('Front-end/audio_to_predict.wav', audio_file, 'audio/wav')}
            response = requests.post("http://127.0.0.1:8082/vgg", files=files)

        self.assertEqual(response.status_code, 200)
        predicted_genre = response.json().get("predicted_genre")
        self.assertIsNotNone(predicted_genre, "La clé 'predicted_genre' n'est pas présente dans la réponse JSON.")
        self.assertEqual(predicted_genre, "expected_prediction_vgg19")

if __name__ == '__main__':
    unittest.main()
