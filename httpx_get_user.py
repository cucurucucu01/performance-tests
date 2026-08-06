import httpx
import time

create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "TFgGH",
  "firstName": "Giugds",
  "middleName": "OIgcjdcuwey",
  "phoneNumber": "7345474768734"
}
response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)

# print(response.json())
# print(response.status_code)

response2 = httpx.get(f"http://localhost:8003/api/v1/users/{response.json()['user']['id']}")
print(response2.json())