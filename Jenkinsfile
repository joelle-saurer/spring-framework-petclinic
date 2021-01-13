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


    }
}
