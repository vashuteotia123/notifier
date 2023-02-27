# Notifier.

## Auth Service Endpoints - serve at port 3000.

### `POST /auth/signup`

Creates a new user account.

Request body:
- `username` (string, required)
- `email` (string, required)
- `password` (string, required)

Response:
- `201 Created` if successful, with:
  - `msg` (string)
  - `data` (object) containing:
    - `username` (string)
    - `email` (string)
    - `id` (number)
- `422 Unprocessable Entity` if unsuccessful, with:
  - `err` (array) containing error messages
  

### `POST /auth/login`

Logs in an existing user.

Request body:
- `username` (string, required)
- `password` (string, required)

Response:
- `200 Ok` if successful, with:
  - `msg` (string)
  - `data` (object) containing:
    - `token` (string) representing the JWT token
    - `exp` (string) representing the token expiration time
    - `user` (object) containing:
      - `username` (string)
      - `email` (string)
      - `id` (number)
- `401 Unauthorized` if the username and password don't match, with:
  - `err` (string) describing the error

## Notify Service - serve at port 8000.

### `GET localhost:8000/get_user_notifications`

This endpoint retrieves notifications for the authenticated user.

Request Headers

- `Authorization` (string, required): Bearer token <JWT_TOKEN> for authentication.

Response

- `200 OK` if successful, with:
  - `notifications` (list) containing notification objects with the following fields:
    - `id` (number) representing the notification ID
    - `uid` (string) representing the user ID
    - `token_id` (string) representing the token ID
    - `blockchain_deposit_status` (string) representing the status of the blockchain deposit
    - `brine_deposit_status` (string) representing the status of the brine deposit
    - `deposit_blockchain_hash` (string) representing the hash of the blockchain deposit
    - `amount` (string) representing the amount of the deposit
    - `created_at` (string) representing the timestamp of the notification creation
    - `type` (string) representing the type of the deposit
- `403 Forbidden` if the token is invalid, with:
  - `detail` (string) describing the error. 


### Publish notification.

Publishes a notification to the RabbitMQ message broker.

Notification message:

A JSON object containing the notification data with the following fields:
- `type` (string, required): the type of the notification
- `uid` (string, required): the user ID associated with the notification
- `token_id` (string, required): the ID of the token associated with the notification
- `blockchain_deposit_status` (string, required): the status of the blockchain deposit
- `brine_deposit_status` (string, required): the status of the Brine deposit
- `deposit_blockchain_hash` (string, required): the hash of the blockchain deposit
- `amount` (string, required): the amount of the deposit
- `created_at` (string, required): the creation timestamp of the notification in the format "YYYY-MM-DDTHH:MM:SSZ"

### Development

Uses the default Django development server.

1. Update the environment variables in the *docker-compose.yml*, *.env.dev* and *env.dev.db* files. (checkout *.env.dev.sample* for reference.)
2. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```
