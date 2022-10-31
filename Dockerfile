FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 5050
# CMD [ "gunicorn" , "-w=4" , "-b" , "0.0.0.0:5050" , "app:app" ]

EXPOSE $PORT
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app
