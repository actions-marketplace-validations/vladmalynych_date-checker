FROM python:3.8-alpine

COPY src/ /app/

ENTRYPOINT ["/app/main.py"]
