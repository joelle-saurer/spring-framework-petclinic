pipeline {
    
    agent any
 
    tools {
        maven "Maven"
    }

    stages {   
        stage('Build') {
            steps {
              echo 'Deploying the Application'
              sh 'mvn package'
            }
        }

       
        stage('Selenium test') {
            steps {
              echo 'Testing the application'
              sh 'python3 /home/azureuser/petclinic/spring-framework-petclinic/test_petclinic.py'
            }
        }

    }
}
