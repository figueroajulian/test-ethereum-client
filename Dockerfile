FROM python:3.9
LABEL maintainers = 'QA'

WORKDIR /app
ENV PYTHONPATH=/app \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# Install requirements.txt
COPY ./requirements.txt .
RUN pip -q install -r requirements.txt