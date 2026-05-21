# what is web server ?

A **web server** is a software application (and sometimes the underlying hardware) that **hosts websites and delivers web content** to users over the **HTTP/HTTPS** protocol.

When a user types a URL in the browser, the browser sends a request to the web server. The server processes the request and sends back the response—such as **HTML pages, CSS, JavaScript, images, videos, or data**.

---

## How a web server works (simple flow)
1. **User requests a URL** in the browser.
2. **Browser sends an HTTP/HTTPS request** to the web server.
3. **Web server finds the requested resource** (page/file/API endpoint).
4. **Web server sends a response** back to the browser.
5. **Browser renders the page** for the user.

---

## Types / examples of web servers
Below are common web server software used in real systems:

### 1) Apache HTTP Server
- Very popular and widely used
- Open-source
- Supports many modules (security, caching, rewriting, etc.)

### 2) Nginx
- Known for high performance and efficient handling of many connections
- Often used for reverse proxy, load balancing, and caching

### 3) Microsoft Internet Information Services (IIS)
- Common in Windows environments
- Supports ASP.NET and Microsoft technologies

### 4) Tomcat
- Primarily a Java application server for running **Java Servlets/JSP**
- Often used together with a front web server like Nginx/Apache

### 5) WildFly (JBoss)
- Java-based application server
- Used for enterprise Java applications

### 6) WebLogic Server (Oracle)
- Enterprise Java application server
- Supports large-scale business applications

### 7) IBM WebSphere
- Enterprise application server
- Used in large organizations

---

## Basic functions of a web server
- **Serving static content**: HTML, CSS, images, files
- **Running server-side logic**: dynamic pages and APIs
- **Handling HTTP/HTTPS** requests
- **Authentication & authorization** (login/permissions)
- **Security features**: TLS/SSL, request filtering, rate limiting
- **Logging & monitoring** of traffic

---

## Web server vs Application server (quick difference)
- **Web server**: mainly handles HTTP/HTTPS and serves content.
- **Application server**: runs application logic (e.g., Java/.NET apps) and can work with a web server.

Many production systems use both, such as:
- Nginx (web/reverse proxy) + Tomcat (app)
- Apache (web) + Tomcat (app)

---

## Summary
A **web server** delivers web content to users using **HTTP/HTTPS**. Common web servers include **Apache, Nginx, and IIS**, and there are also application-focused servers like **Tomcat, WildFly, WebLogic, and WebSphere**.
