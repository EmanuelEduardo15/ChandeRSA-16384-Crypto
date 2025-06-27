<!-- ================== -->
<!--   ChQuantum Demo  -->
<!-- ================== -->

<p align="center">
  <!-- Logo PNG com fundo transparente, exibido sobre o fundo escuro do GitHub Dark Mode -->
  <img src="https://i.postimg.cc/XJF56tzt/Pilha-Eletromagn-tica.png" alt="ChQuantum Logo" width="200px" />
</p>

<p align="center">
  <!-- Imagem principal clicável -->
  <a href="https://postimg.cc/MvwJcJpg">
    <img src="https://i.postimg.cc/yYg1bV46/Privacy-zip-1.png" alt="Demonstração ChQuantum" width="600px" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/your-user/chquantum-demo/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/your-user/chquantum-demo/ci.yml?branch=main&style=for-the-badge&label=CI%20Status&logo=github" alt="CI Status">
  </a>
  <a href="https://your-user.github.io/chquantum-demo/">
    <img src="https://img.shields.io/badge/GitHub%20Pages-live-darkgreen?style=for-the-badge&logo=github-pages" alt="Pages">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/your-user/chquantum-demo?style=for-the-badge&logo=opensourceinitiative" alt="License">
  </a>
</p>

---

# 🚀 ChQuantum Demo Platform
ChandeRSA 16384 Crypto

> **Test your quantum-grade RSA/AES engine online**  
> From fast JWT auth to 16 384-bit RSA demos in under 4 seconds, all within a sleek dark-mode interface.

---

## 📖 Contents

1. [✨ Features](#-features)  
2. [🚀 Quick Start](#-quick-start)  
3. [📁 Structure](#-structure)  
4. [⚙️ Usage](#️-usage)  
5. [📊 CI & Testing](#-ci--testing)  
6. [🛡️ Security](#️-security)  
7. [🤝 Contributing](#-contributing)  
8. [📜 License](#-license)

---

## ✨ Features

- 🔐 **JWT Auth** (RSA-2048)  
- 🔑 **API Key** gatekeeping  
- ⚡ **RSA-16384 + AES-256** hybrid crypto  
- 📡 **FastAPI** backend (async + ProcessPool)  
- 🎨 **Dark-mode** inspired frontend (HTML/JS)  
- 🐳 **Docker & Compose** deployment  
- 🔧 **GitHub Actions CI** & **Locust** load tests  
- 🌐 **GitHub Pages** hosting

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/your-user/chquantum-demo.git
cd chquantum-demo

# Install backend
pip install -r requirements.txt

# Run API
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Serve frontend
cd frontend
python -m http.server 8080

# Access
# • API docs:  http://localhost:8000/docs
# • UI (dark mode): http://localhost:8080
