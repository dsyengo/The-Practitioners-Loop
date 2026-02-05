# Secure Full-Stack Portfolio 🚀

A high-performance, security-first professional portfolio showcasing engineering expertise and cybersecurity credentials. This project is built entirely with **Vanilla Web Technologies** and **Standard Python Libraries**, emphasizing clean code, lifecycle management, and minimal dependencies.

---

## 🏗️ Architecture Overview

The project follows a decoupled architecture, separating the interactive UI from the secure communication backend.

### 🎨 Frontend: Vanilla UI Engine

The frontend is built without frameworks (No React, No Bootstrap) to ensure maximum performance and total control over the DOM.

- **HTML5 & CSS3**: Utilizes **CSS Grid** and **Flexbox** for a fully responsive, modern layout that mimics high-end design systems.
- **Vanilla JavaScript**: Employs a **Data-Driven Rendering** approach. Project details, professional experiences, and certifications are stored in JS arrays and injected into the DOM dynamically.
- **Asynchronous Communication**: Uses the **Fetch API** to communicate with the Python backend via secure POST requests and handles CORS preflight handshakes.

### ⚙️ Backend: Vanilla Python SMTP Service

The backend is a lightweight, secure server built using Python’s standard library, focusing on secure communication protocols.

- **`http.server`**: A custom request handler manages incoming RESTful API calls without the overhead of Flask or Django.
- **`smtplib` & `email.mime`**: Implements the **Simple Mail Protocol** to handle professional inquiries directly from the contact form.
- **Security & Encryption**:
  - **STARTTLS**: Upgrades the connection to a secure, encrypted state before authentication.
  - **Environment Variables**: Leverages `.env` files to keep sensitive credentials (App Passwords) out of the codebase.
  - **CORS Management**: Explicitly defines allowed origins and methods to prevent Cross-Site Request Forgery (CSRF).

---

## 🛠️ Setup & Installation

### 1. Prerequisites

- Python 3.x
- A modern web browser
- An SMTP-enabled email account (e.g., Gmail with an App Password)

### 2. Environment Configuration

Create a `.env` file in the root directory:

```env
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-16-character-app-password


3. Running the Project
Start the Backend:
bash
python app.py
Use code with caution.

Launch the Frontend:
Open index.html via a local server (e.g., Live Server in VS Code at port 5500).
🏆 Key Features
Huawei ICT Competition Integration: Showcases Global Finalist achievements (Third Prize, Innovation Track) in AI and IoT.
Konza Technopolis Experience: Documents current DevOps internship within the ISCS Department and PDTP program involvement.
Cybersecurity Focus: Highlights core credentials, including the ISC² Certified in Cybersecurity (CC) and specialized Cisco Networking Academy certifications.
📝 License
Copyright © 2026 Denis Syengo. All rights reserved.
Built with security-first principles and professional dedication.
```
