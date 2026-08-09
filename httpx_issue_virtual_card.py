import httpx
import time

create_user_payload = {
  "email": f"user{time.time()}@example.com",
  "lastName": "TFgGH",
  "firstName": "Giugds",
  "middleName": "OIgcjdcuwey",
  "phoneNumber": "7345474768734"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

open_debit_card_payload = {"userId": create_user_response_data["user"]["id"]}

open_debit_card = httpx.post("http://localhost:8003/api/v1/accounts/open-debit-card-account", json=open_debit_card_payload)
open_debit_card_data = open_debit_card.json()

issue_virtual_card_payload = {"userId": create_user_response_data["user"]["id"],
                              "accountId": open_debit_card_data["account"]["id"]}

issue_virtual_card_response = httpx.post("http://localhost:8003/api/v1/cards/issue-virtual-card", json=issue_virtual_card_payload)
issue_virtual_card_data = issue_virtual_card_response.json()

print(issue_virtual_card_data)