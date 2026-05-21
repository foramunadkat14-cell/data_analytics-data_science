# what is URL ?

A **URL (Uniform Resource Locator)** is the address of a resource on the internet. It tells your browser **where** to find something (a web page, an image, a file, or an API endpoint) and **how** to access it.

Example:
- `https://www.example.com/page1`

---

## URL parts (with meaning)
A typical URL has these components:

1. **Scheme / Protocol** (e.g., `http`, `https`)
   - Tells the browser which protocol to use.

2. **Domain name** (e.g., `www.example.com`)
   - Identifies the website server.

3. **Port** (optional, e.g., `:80`, `:443`)
   - Specific network port for the service.

4. **Path** (e.g., `/page1`)
   - Points to a specific location/resource on the website.

5. **Query string** (optional, e.g., `?id=10&cat=books`)
   - Sends parameters to the server (often used for search/filtering).

6. **Fragment / Anchor** (optional, e.g., `#section1`)
   - Jumps to a specific part of the page.

---

## Types of URL (common classification)
There are multiple ways to classify URLs, but the most common “types” are:

### 1) Absolute URL
- Contains the **full address**, including protocol and domain.
- Example: `https://www.example.com/products/item1`

### 2) Relative URL
- Contains only the path/relative location (no domain).
- Example (from a page in `/products/`): `item1` or `../item1`

### 3) Static URL
- Points to content that usually **does not change often**.
- Example: `https://www.example.com/about`

### 4) Dynamic URL
- Includes information (often via query parameters) that generates different responses.
- Example: `https://www.example.com/search?query=phones`

### 5) Domain-based URL
- Uses domain names to locate the resource.
- Example: `https://www.google.com/`

### 6) IP-based URL
- Uses an IP address instead of a domain name.
- Example: `http://192.168.1.10/index.html`

---

## URL formats by protocol (another useful view)
You may also see URLs categorized by protocol:
- **HTTP**: `http://example.com`
- **HTTPS**: `https://example.com` (secure via SSL/TLS)
- **FTP**: `ftp://example.com/file.txt`
- **Mailto**: `mailto:user@example.com`

---

## Why URLs are important
- Help browsers locate and load resources.
- Allow web navigation (links between pages).
- Enable APIs to specify endpoints and parameters.

---

## Summary
A **URL** is the internet address of a resource. It includes protocol, domain, path, and optional query/fragment. Common types include **absolute**, **relative**, **static**, and **dynamic** URLs.
