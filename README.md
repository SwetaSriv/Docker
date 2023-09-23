# Docker

Application details: Springboot with Thymleaf, H2 (in memory database)
GetRequest: /say-hello



Dockerfile details-

#the sample web app runs on java 1.8 version

FROM openjdk:1.8

# Adding a suitable label 
LABEL maintainer ="Sweta"

# Add the jar from the target directory(its a java maven project, jar is in target directory)
ADD target/demo-0.0.1-SNAPSHOT.jar sampleapp.jar

#For Docker to run the application, first value is a command and the last two are parameters.
ENTRYPOINT ["java", "-jar", "springboot-docker-demo.jar"]

Now run the below commands in the terminal to build the image

docker build -t sample-web-app-springboot:latest .

Now we can run the container based on the above image using the command below

docker run -p 8082:8080 sample-web-app-springboot

The application can be reached from the url: localhost:8082/say-hello


@Author - Sweta Srivastava - M22AIE204
