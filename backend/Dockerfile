# Base Image
FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
