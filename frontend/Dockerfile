FROM python:3.8-slim

WORKDIR /app

COPY backend/templates /app/backend/app.py/
COPY frontend/templates /app/frontend/templates/
COPY frontend/templates /app/frontend/app.py/

RUN pip install Flask Flask-RESTful

EXPOSE 5000

CMD ["python", "app.py"]
