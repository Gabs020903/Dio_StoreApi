# Store API

## Description 📖
This REST API was created as a project for the course "Vivo - Python AI Backend Developer", hosted by the platform DIO and It has the capability to do simple HTTP requests (GET, POST, PATCH, DELETE). It was, as statted, created for educational purposes, and new implementations may be realized in a near future. But, for the moment, no new implementations are scheduled.

## Technologies utilized 🛠
* Python 3.12
* Docker
* Uvicorn
* Fastapi
* MongoDB

## Installation and compiling 🚀
1. To start, clone the repo with the command `git clone https://github.com/danielkmatuo/dio_store_api.git`

2. In the terminal, use the command `pip install -r requirements`

3. Download [MongoDB](https://www.mongodb.com/) and [create a new cluster](https://www.mongodb.com/pt-br/docs/atlas/getting-started/)

4. Create a `.env` file in the API directory and create a new environment variable, following the example `DATABASE_URL=mongodb+srv://<your_username>:<your_password>@<cluster_name>/<database_name>`

5. Then, download [Docker](https://www.docker.com/) and run the command `docker-compose up --build` in the terminal

6. Now, your application should run smoothly!

* **NOTE**: if you are using Windows, you need to first install WSL2 to make the application work with Docker. If you do not want to use Docker, you just need to follow the first 4 steps and, then, type in your terminal the following command: `uvicorn main:app --host 0.0.0.0 --port 8000`

## Connections 📱
* email: danielkmatuo@gmail.com
* github: danielkmatuo
