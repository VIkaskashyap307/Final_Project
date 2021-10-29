From python:latest
COPY . /terminal
WORKDIR /terminal
CMD ["python","main.py"]
