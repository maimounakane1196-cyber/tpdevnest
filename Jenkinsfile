pipeline {
    // Jenkins choisit lui-même où exécuter le pipeline
    agent any

    // Jenkins vérifie GitHub toutes les 2 minutes environ
    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        // Ton nom d'utilisateur Docker Hub (en minuscules, entre apostrophes)
        DOCKERHUB_USER = 'maimounakane'
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
                sh "docker tag tpdevnest-backend ${DOCKERHUB_USER}/backend:latest"
                sh "docker tag tpdevnest-frontend ${DOCKERHUB_USER}/frontend:latest"
            }
        }

        // Étape 7 : envoi des images vers Docker Hub
        stage('Push Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
                    // Si le push échoue, on attend puis on réessaie
                    sh "docker push ${DOCKERHUB_USER}/backend:latest || (sleep 15 && docker push ${DOCKERHUB_USER}/backend:latest) || (sleep 30 && docker push ${DOCKERHUB_USER}/backend:latest)"
                    sh "docker push ${DOCKERHUB_USER}/frontend:latest || (sleep 15 && docker push ${DOCKERHUB_USER}/frontend:latest) || (sleep 30 && docker push ${DOCKERHUB_USER}/frontend:latest)"
                }
            }
        }

        // Vérifie que Jenkins connaît docker compose
        stage('Test Compose') {
            steps {
                sh 'docker compose version'
            }
        }

        // Étape 8 : déploiement avec Docker Compose
        stage('Déploiement') {
            steps {
                sh 'docker compose -f docker-compose.deploy.yml pull'
                sh 'docker compose -f docker-compose.deploy.yml up -d'
            }
        }
    }
}

//Dans un Jenkinsfile, on range les blocs dans cet ordre :

//agent : où exécuter
//triggers : quand se lancer
//environment : les variables
//stages : quoi faire