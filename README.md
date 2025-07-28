
# 🚀 FastAPI Mongo Starter

A minimal FastAPI application powered by **MongoDB**, containerized with **Docker**, and orchestrated using **Docker Compose**.

---

## 🌐 Core Functionality

- ⚡ **Create User**: Add a new user to the MongoDB collection using a simple JSON payload.
- 🔍 **Retrieve User**: Fetch user details by email from the database.
- 🧩 **Async I/O**: Fully asynchronous using `motor` (MongoDB async driver).
- 📦 **Containerized**: FastAPI and MongoDB run in isolated containers.
- 🔧 **Service Orchestration**: Docker Compose handles setup and networking automatically.

---

## 📄 API Docs

Once running, visit: [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---

## 🐳 Run the App

```bash
docker-compose up --build
````

---


