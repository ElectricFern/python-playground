import os

def walk_and_print_file_paths():
  directory = './files_to_walk'
  file_paths = []
  for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  for file_name in file_paths: 
        print(file_name) 

if __name__ == "__main__": 
    walk_and_print_file_paths() 