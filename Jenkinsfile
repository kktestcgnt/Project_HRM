pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/kktestcgnt/Project_HRM.git'
            }
        }

        stage('Run Python File') {
            steps {
                sh '''
                echo "Checking Python version"
                python3 --version

                echo "Running one.py"
                python3 one.py
                '''
            }
        }
    }
}
