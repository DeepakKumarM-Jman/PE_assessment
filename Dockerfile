FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "dataprocessor.py" ]

# sudo docker build -t python-app .
# sudo docker run --name container-01 -v /home/deepakkumarm/src:/app/src -v /home/deepakkumarm/dest:/app/dest python-app