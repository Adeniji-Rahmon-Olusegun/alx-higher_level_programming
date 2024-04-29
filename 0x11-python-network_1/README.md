# 0x11. Python - Network #1
**Fetching Internet Resources with Python**

This README provides an overview of essential techniques for fetching and manipulating data from external services using Python. We'll explore two popular libraries: `urllib` (built-in) and `requests` (third-party).

**1. Using `urllib`**

**1.1. Fetching Resources**

The `urllib` module offers the `urllib.request.urlopen` function to retrieve content from a URL. Here's an example:

```python
import urllib.request

with urllib.request.urlopen("https://www.example.com") as response:
    data = response.read()
    print(data.decode("utf-8"))  # Decode using appropriate encoding
```

**1.2. Decoding Response Body**

The returned `data` from `urlopen` is typically in bytes format. Decode it using the correct encoding (often UTF-8):

```python
decoded_data = data.decode("utf-8")
```

**2. Using `requests` (Recommended)**

**2.1. Installation**

If you don't have `requests` installed, use pip:

```bash
pip install requests
```

**2.2. HTTP GET Requests**

The `requests` library offers a more user-friendly and feature-rich way to interact with web APIs. Here's how to make a GET request:

```python
import requests

response = requests.get("https://www.example.com")

if response.status_code == 200:  # Check for successful response
    data = response.text  # Response body is already decoded by default
    print(data)
else:
    print(f"Error: {response.status_code}")
```

**2.3. HTTP POST/PUT/etc. Requests**

`requests` supports various HTTP methods:

```python
# POST request with JSON data
data = {"key": "value"}
response = requests.post("https://api.example.com", json=data)

# PUT request with form data
data = {"name": "John", "age": 30}
response = requests.put("https://api.example.com/users/1", data=data)  # Use data= for form data

# You can similarly use requests.delete() and other methods
```

**2.4. Fetching JSON Resources**

To work with JSON data directly:

```python
response = requests.get("https://api.example.com/data.json")
data = response.json()  # Parses JSON into a Python dictionary
print(data["key"])  # Access data using dictionary keys
```

**3. Manipulating External Service Data**

Once you have the data from the external service, you can process it using Python's built-in data structures and functions:

```python
# Example: Filter data based on a condition
filtered_data = [item for item in data if item["age"] > 25]
```

**4. Additional Considerations**

- **Error Handling:** Always check the response's status code (`response.status_code`) to handle errors gracefully.
- **Authentication:** Some APIs require authentication headers or tokens. Use `requests.auth` for basic authentication or provide custom headers.
- **Timeouts:** Set timeouts for requests using `requests.get(..., timeout=5)`.
- **Advanced Usage:** `requests` offers a wealth of features like file uploads, session management, and more. Refer to the official documentation: [https://requests.readthedocs.io/](https://requests.readthedocs.io/)

**Conclusion**

This README provides a foundation for fetching and processing data from external services using `urllib` and `requests` in Python. By combining their strengths and considering error handling, authentication, timeouts, and advanced usage, you can build robust and flexible data interactions with web APIs.
