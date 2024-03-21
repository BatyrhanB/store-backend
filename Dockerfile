FROM python:3.9

RUN mkdir -p /opt/services/store-backend

WORKDIR /opt/services/store-backend

ADD . /opt/services/store-backend/

RUN chmod 755 /opt/services/store-backend/scripts/* && \
        chmod +x /opt/services/store-backend/scripts/* && \
            export DJANGO_SETTINGS_MODULE=store.settings && \
                pip install -r requirements.txt 