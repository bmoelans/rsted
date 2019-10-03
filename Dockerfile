FROM python:3-alpine

RUN apk --no-cache add build-base python-dev py-pip jpeg-dev zlib-dev git

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r pip-requirements.txt

RUN adduser -D myuser
USER myuser

ENTRYPOINT ["python"]
CMD ["application.py"]
