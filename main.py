import os
from nylas import APIClient

nylas = APIClient(
  os.getenv("CLIENT_ID"),
  os.getenv  ("CLIENT_SECRET"),
)


accounts = nylas.accounts.all()

for account in accounts:
  print("Email: {} | Billing State: {} | Sync State: {} | Account ID: {}".format(
  account.get('email'), account.get('billing_state'),
  account.get('sync_state'), account.get('account_id')
))