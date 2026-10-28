
pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat 'D:\\mlops-car-severity\\.venv\\Scripts\\python.exe --version'
            }
        }

        stage('Run Model Tests') {
            steps {
                dir('D:\\mlops-car-severity') {
                    bat 'D:\\mlops-car-severity\\.venv\\Scripts\\python.exe -m pytest -v'
                }
            }
        }
    }
}
