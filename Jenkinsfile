pipeline {
    // Jenkins choisit lui-même où exécuter le pipeline
    agent any

    environment {
        // À REMPLACER par ton nom d'utilisateur Docker Hub
        DOCKERHUB_USER = 'TON-USER-DOCKERHUB'
    }

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
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --severity HIGH,CRITICAL --exit-code 0 tpdevnest-backend'
                sh 'docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --severity HIGH,CRITICAL --exit-code 0 tpdevnest-frontend'
            }
        }

        // Étape 6 : donner aux images leur nom complet pour Docker Hub
        stage('Build des images') {
            steps {
                sh "docker tag tpdevnest-backend ${'maimounakane'}/backend:latest"
                sh "docker tag tpdevnest-frontend ${'maimounakane'}/frontend:latest"
            }
        }

                // Étape 7 : envoi des images vers Docker Hub
        stage('Push Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
                    // retry(3) : en cas d'échec, Jenkins réessaie jusqu'à 3 fois
                    retry(3) {
                        sh "docker push ${'maimounakane'}/backend:latest"
                    }
                    retry(3) {
                        sh "docker push ${'maimounakane'}/frontend:latest"
                    }
                }
            }
        }
    }
}