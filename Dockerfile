FROM python:3.8-slim-buster 
WORKDIR /docker_working_dir 
COPY /templates /docker_working_dir/templates
COPY /data/rf.pkl /docker_working_dir/rf.pkl
COPY /requirements.txt /docker_working_dir/requirements.txt
RUN pip3 install -r requirements.txt
COPY /code/app.py /docker_working_dir/app.py
EXPOSE 80
CMD ["python3","/docker_working_dir/app.py"]
