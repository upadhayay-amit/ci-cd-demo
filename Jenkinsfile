pipeline {
  
  agent any 
  
  stages {
    
    stage("build") {
      steps {
        echo "Inside the build step"
        echo env.BRANCH_NAME
      }
    }  
    
    stage("test") {
      steps {
        echo "Inside the test step"
      }
    }  
    
    stage("deploy") {
      steps {
        echo "Inside the deploy step"
      }
    }  
  }
  
}
  
