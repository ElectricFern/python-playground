import csv

def write_list_to_csv():

  Header = ['Name', 'class', 'finishYear', 'subject']
  Rows = [ ['James', '3rd', '2023', 'Physics'],  ['Jill', '2nd', '2022', 'M2'],  ['Joe', '1st', '2021', 'M4']] 

  with open('student.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(Header)
    write.writerows(Rows)


if __name__ == "__main__": 
    write_list_to_csv()