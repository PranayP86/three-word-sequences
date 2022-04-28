FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install -r requirements_web.txt

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py"]