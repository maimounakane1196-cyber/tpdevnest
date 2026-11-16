pipeline {
    // Jenkins choisit lui-même où exécuter le pipeline
    agent any

    stages {
        // Étape 1 : récupérer le code depuis GitHub
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code récupéré avec succès'
            }
        }

        // Étape 2 : tests du backend
        stage('Tests Backend') {
            steps {
                sh 'docker build -t tpdevnest-backend ./backend'
                sh 'docker run --rm tpdevnest-backend python -m pytest'
            }
        }

        // Étape 3 : tests du frontend
        stage('Tests Frontend') {
            steps {
                sh 'docker build -t tpdevnest-frontend ./frontend'
                sh 'docker run --rm tpdevnest-frontend npm test'
            }
        }
    }
}