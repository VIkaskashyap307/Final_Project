From python:latest

ENV PORT 8990
ENV HOST 0.0.0.0

COPY . /gui
WORKDIR /gui
RUN pip install -r requirements.txt
CMD ["python","app.py"]
