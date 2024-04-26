# 0x10. Python - Network #0: Understanding Web Communication Fundamentals

This repository delves into the core concepts that underpin communication on the web, using Python for potential code examples where applicable. The focus is on building a solid foundation in HTTP and related network protocols.

**Essential Web Concepts**

* **What a URL is (Uniform Resource Locator):** A URL acts as an address that identifies a specific resource on the internet. It follows a standard format with various components, like protocol, domain name, path, and query string.
* **What HTTP (Hypertext Transfer Protocol) is:**  HTTP establishes the communication rules between web browsers and servers. It defines how data is exchanged, including request formats, response structures, and error codes.
* **How to read a URL:** Breaking down a URL into its constituent parts:
    * **Scheme:** The protocol used (e.g., `http`, `https`).
    * **Domain Name:** The website's unique identifier (e.g., `google.com`).
    * **Subdomain (Optional):** A subdivision within the domain (e.g., `mail.google.com`).
    * **Port Number (Optional):** Specifies the communication port on the server (e.g., port 80 for HTTP).
    * **Path:** Identifies a specific resource or file within the domain (e.g., `/search`).
    * **Query String (Optional):** Parameters passed to the server for dynamic content (e.g., `?q=python`).
* **What a domain name is:** A human-readable address used to locate websites, replacing complex IP addresses.
* **What a subdomain is:** A further division within a domain, often used for specific functionalities (e.g., `mail.google.com` for email).
* **How to define a port number in a URL:** The port number is typically omitted (defaulting to 80 for HTTP and 443 for HTTPS) but can be explicitly included after a colon following the domain name (e.g., `http://www.example.com:8080`).
* **What a query string is:** A section of the URL containing key-value pairs used to pass data to the server (e.g., `?q=python` in `https://www.google.com/search?q=python`).
* **What an HTTP request is:** A message initiated by the browser to fetch a resource from a web server. It includes the request method (e.g., GET, POST), URL, headers, and an optional body containing data.
* **What an HTTP response is:** The server's reply to an HTTP request. It contains a status code (e.g., 200 for success, 404 for not found), headers, and an optional body with the requested content.
* **What HTTP headers are:** Key-value pairs appended to both requests and responses, providing additional information like content type, encoding, and authentication.
* **What the HTTP message body is:** The optional data section of an HTTP request or response used to send or receive content like form submissions or images.
* **What an HTTP request method is:**  An indicator specifying the intended action on the server. Common methods include GET (retrieval), POST (submission), PUT (update), DELETE (removal), etc.
* **What an HTTP response status code is:** A three-digit code conveying the outcome of the request to the browser. Common codes include:
    * 200 (OK): Success
    * 301 (Moved Permanently): Resource relocated
    * 404 (Not Found): Resource not found
    * 500 (Internal Server Error): Server-side issue
* **What an HTTP Cookie is:** A small piece of data stored on the client's machine that helps servers maintain state information across requests.
* **How to make a request with cURL:** cURL is a command-line tool that allows you to send HTTP requests directly from your terminal.

**What happens when you type google.com in your browser (Application Level):**

1. **DNS Lookup:** The browser doesn't understand domain names, so it queries a Domain Name System (DNS) server to translate `google.com` into its corresponding IP address.
2. **HTTP Request:** The browser builds an HTTP GET request targeting the IP address and the root path (`/`).
3. **Connection Establishment:** The browser establishes a TCP/IP connection with the web server at the obtained IP address.
4. **Request Sending:** The browser sends the crafted HTTP request to the server.
5. **Server Processing:** The server receives the request, processes it,
