import os

for root, dir, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.endswith('.txt'):
            print(f"{root}/{file}")
