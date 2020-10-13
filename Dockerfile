FROM python:3.8.6-alpine3.12

# copy everything from current dir to /var...
COPY . /var/www/html

# cd + auto def wdir
WORKDIR /var/www/html

# install dependencies
RUN pip3 install -r ./requirements.txt

# Set Flask variables
ENV FLASK_DEBUG=1
ENV FLASK_APP=start.py

# run app
CMD flask run --host=0.0.0.0

# Info about port
EXPOSE 5000
