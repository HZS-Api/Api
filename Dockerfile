FROM python:3.8.6-alpine3.12

#copy everything from current dir to /var...
COPY . /var/www/html

#cd + auto def wdir
WORKDIR /var/www/html

#install dependencies
RUN pip3 install -r ./requirements.txt

#run app
CMD python ./start.py

#info about port
EXPOSE 5000
