import os

def rename_files():
  file_list = os.listdir(r"/Users/anthonyso/Documents/programs/udacity/python-foundation/prank")
  print(file_list)
  saved_path = os.getcwd()
  print("Current working directory is "+saved_path)
  os.chdir(r"/Users/anthonyso/Documents/programs/udacity/python-foundation/prank")

  for filename in file_list:
    print("Old name - " + filename)
    new_name = filename.translate(None, "1234567890")
    print("New name - " + new_name)
    os.rename(filename, new_name)
  os.chdir(saved_path)

rename_files()
