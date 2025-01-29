import zipfile

def unzip_file(zip_file_path, dest_dir):
  with zipfile.ZipFile("/home/ubuntu/behave-1.2.6.zip", 'r') as zip_ref:
    zip_ref.extractall("/home/ubuntu/")

zip_file_path = "/home/ubuntu/behave-1.2.6.zip"
dest_dir = "/home/ubuntu/"
unzip_file(zip_file_path, dest_dir)
print("Unzip completed successfully!")
