pipeline {
    
    agent any
 
    tools {
        maven "Maven"
    }

    stages {   
        stage('deploy') {
            steps {
              echo 'Deploying the to Nexus Repo'
              echo 'Application is running on tomcat server'
              sh 'mvn deploy'
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
