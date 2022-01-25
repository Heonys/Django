FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/siwmua0/Django.git

WORKDIR /home/Django/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=project.settings.deploy && gunicorn project.wsgi --env DJANGO_SETTINGS_MODULE=project.settings.deploy --bind 0.0.0.0:8000"]

