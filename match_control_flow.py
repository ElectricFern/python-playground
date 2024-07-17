def message_match():
  n = int(input("Enter a number between 1-5 (inclusive)"))
  match n:
    case 1:
      print("one")
    case 2:
      print("two")
    case 3:
      print("three")
    case 4:
      print("four")
    case 5:
      print("five")
    case _:
      print("failed to follow instructions, try again")
      message_match()

if __name__ == "__main__": 
    message_match() 
  