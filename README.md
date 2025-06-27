<!-- ================== -->
<!--   ChQuantum Demo  -->
<!-- ================== -->

<p align="center">
  <img src="https://i.postimg.cc/XJF56tzt/Pilha-Eletromagn-tica.png" alt="ChQuantum Logo" width="180px" />
</p>

<p align="center">
  [![Demonstração ChQuantum](https://i.postimg.cc/yYg1bV46/Privacy-zip-1.png)](https://postimg.cc/MvwJcJpg)
</p>

<p align="center">
  <a href="https://github.com/your-user/chquantum-demo/actions"><img src="https://img.shields.io/github/actions/workflow/status/your-user/chquantum-demo/ci.yml?branch=main&style=for-the-badge&label=CI%20Status&logo=github" alt="CI Status"></a>
  <a href="https://your-user.github.io/chquantum-demo/"><img src="https://img.shields.io/badge/GitHub%20Pages-live-blueviolet?style=for-the-badge&logo=github-pages" alt="Pages"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/your-user/chquantum-demo?style=for-the-badge&logo=opensourceinitiative" alt="License"></a>
</p>

---

## 🌑 Dark Mode Preview

<details>
<summary>Click to expand demo animation</summary>

<video autoplay loop muted playsinline width="600">
  <source src="https://media.giphy.com/media/VxbvpfaTTo3le/giphy.mp4" type="video/mp4">
</video>

*Above: Dark-themed interface animation*

</details>

---

# 🚀 ChQuantum Demo Platform

**Test your quantum-grade RSA/AES engine online** – from fast JWT auth to 16 384-bit RSA demos in under 4 seconds.

---

## 📖 Table of Contents

1. [✨ Features](#-features)  
2. [🚀 Quick Start](#-quick-start)  
3. [📁 Project Structure](#-project-structure)  
4. [⚙️ Usage](#️-usage)  
   1. [Authentication (JWT)](#1-authentication-jwt)  
   2. [Generate API Key](#2-generate-api-key)  
   3. [Run Crypto Demo](#3-run-crypto-demo)  
5. [📊 Testing & CI/CD](#-testing--cicd)  
6. [🛡️ Security & Best Practices](#️-security--best-practices)  
7. [🤝 Contributing](#-contributing)  
8. [📜 License](#-license)

---

## ✨ Features

- 🔐 **JWT Authentication** with RSA-2048  
- 🔑 **API-Key** protection for demo endpoints  
- ⚡ **RSA-16384-bit** engine + **AES-256** hybrid crypto  
- 📡 **FastAPI** backend with async & multiprocessing  
- 🎨 **Dark-mode-inspired** static frontend (HTML + JS)  
- 🐳 **Docker & Docker-Compose** deployment  
- 🔧 **CI** via GitHub Actions & **Locust** load-testing  
- 🌐 **GitHub Pages** hosting for front-end  

---

## 🚀 Quick Start

```bash
# 1) Clone repository
git clone https://github.com/your-user/chquantum-demo.git
cd chquantum-demo

# 2) Install backend dependencies
pip install -r requirements.txt

# 3) Launch FastAPI backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 4) Serve frontend (in separate shell)
cd frontend
python -m http.server 8080

# 5) Browse
# Backend Swagger: http://localhost:8000/docs
# Frontend UI:    http://localhost:8080
