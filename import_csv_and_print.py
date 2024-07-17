import csv

def import_csv_and_print():

  with open('import-student.csv', newline='') as f:
      next(f)
      reader = csv.reader(f)
      data= list(reader)
      print(data)

if __name__ == "__main__": 
    import_csv_and_print()