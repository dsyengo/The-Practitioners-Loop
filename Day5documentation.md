# 🛠 Day 5 – SPA Routing & Hybrid Deployment Strategy

### 📌 Comparison Submit PR – Konza Technopolis Internship Log

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

```html
<main id="app"></main>
index.js dynamically injects view content into this container. This recreated
component-based rendering manually. 🔄 Lifecycle Re-Initialization Each route
included an init() callback to: Re-run DOM-dependent scripts Reinitialize
Intersection Observers Restore dynamic grid rendering This mimicked framework
lifecycle hooks such as: ngOnInit() (Angular) useEffect() (React) 📨 Backend –
Vanilla Python Mail Microservice A lightweight backend was built using:
http.server smtplib Python 3.10+ Purpose: Handle contact form submissions from
the static frontend. 🌐 REST Endpoint Implemented a POST handler Receives JSON
payload from frontend Sends email via SMTP 🔐 Input Validation Strategy
Client-Side Regex-based validation Server-Side String sanitization Payload
structure verification Field validation This enforced a multi-layer validation
model. 🌍 CORS Configuration Manually configured HTTP headers:
Access-Control-Allow-Origin Access-Control-Allow-Methods
Access-Control-Allow-Headers Also implemented: OPTIONS preflight handling
Explicit origin trust configuration Result: Secure cross-origin communication
between: GitHub Pages (Static) ↓ Python Backend (Dynamic) 2️⃣ What the Framework
Was Doing (Under the Hood) This project intentionally avoided frameworks to
expose what they automate. ⚙ Frontend Framework Responsibilities (Recreated
Manually) Framework Feature Manual Implementation Router Custom Hash-Router
Component Lifecycle init() callback DOM Diffing / Rendering Manual innerHTML
injection State Management Route-based logic 404 Fallback Hash-based routing
Insight Frameworks abstract routing, lifecycle control, and rendering logic. By
implementing these manually, the internal mechanics of SPAs became clear. 🧱
Backend Framework Responsibilities (Recreated Manually) Framework Feature Manual
Implementation Request Parsing Manual JSON parsing CORS Middleware Explicit
header injection Input Validation Libraries Custom validation logic Route
Handling Conditional method-based routing Environment Config Planned .env
integration Insight Frameworks like Django or Flask provide structure and secure
defaults. In this implementation, every responsibility was handled explicitly.
3️⃣ Deployment & Hybrid Architecture 🌐 Dual Hosting Strategy Layer Technology
Hosting Frontend Vanilla HTML5 + ES Modules GitHub Pages Backend Vanilla Python
(v3.10+) Render / VPS Routing Hash-Based SPA Routing Browser 🚧 Infrastructure
Decision Because GitHub Pages is static: History API routing resulted in 404
errors Switched to hash routing This ensured: index.html always loads first
JavaScript resolves route internally This reflects deployment-aware engineering
rather than purely frontend implementation. 4️⃣ Key Challenges & Solutions 🔴
Issue: 404 Errors on Refresh Cause: Static hosting cannot resolve dynamic
routes. Solution: Migrated to Hash Routing (#/route). Result: Removed server
dependency for route resolution. 🔴 Issue: CORS Blocking POST Requests Cause:
Browser security policies prevented cross-origin requests. Solution: Added CORS
headers Implemented OPTIONS preflight handling Explicitly trusted GitHub Pages
origin Result: Secure frontend-backend communication established. 5️⃣ Reflection
– Practitioner Growth Day 5 marked a shift from frontend implementation to
full-stack systems thinking. 📈 Technical Growth Understood how SPA routers work
internally Learned how static hosting constraints affect architecture Configured
CORS manually at protocol level Experienced the difference between local and
production environments 🧠 Architectural Realizations Frameworks reduce
complexity but hide mechanics Deployment constraints influence software design
Security must be explicitly engineered SPA behavior is structured DOM
orchestration ⚙ DevOps Awareness This phase reinforced: Environment separation
principles The importance of moving credentials to .env The need for CI/CD
automation (GitHub Actions)
```
