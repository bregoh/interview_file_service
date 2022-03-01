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

## How to Use

- Clone the repository
- Run `docker compose up`

## How to Run Tests

- Run `docker compose -f docker-compose-test.yml up`
