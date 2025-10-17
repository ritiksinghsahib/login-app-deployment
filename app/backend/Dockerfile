
FROM python:3.9-slim
WORKDIR /app
COPY app.py init_db.py /app/
RUN pip install flask && python init_db.py
CMD ["python", "app.py"]
