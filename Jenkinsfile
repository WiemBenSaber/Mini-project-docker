pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                script {
                   env.PATH = "/usr/local/bin:${env.PATH}"
                    // Installer les dépendances nécessaires
                    //sh 'pip install requests'

                    // Construire et lancer les conteneurs Docker
                   // sh 'pip3 install docker-compose'
                    sh '/usr/local/bin/docker-compose build'
                    sh '/usr/local/bin/docker-compose up'
                    sh '/usr/local/bin/docker-compose ps'


                }
            }
        }
         stage('Wait for Backend Services') {
            steps {
                script {
                    sh '/Users/wiem/Desktop/wait-for-it.sh -t 0 http://127.0.0.1:8081/predict -- echo "Backend services are ready!"'
                }
            }
        }
         stage('Run tests against the container') {
      steps {
        // Attendre un peu pour permettre aux conteneurs de démarrer


                  // Create and activate a virtual environment
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'

                    // Install required dependencies
                    sh 'pip3 install requests werkzeug'

                    // Exécuter les tests
                    sh 'python3 -m unittest tests/prediction_tests.py'
           }
       }

        // Ajoutez d'autres étapes de pipeline selon vos besoins
    }

}
