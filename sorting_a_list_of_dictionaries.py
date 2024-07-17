from datetime import datetime
# In here we will:
# Access dictionaries in the list and print it
# Access a key value pair in a dictionary and print it
# Sort our list of dictionaries in different ways and print them

def sorting_a_list_of_dictionaries():

  accounts = [
      {"account_id": 1, "username": "Jett", "datetime_created": "1997-07-16T19:20:10+05:30", "role": "administrator"},
      {"account_id": 2, "username": "Jack", "datetime_created": "1998-05-12T16:12:05+05:30", "role": "auditor"},
      {"account_id": 4, "username": "Jane", "datetime_created": "2020-06-04T21:31:56+05:30", "role": "editor"},
      {"account_id": 3, "username": "Jill", "datetime_created": "2004-04-04T19:04:32+05:30", "role": "editor"},
  ]
  # General account info unsorted
  for dictionary in accounts:
    print("unsorted", dictionary)
  print("-------------------------------------------")
  for account_dict in accounts:
    usernames = account_dict["username"]
    # Print each account dictionary
    print(usernames)
    # Filter for the editors and print their name
    if account_dict["role"] == "editor":
      print("editors:", account_dict["username"])
  print("-------------------------------------------")
  # Account info that is sorted by ID
  id_sorted_accounts = sorted(accounts, key=lambda x: x["account_id"])
  for id_sorted_account in id_sorted_accounts:
    print("sorted by id", id_sorted_account)
  print("-------------------------------------------")
  # Account info that is sorted by datetime created
  # YYYY-MM-DD HH:MM:SS+TZOFFSET
  accounts.sort(key = lambda x: datetime.strptime(x["datetime_created"], '%Y-%m-%dT%H:%M:%S%z'))
  for date_sorted_account in accounts:
    print("sorted by datetime_created", (date_sorted_account))
  

if __name__ == "__main__": 
    sorting_a_list_of_dictionaries() 







  # https://realpython.com/sort-python-dictionary/#judging-whether-you-want-to-use-a-sorted-dictionary
