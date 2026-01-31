pipeline {
    agent any

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
