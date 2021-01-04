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
              sh 'mvn deploy -Dmaven.install.skip=true'
            }
        }

       
        stage('Selenium test') {
            steps {
              echo 'Testing the application'
              sh "python3 '/var/lib/jenkins/workspace/Petclinic Pipeline/src/test/java/org/springframework/samples/petclinic/test_petclinic.py'"
            }
        }

    }
}
