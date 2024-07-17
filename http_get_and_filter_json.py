import requests
import json

def get_random_card():
  random_card_get_request = requests.get('https://api.scryfall.com/cards/random?q=is%3Acommander')
  random_card_json = random_card_get_request.text
  return random_card_json

def filter_name_and_oracle_text():
  input_data = json.loads(get_random_card())

  filtered_data = {key: input_data[key] for key in ["name", "oracle_text"]}

  print(filtered_data)

if __name__ == '__main__':
  filter_name_and_oracle_text()