pipeline {
    // Jenkins choisit lui-même où exécuter le pipeline
    agent any

    stages {
        // Étape 1 : récupérer le code depuis GitHub
        stage('Checkout') {
            steps {
                // Télécharge le dépôt configuré dans le job
                checkout scm
                echo 'Code récupéré avec succès'
            }
        }

                // Étape de diagnostic : quels outils Jenkins connaît-il ?
        stage('Vérif outils') {
            steps {
                bat 'python --version'
                bat 'node -v'
                bat 'npm -v'
                bat 'docker --version'
            }
        }
    }
}