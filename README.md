
# 🚀 FastAPI Mongo Starter

A minimal FastAPI application powered by **MongoDB**, containerized with **Docker**, secured with **JWT authentication**, and orchestrated using **Docker Compose**.

---

## 🌐 Core Functionality

- ⚡ **User Signup & Login**: Register and authenticate users with email and password.
- 🔐 **JWT Authentication**: Secure protected routes using access tokens.
- 🔍 **Get Current User**: Retrieve user details using a valid JWT token.
- 🧩 **Async I/O**: Fully asynchronous using `motor` (MongoDB async driver).
- 📦 **Containerized**: FastAPI and MongoDB run in isolated containers.
- 🔧 **Service Orchestration**: Docker Compose handles setup and networking automatically.
- 🔐 **Environment Configuration**: Secrets and config loaded securely using `.env` and `python-dotenv`.

---


## 🐳 Run the App

```bash
docker-compose up --build
```

---

## ✅ Tech Stack

* FastAPI
* MongoDB
* Motor (async MongoDB driver)
* Python-Jose (JWT)
* Passlib (bcrypt)
* Python-Dotenv
* Docker + Docker Compose

---
