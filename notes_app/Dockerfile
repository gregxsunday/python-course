FROM python:3.8.1-slim-buster
RUN adduser --group hacker && adduser --ingroup hacker hacker
WORKDIR /
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_env=production
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /notes
WORKDIR /notes
RUN chown -R hacker:hacker .
USER hacker
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--access-logfile", "-", "wsgi:app"]