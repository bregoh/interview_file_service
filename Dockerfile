# official base image
FROM python:3.9-slim-buster


# environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential netcat \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# work directory
WORKDIR /usr/src/app

# copy dependencies file
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD [ "python", "manage.py", "runserver" ]