FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /hope_project
COPY requirements.txt /hope_project/
RUN pip install -r requirements.txt
COPY . /hope_project/
EXPOSE 8000
# CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
CMD exec gunicorn hope_project.wsgi:application --bind 0.0.0.0:8000 --workers 3


