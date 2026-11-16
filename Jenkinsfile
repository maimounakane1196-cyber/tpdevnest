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

        // Étape 5 : scan de sécurité avec Trivy
        stage('Scan Sécurité') {
            steps {
                // Scan de l'image backend (rapport seulement, le build ne casse pas)
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --severity HIGH,CRITICAL --exit-code 0 tpdevnest-backend'
                // Scan de l'image frontend
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --severity HIGH,CRITICAL --exit-code 0 tpdevnest-frontend'
            }
        }
    }
}