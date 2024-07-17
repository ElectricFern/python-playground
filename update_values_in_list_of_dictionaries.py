from datetime import datetime
import pytz

def update_accounts_list():
  current_datetime = datetime.now(pytz.timezone('Pacific/Auckland')).strftime('%Y-%m-%dT%H:%M:%S%z')
  accounts = [
      {"account_id": 1, "username": "Jett", "datetime_created": "1997-07-16T19:20:10+05:30","last_modfied": "1997-07-16T19:20:10+05:30", "permissions": ["administrator", "editor"]},
      {"account_id": 2, "username": "Jack", "datetime_created": "1998-05-12T16:12:05+05:30","last_modfied": "1998-05-12T16:12:05+05:30", "permissions": ["auditor"]},
      {"account_id": 4, "username": "Jane", "datetime_created": "2020-06-04T21:31:56+05:30","last_modfied": "2020-06-04T21:31:56+05:30", "permissions": ["editor"]},
      {"account_id": 3, "username": "Jill", "datetime_created": "2004-04-04T19:04:32+05:30","last_modfied": "2004-04-04T19:04:32+05:30", "permissions": ["editor"]},
  ]
  print("original accounts list")
  for account in accounts:
    print(account)
  print("-----------------------------")

  # Add and remove the third dicts permissions
  accounts[0]["permissions"].append("superuser")
  accounts[0]["permissions"].pop(0)
  accounts[0]["last_modfied"] = current_datetime
  # Make changes selected by user rather than dict key
  for user in accounts:
    if user["username"] == "Jack":
      user["username"] = "Jackaroo"
      user["last_modfied"] = current_datetime
 
  print("updated accounts list")
  for new_account in accounts:
    print(new_account)
  print("-----------------------------")    

if __name__ == "__main__": 
    update_accounts_list() 