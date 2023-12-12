import unittest
import requests

class TestPredictions(unittest.TestCase):
    # Assuming you have a list of genres used during training
    genres = ["pop", "jazz", "metal", "blues", "disco", "classical", "country", "hiphop", "reggae", "rock"]

    def test_backend_prediction(self):
        response = requests.post("http://localhost:8081/predict", json={"data": "sample_data"})
        self.assertEqual(response.status_code, 200)

        # Ensure the predicted genre is in the list of genres
        predicted_genre = response.json().get("predicted_genre")
        self.assertIn(predicted_genre, self.genres)

    def test_vgg19_backend_prediction(self):
        response = requests.post("http://localhost:8082/vgg", json={"data": "sample_data"})
        self.assertEqual(response.status_code, 200)

        # Ensure the predicted genre is in the list of genres
        predicted_genre = response.json().get("predicted_genre")
        self.assertIn(predicted_genre, self.genres)

if __name__ == '__main__':
    unittest.main()
