# Getting started with Producer Consumer API

## Running

1) ### `docker-compose up -d --build`
2) ### `docker-compose run web python producer_consumer/manage.py migrate`
3) ### `docker-compose run web python producer_consumer/manage.py createsuperuser`
4) ### `docker-compose up`

## Available Paths

### `http://localhost:8000/admin` - admin panel for searching DB`s and adding new user to User table

### `http://localhost:8000/api/orders` - list of orders with the ability to delete, add, modify

### `http://localhost:3000` - web page of producer-consumer
