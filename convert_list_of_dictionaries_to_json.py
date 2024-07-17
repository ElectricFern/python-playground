import json

def dump_a_list_of_dictionaries_to_json_file():

  accounts = [
      {"account_id": 1, "username": "Jett", "datetime_created": "1997-07-16T19:20:10+05:30", "role": "administrator"},
      {"account_id": 2, "username": "Jack", "datetime_created": "1998-05-12T16:12:05+05:30", "role": "auditor"},
      {"account_id": 4, "username": "Jane", "datetime_created": "2020-06-04T21:31:56+05:30", "role": "editor"},
      {"account_id": 3, "username": "Jill", "datetime_created": "2004-04-04T19:04:32+05:30", "role": "editor"},
  ]
  directory = "./files_to_dump_json_into/data.json"
  print(f"dumping data into {directory}")
  with open(directory, "w") as final:
    json.dump(accounts, final)

  # final = json.dumps(accounts, indent=2)
  # print(final)

  # Filter the json for a user
  print(f"loading data from {directory}")
  with open(directory, "r") as unfinal_file:
    unfinal_json = json.load(unfinal_file)
    filtered_data = [user for user in unfinal_json if user["role"]=="auditor"]
    print("role auditor filtered data loaded from the json file", filtered_data)

if __name__ == "__main__": 
    dump_a_list_of_dictionaries_to_json_file() 