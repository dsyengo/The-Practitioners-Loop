# 🛠 Day 5 – The Comparison

### 📌 Comparison Submit PR

---

## 📖 Overview

On Day 5, the portfolio evolved from a static multi-page structure into a **Single Page Application (SPA)** with a **hybrid deployment architecture**.

The objective was to:

- Implement client-side routing without frameworks
- Bridge a static frontend (GitHub Pages) with a dynamic backend (Python microservice)
- Understand what frameworks abstract by rebuilding core functionality manually
- Deploy in a production-like hybrid cloud environment

---

# 1️⃣ Working Bare-Metal / Vanilla Implementation

## 🖥 Frontend – Manual SPA (No Frameworks)

The application was refactored into a **Single Page Application (SPA)** using:

- Vanilla JavaScript (ES Modules)
- Manual Hash-based routing
- Dynamic DOM injection

No Angular, React, or routing libraries were used.

---

### 🔁 Routing Mechanism

Instead of using the History API (which caused 404 errors on GitHub Pages), a **Hash-Router** was implemented.

Example routes:

#/about
#/projects
#/contact

**Implementation strategy:**

- Used the `hashchange` event listener
- Browser always loads `index.html`
- JavaScript interprets the hash and renders the appropriate view

✔ Prevented GitHub Pages 404 refresh errors  
✔ Enabled SPA navigation on static hosting

---

### 🧩 View Injection Architecture

All UI sections were modularized in `views.js`.

The application shell:


<main id="app"></main>
The index.js controller dynamically injects view content into this container based on the active route.
This approach manually recreates component-based rendering without relying on a frontend framework.

---

### 🔄 Lifecycle Re-Initialization

- Each route definition included an init() callback responsible for:

- Re-running DOM-dependent scripts

- Reinitializing Intersection Observers

- Restoring dynamic grid rendering

- Rebinding event listeners when necessary

This design mirrors framework lifecycle hooks such as:

- ngOnInit() (Angular)

- useEffect() (React)

By implementing this manually, view rendering and lifecycle control were handled explicitly rather than abstracted.

---

### 📨 Backend – Vanilla Python Mail Microservice

A lightweight backend service was developed using:

- http.server

- smtplib

- Python 3.10+

---

### 🎯 Purpose

To handle contact form submissions from the static frontend and deliver messages via SMTP.

---

### 🌐 REST Endpoint

- Implemented a POST handler

- Receives JSON payloads from the frontend

- Parses and validates request body

- Sends email through SMTP server

---

### 🔐 Input Validation Strategy
- Client-Side

- Regex-based validation for email and required fields

- Server-Side

- String sanitization

- Payload structure verification

- Field-level validation

This established a multi-layer validation model to protect against malformed input and injection attempts.

---

### 🌍 CORS Configuration

**Manually configured HTTP headers:**

- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers


**Additionally implemented:**

- OPTIONS preflight request handling

-Explicit origin trust configuration

**Result**

- Secure cross-origin communication between:

- GitHub Pages (Static Frontend)
              ↓
- Python Backend Service (Dynamic)

---

### 2️⃣ What the Framework Was Doing (Under the Hood)

## ⚙ Frontend Framework Responsibilities (Recreated Manually)

| Framework Feature              | Manual Implementation            |
|--------------------------------|----------------------------------|
| Router                         | Custom Hash-Router               |
| Component Lifecycle            | `init()` callback                |
| DOM Diffing / Rendering        | Manual `innerHTML` injection     |
| State Management               | Route-based logic                |
| 404 Fallback Handling          | Hash-based routing               |

**Insight:**  
Frontend frameworks abstract routing, lifecycle management, state control, and rendering orchestration.  
By implementing these manually, the internal mechanics of Single Page Applications became fully transparent.
---

## 🧱 Backend Framework Responsibilities (Recreated Manually)

| Framework Feature              | Manual Implementation                |
|--------------------------------|--------------------------------------|
| Request Parsing                | Manual JSON parsing                  |
| CORS Middleware                | Explicit header injection            |
| Input Validation Libraries     | Custom validation logic              |
| Route Handling                 | Conditional method-based routing     |
| Environment Configuration      | Planned `.env` integration           |

 **Insight**

 Frameworks such as Django or Flask provide structured architecture, middleware layers, and secure defaults. In this implementation, every responsibility—from request parsing to security header configuration—was handled explicitly. 
---

## 3️⃣ Deployment & Hybrid Architecture  

### 🌐 Dual Hosting Strategy

| Layer     | Technology                      | Hosting Provider |
|-----------|----------------------------------|------------------|
| Frontend  | Vanilla HTML5 + ES Modules       | GitHub Pages     |
| Backend   | Vanilla Python (v3.10+)          | Render / VPS     |
| Routing   | Hash-Based SPA Routing           | Browser          |

### 🚧 Infrastructure Decision

Because GitHub Pages is a static hosting platform:

- History API routing resulted in 404 errors on refresh

- The solution was migrating to hash-based routing

This ensured:

- `index.html` always loads first

- JavaScript resolves the route internally

This decision reflects deployment-aware engineering rather than purely frontend implementation.

---

### 4️⃣ Key Challenges & Solutions
**🔴 Issue: 404 Errors on Refresh**

Cause:
Static hosting environments cannot resolve dynamic routes.

Solution:
Migrated to Hash Routing (#/route).

Result:
Removed server dependency for route resolution.

---

🔴 Issue: **CORS Blocking POST Requests**

Cause:
Browser security policies blocked cross-origin requests.

Solution:

- Added CORS headers

- Implemented OPTIONS preflight handling

- Explicitly trusted the GitHub Pages origin

Result:
Secure frontend-backend communication was successfully established.

---

### 5️⃣ Reflection – Practitioner Growth

Day 5 represented a shift from frontend implementation toward full-stack systems thinking.
---

**📈 Technical Growth**

- Understood how SPA routers function internally

- Learned how static hosting constraints shape architectural decisions

- Configured CORS manually at the HTTP protocol level

- Experienced the operational difference between local and production environments
--

**🧠 Architectural Realizations**

- Frameworks reduce complexity but obscure internal mechanics

- Deployment constraints directly influence software design

- Security must be explicitly engineered in distributed systems

- SPA behavior is structured DOM orchestration, not hidden magic
--

**⚙ DevOps Awareness**

This phase reinforced:

- The importance of environment separation

- Moving sensitive credentials to .env

- The necessity of CI/CD automation (GitHub Actions)