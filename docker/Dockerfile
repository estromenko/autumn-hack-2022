FROM python:3.10-bullseye

WORKDIR /var/www/app

COPY . /var/www/app

COPY docker/uwsgi.ini /var/www/app

COPY docker/uwsgi_params /etc/nginx

RUN cd /var/www/app && \
    pip3 install -r requirements.txt && \
    echo yes | python3 manage.py collectstatic

COPY docker/docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
