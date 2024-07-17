from time import sleep

def process_first_data(data):
    print("Beginning first round of data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Finishing first round of data processing.")
    return modified_data

def process_second_data(modified_data):
    print("Beginning second round of data processing...")
    twice_modified_data = modified_data + " twice"
    sleep(3)
    print("Finishing second round of data processing.")
    return twice_modified_data

def main():
    print("BEGIN")
    data = "My data"
    modified_data = process_first_data(data)
    twice_modified_data_result = process_second_data(modified_data)
    print(twice_modified_data_result)
    print("END")

if __name__ == "__main__":

    main()
