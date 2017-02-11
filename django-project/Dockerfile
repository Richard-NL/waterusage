FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh | sh
RUN source ~/.profile

RUN nvm install 7.4.0
RUN nvm use 7.4.0
RUN npm install http-server -g

WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD bash -c "python3 manage.py runserver 0.0.0.0:8000"
