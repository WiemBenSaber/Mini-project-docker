import unittest
import requests

class TestPredictions(unittest.TestCase):


    def test_backend_prediction(self):
        response = requests.post("http://localhost:8081/predict", json={"data": "sample_data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["predicted_genre"], "expected_prediction_backend")

    def test_vgg19_backend_prediction(self):
        response = requests.post("http://localhost:8082/vgg", json={"data": "sample_data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["predicted_genre"], "expected_prediction_vgg19")

if __name__ == '__main__':
    unittest.main()
