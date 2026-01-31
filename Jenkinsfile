pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                python --version
                python sample.py
                '''
            }
        }
    }
}
