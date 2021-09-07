FROM python:3.9

RUN apt-get update && apt-get upgrade -y

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5004

CMD ["python", "run.py"] 
