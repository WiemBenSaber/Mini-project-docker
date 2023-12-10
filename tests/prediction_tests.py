import requests

def test_prediction_results(model_url, audio_file_path):
    # Make a request to the prediction endpoint
    response = requests.post(f'{model_url}/predict', files={'audio_file': open(audio_file_path, 'rb')})

    # Print the response
    print(response.text)

    # Check if the response is successful
    if response.status_code == 200:
        # Extract and print the predicted genre
        data = response.json()
        predicted_genre = data.get('predicted_genre')
        print(f'Predicted Genre: {predicted_genre}')
    else:
        print(f'Prediction failed. Status Code: {response.status_code}')

if __name__ == '__main__':
    # Example usage
    model_url = 'http://127.0.0.1:8081/predict'  # Replace with the actual URL
    audio_file_path = 'Front-end/audio_to_predict.wav'  # Replace with the actual path
    # Call the test function
    test_prediction_results(model_url, audio_file_path).main()
