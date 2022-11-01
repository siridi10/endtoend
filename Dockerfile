FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 5050
# CMD [ "gunicorn" , "-w=4" , "-b" , "0.0.0.0:5050" , "app:app" ]
<<<<<<< HEAD

=======
>>>>>>> 357f845ee692c3aba920e828ba250d6f890ad7bf
EXPOSE $PORT
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app
