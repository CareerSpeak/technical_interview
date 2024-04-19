FROM python:3.9-alpine

RUN mkdir -p /home/python/tech_interview

WORKDIR /home/python/tech_interview

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD [ "service.py" ]
