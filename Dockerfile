FROM python:3.8
COPY . .
RUN pip install -r requirements.txt
WORKDIR .
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]