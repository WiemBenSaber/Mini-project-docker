pipeline {
    agent any

    stages {
        stage('Build and Deploy Containers') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml up -d --build'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml exec frontend python tests/prediction_tests.py'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml down'
                }
            }
        }
    }
}
