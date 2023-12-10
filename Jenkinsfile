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
         stage('Run tests against the container') {
      steps {
        // Attendre un peu pour permettre aux conteneurs de démarrer
                   sleep 20
                    echo 'tested..'
                    // Exécuter les tests
                    sh 'python -m unittest tests/prediction_tests.py'
           }
       }

        // Ajoutez d'autres étapes de pipeline selon vos besoins
    }

}
