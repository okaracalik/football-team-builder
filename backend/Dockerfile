FROM python:3.7

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8051

CMD ["python","-u", "app.py"]