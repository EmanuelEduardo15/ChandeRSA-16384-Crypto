<!-- ================== -->
<!--   ChQuantum Demo  -->
<!-- ================== -->

<p align="center">
  <img src=" https://i.postimg.cc/XJF56tzt/Pilha-Eletromagn-tica.png" alt="ChQuantum Logo" width="180px" />
</p>

<p align="center">
  [![Demonstração ChQuantum](https://i.postimg.cc/yYg1bV46/Privacy-zip-1.png)](https://postimg.cc/MvwJcJpg)
</p>

<p align="center">
  <a href="https://github.com/your-user/chquantum-demo/actions"><img src="https://img.shields.io/github/actions/workflow/status/your-user/chquantum-demo/ci.yml?branch=main&style=for-the-badge&label=CI%20Status&logo=github" alt="CI Status"></a>
  <a href="https://your-user.github.io/chquantum-demo/"><img src="https://img.shields.io/badge/GitHub%20Pages-live-blueviolet?style=for-the-badge&logo=github-pages" alt="Pages"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/your-user/chquantum-demo?style=for-the-badge&logo=opensourceinitiative" alt="License"></a>
  <a href="https://postimg.cc/MvwJcJpg"><img src="https://img.shields.io/badge/Architecture–Diagram-black?style=for-the-badge" alt="Architecture"></a>
</p>

---

## 🌑 Dark Mode Preview

<details>
<summary>Click to expand <code>index.html</code> Dark Theme Preview</summary>

<video autoplay loop muted playsinline width="600">
  <source src="https://media.giphy.com/media/VxbvpfaTTo3le/giphy.mp4" type="video/mp4">
</video>

*Above: Example dark-themed interface animation*

</details>

---

## 🚀 ChQuantum Demo Platform

> **Test your quantum-grade RSA/AES engine online**  
> from fast JWT auth to 16 384-bit RSA demos in under 4 seconds.

---

## 📖 Table of Contents

1. [✨ Features](#-features)  
2. [🚀 Quick Start](#-quick-start)  
3. [📁 Project Structure](#-project-structure)  
4. [⚙️ Usage](#️-usage)  
   - [1. Authentication (JWT)](#1-authentication-jwt)  
   - [2. Generate API Key](#2-generate-api-key)  
   - [3. Run Crypto Demo](#3-run-crypto-demo)  
5. [📊 Testing & CI/CD](#-testing--cicd)  
6. [🛡️ Security & Best Practices](#️-security--best-practices)  
7. [🧑‍🤝‍🧑 Contributing](#-contributing)  
8. [📜 License](#-license)

---

## ✨ Features

- **🔐 JWT Authentication** with RSA-2048  
- **🔑 API-Key** protection for demo endpoints  
- **⚡ RSA-16384-bit** engine + **AES-256** hybrid crypto  
- **📡 FastAPI** backend with async & multiprocessing  
- **🎨 Dark-mode-inspired** static frontend (HTML + JS)  
- **🐳 Docker & Docker-Compose** for containerized deploy  
- **🔧 CI** via GitHub Actions & **Locust** load-testing  
- **🌐 GitHub Pages** hosting for front-end  

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

# 5) Browse 👇
# Backend Swagger: http://localhost:8000/docs
# Frontend UI:    http://localhost:8080


⸻

📁 Project Structure

chquantum-demo/
├── .github/                   # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml
│       ├── deploy-backend.yml
│       └── load-test.yml
│
├── app/                       # FastAPI backend
│   ├── main.py                # API routes & dependencies
│   ├── token_rsa.py           # JWT-RSA2048 auth module
│   ├── api_key.py             # API-Key generation & validation
│   └── turbo_demo.py          # RSA-16384 + AES engine (cached)
│
├── frontend/                  # Static site (HTML + JS)
│   ├── index.html             # Demo page with dark-inspired CSS
│   └── script.js              # Frontend logic
│
├── deploy/                    # Docker & Compose
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation


⸻

⚙️ Usage

1. Authentication (JWT)

curl -s -X POST http://localhost:8000/auth \
     -H "Content-Type: application/json" \
     -d '{"user":"investidor1"}'

<details>
<summary>Example Response</summary>


{ "token": "eyJhbGc…snip…fQ" }

</details>



⸻

2. Generate API Key

curl -s -X POST http://localhost:8000/generate_key \
     -H "Authorization: Bearer <JWT_TOKEN>"

<details>
<summary>Example Response</summary>


{ "api_key": "a3f5b1c9…ff12" }

</details>



⸻

3. Run Crypto Demo

curl -s -X POST http://localhost:8000/demo \
     -H "Authorization: Bearer <JWT_TOKEN>" \
     -H "X-API-Key: <API_KEY>" \
     -H "Content-Type: application/json" \
     -d '{"message":"Olá Mundo"}'

<details>
<summary>Example Response</summary>


{
  "user": "investidor1",
  "plaintext": "Olá Mundo",
  "decrypt_time_s": 3.42
}

</details>



⸻

📊 Testing & CI/CD

🛠️ Continuous Integration
	•	.github/workflows/ci.yml
	•	Lint with flake8
	•	Run pytest

🚀 Deployment
	•	Heroku: .github/workflows/deploy-backend.yml
	•	Docker-Compose: deploy/docker-compose.yml

🐳 Docker

docker-compose up --build

🔥 Load Testing
	•	Locust: run headless in CI or locally
	•	locust --headless --users 20 --spawn-rate 5 --run-time 1m --csv=reports/locust


⸻

🛡️ Security & Best Practices
	•	HTTPS with Let’s Encrypt
	•	CORS restricted to your domains
	•	Rate Limiting on /demo
	•	Env-based Config for secrets & keys
	•	Monitoring via Prometheus + Grafana

⸻

🧑‍🤝‍🧑 Contributing
	1.	Fork & clone
	2.	Create feature branch
	3.	Commit & open PR
	4.	Pass CI & merge

Read CONTRIBUTING.md & CODE_OF_CONDUCT.md.

⸻

📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

⸻

© 2025 ChQuantum Technologies. All rights reserved.

**Next Steps:**  
1. Replace all `your-user/chquantum-demo` references with your GitHub username and repo name.  
2. Commit this `README.md` to the root of your project.  
3. Push and enjoy the **sophisticated**, **dark-mode-inspired** documentation with badges, images, and interactive demos!
