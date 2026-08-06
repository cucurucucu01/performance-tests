import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# data = {"userId":1,
#         "title": "delectus aut autem",
#         "completed": False
#         }
# response = httpx.post("https://jsonplaceholder.typicode.com/todos")
#
# print(response.json())
# print(response.status_code)

# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)

params = { "usedId":1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.json())
print(response.status_code)