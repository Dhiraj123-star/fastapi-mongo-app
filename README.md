
# 🚀 FastAPI Mongo Starter

A minimal FastAPI application powered by **MongoDB** and **Valkey (Redis-compatible cache)**, secured with **JWT authentication**, containerized with **Docker**, and orchestrated using **Docker Compose**. It also supports **CI/CD pipelines** via GitHub Actions for seamless Docker image builds and deployments.

---

## 🌐 Core Functionality

* ⚡ **User Signup & Login**: Register and authenticate users with email and password.
* 🔐 **JWT Authentication**: Secure protected routes using access tokens.
* 🔍 **Get Current User**: Retrieve user details using a valid JWT token, with cache fallback using Valkey.
* 🚀 **Valkey Caching**: Improves performance by caching user data in Valkey (a Redis-compatible cache).
* 🧩 **Async I/O**: Fully asynchronous using `motor` (MongoDB async driver) and `redis.asyncio` for cache.
* 📦 **Containerized**: FastAPI, MongoDB, and Valkey run in isolated containers.
* 🔧 **Service Orchestration**: Docker Compose handles setup, networking, and service orchestration automatically.
* 📡 **NGINX Load Balancer**: Routes and balances traffic across 3 FastAPI instances using round-robin strategy.
* 🔒 **Self-Signed SSL (HTTPS)**: NGINX serves traffic over HTTPS using self-signed SSL certificates.
* 🚫 **No `.env` Required for CI/CD**: GitHub Actions sets sensitive variables directly during build—no `.env` file dependency for Docker image creation.

---

## 🐳 Run the App Locally

```bash
docker-compose up --build
```

The app will be accessible at:

```
https://localhost
```

> ⚠️ You may need to accept the security warning in your browser due to the self-signed SSL certificate.

NGINX will route requests to one of the 3 FastAPI instances running behind it.

---

## ✅ Tech Stack

* FastAPI
* MongoDB
* Valkey (Redis-compatible cache)
* Motor (async MongoDB driver)
* redis-py (async Valkey/Redis client)
* Python-Jose (JWT)
* Passlib (bcrypt)
* Python-Dotenv *(only for local development)*
* Docker + Docker Compose
* NGINX (as reverse proxy + load balancer with SSL)
* GitHub Actions (CI/CD pipeline for Docker builds)

---

