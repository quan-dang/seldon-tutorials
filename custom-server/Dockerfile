FROM python:3.7

RUN mkdir -p /mnt/model/
RUN chmod -R a+rw /mnt/model/

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Port for REST
EXPOSE 9000

# Define environment variable
ENV MODEL_NAME online_score_api
ENV SERVICE_TYPE MODEL

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
