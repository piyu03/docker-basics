Steps to create docker file
1. We decide on the base image on which we want to run our application, here we use python image, so that will have a python environment pre-installed and dont have to worry about installing python.

FROM python:3.8-slim-buster 

2. We create a directory in a container where we can keep our code,data other relevant files.

WORKDIR /docker_working_dir

3. We now copy our files present in the host(local) directory to the image ‘docker_working_dir’ directory using the COPY command

COPY . /docker_working_dir

4. To install our app dependencies, we use

RUN pip3 install -r requirements.txt

5. We can expose our application to the port using the EXPOSE command

Expose 5000

6. To specify which command to run when our image is executed inside the container we use the CMD commend.

CMD ["python3","/docker_working_dir/app.py"]

--------------------------------------------------------
--------------------------------------------------------

- To build docker image

cd credit_score(where dockerfile is located)
docker build -t app:v1(name your docker image) . 

- To run dockerfile
docker run -p 80:80 app:v1

- To publish your dockerfile public
docker push 03piyu(username of your dockerhub)/app:v1
