FROM python:3.8-alpine
USER root
EXPOSE 8080
COPY * /
RUN pip3 install -r requirements.txt
ENV FLASK_APP=ip.py
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=8080"]
