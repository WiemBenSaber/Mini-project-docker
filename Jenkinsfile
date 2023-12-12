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


        stage('Run Tests') {
            steps {
                script {
                    // Wait for a few seconds to allow containers to fully start
                    sleep 10

                    sh 'python3 tests/prediction_tests.py'
                }
            }
        }
    }
}
