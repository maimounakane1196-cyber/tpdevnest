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
                sh 'python3 --version || echo "python ABSENT"'
                sh 'node -v || echo "node ABSENT"'
                sh 'npm -v || echo "npm ABSENT"'
                sh 'docker --version || echo "docker ABSENT"'
            }
        }
    }
}