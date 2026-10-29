
pipeline {
    agent any

    environment {
        MLFLOW_TRACKING_URI = 'sqlite:///C:/Users/Akshay.MS/.jenkins/workspace/Car-Severity-MLOps/mlflow.db'
    }

    stages {
        stage('Checkout from Git') {
            steps {
                bat 'if exist source rmdir /s /q source'
                bat 'git clone --branch main https://github.com/Yeagerist11/mlops-car-severity.git source'
            }
        }

        stage('Create Python Environment') {
            steps {
                dir('source') {
                    bat 'py -3.14 -m venv .venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('source') {
                    bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                    bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Train Model with MLflow') {
            steps {
                dir('source') {
                    bat '.venv\\Scripts\\python.exe train.py'
                }
            }
        }

        stage('Run Model Tests') {
            steps {
                dir('source') {
                    bat '.venv\\Scripts\\python.exe -m pytest -v'
                }
            }
        }
    }

    post {
        success {
            echo 'MLOps pipeline completed successfully. Model training and tests passed.'
        }

        failure {
            echo 'MLOps pipeline failed. Check the console output for details.'
        }
    }
}
