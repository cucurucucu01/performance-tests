import time
import httpx

client = httpx.Client(base_url='http://localhost:8003', timeout=5)

payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "TFgGH",
  "firstName": "Giugds",
  "middleName": "OIgcjdcuwey",
  "phoneNumber": "7345474768734"
}
response = client.post("/api/v1/users", json=payload)

print(response.text)