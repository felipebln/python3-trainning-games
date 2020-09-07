FROM python:3
ADD . /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
CMD ["python", "jogos.py"]