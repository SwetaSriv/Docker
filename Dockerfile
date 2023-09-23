#sample docker file for deploying app on the web
FROM openjdk:8
LABEL maintainer ="Sweta"
ADD target/demo-0.0.1-SNAPSHOT.jar sampleapp.jar
ENTRYPOINT ["java", "-jar", "sampleapp.jar"]