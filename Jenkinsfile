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
    }
}