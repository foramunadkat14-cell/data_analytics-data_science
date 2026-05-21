# what is client server architecture?

**Client–Server Architecture** is a software design where:
- A **Client** (user device/app/browser) requests services or data.
- A **Server** (powerful computer/service) processes the request and returns a response.

This architecture is used in most modern networks like web applications, online games, email systems, and APIs.

---

## Basic working (simple flow)
1. The **client** sends a request to the **server**.
2. The **server** processes the request.
3. The **server** sends back a response/data to the **client**.

Example (web):
- Browser (client) requests a webpage using a URL.
- Web server (server) returns HTML/CSS/JS/images.

---

## Key components
### 1) Client
- Runs on user devices (PC, mobile, browser)
- Sends requests and displays results
- Examples: web browser, mobile app, desktop app

### 2) Server
- Hosts services/resources (websites, databases, APIs)
- Handles requests, authentication, processing
- Examples: web server (Apache/Nginx/IIS), database server (MySQL), application server

### 3) Network
- Connects client and server
- Uses protocols like **HTTP/HTTPS**, **TCP/IP**, etc.

---

## Advantages
- **Centralized management** (data and services on the server)
- **Scalability** (add more servers/upgrade server capacity)
- **Security** (server controls access/authentication)
- **Easy maintenance** (clients rely on server updates)

---

## Disadvantages
- **Server dependency** (if server fails, many clients cannot access service)
- **Higher cost** (servers need resources and maintenance)
- **Network issues** (slow/internet problems affect performance)

---

## Types / variations
### 1) Two-tier architecture
- Client communicates directly with the server.
- Example: Browser (client) ↔ Web server (server)

### 2) Three-tier architecture
- Adds an additional middle layer.
- Example: Client ↔ Application server (business logic) ↔ Database server (data)

---

## Summary
**Client–Server Architecture** separates roles:
- Clients **request** services/data.
- Servers **process** and **respond**.

It is a common architecture for web applications and many network services.
