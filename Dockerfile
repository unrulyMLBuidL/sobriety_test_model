FROM python:3.12.0-slim

ENV PYTHONBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

WORKDIR /Project-1

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system && \ rm -rf /root/.cache

COPY ["*.py", "drunk_or_not.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:sobriety_test" ]