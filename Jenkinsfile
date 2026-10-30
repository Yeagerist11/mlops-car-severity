
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

        stage('Build Docker Image') {
            steps {
                dir('source') {
                    bat 'docker --version'
                    bat 'docker build -t car-severity-api:%BUILD_NUMBER% -t car-severity-api:latest .'
                }
            }
        }
        stage('Deploy Docker Container') {
            steps {
                dir('source') {
                    bat '''
                        powershell -NoProfile -ExecutionPolicy Bypass -Command "$container = docker ps -aq --filter 'name=^/car-severity-container$'; if ($container) { docker rm -f car-severity-container; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }; docker run -d --restart unless-stopped --name car-severity-container -p 8000:8000 car-severity-api:latest; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }"
                    '''
        }
    }
}
        stage('Archive Trained Model') {
            steps {
                archiveArtifacts artifacts: 'source/models/car_severity_model.joblib',
                                fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'MLOps pipeline completed successfully. Model training, tests, Docker build, and artifact archiving passed.'
        }

        failure {
            echo 'MLOps pipeline failed. Check the console output for details.'
        }
    }
}
