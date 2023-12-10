pipeline {
    agent any

    stages {
        stage('Build and Launch Containers') {
            steps {
                script {
                    // Ensure the script uses the correct PATH
                    env.PATH = "/usr/local/bin:${env.PATH}"

                    // Build and launch Docker containers using docker-compose
                    sh '/usr/local/bin/docker-compose up -d --build'
                    sh '/usr/local/bin/docker-compose logs'
                    sh '/usr/local/bin/docker-compose ps'
                }
            }
        }

        stage('Wait for Backend Services') {
            steps {
                script {
                    // Use the correct path to the wait-for-it script
                    sh '/Users/wiem/Desktop/wait-for-it.sh -t 60 http://127.0.0.1:8081/predict -- echo "Backend services are ready!"'
                    sh '/Users/wiem/Desktop/wait-for-it.sh -t 120 http://127.0.0.1:8082/vgg -- echo "Backend services are ready!" '
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Wait for a few seconds to allow containers to fully start
                    sleep 10

                    // Create and activate a virtual environment
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'

                    // Install required dependencies
                    sh 'pip3 install requests werkzeug'

                    // Run the tests
                    sh 'curl http://127.0.0.1:8081/predict'
                    sh 'curl http://127.0.0.1:8082/vgg'
                    sh 'python3 -m unittest tests/prediction_tests.py'
                }
            }
        }
    }
}
