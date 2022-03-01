# File Sharing Service

## Functional Requirements

- A form that adds links or files for protection
- Generating links protected with a password
- Expiry of links after a specified time
- A form that allows you to go to a secured link or download a protected file
- Counting correct redirects
- User Agent saving
- REST API
- The secured endpoint for adding elements
- The secured endpoint for downloading statistics (see example)
- An open endpoint to access secure items (if the password was correct)
- Admin panel

## How to run locally

- Clone the repository

- `python3 -m venv <environment-name>`

### windows

- > `<environment-name>/Scripts/activate`

### mac and linux

- > `source <environment-name>/bin/activate`

- `pip install -r requirements.txt`
- `python3 manage.py migrate`
- `python3 manage.py createsuperuser` - fill the prompt input
- `python3 manage.py runserver`

## How to run with docker

- Run `docker compose up`

## How to Run Tests

### locally

- `python3 manage.py test`

### with docker compose

- `docker compose -f docker-compose-test.yml up`

## How to run via web

- open this url: https://bregoh-filemanager.herokuapp.com/web/
