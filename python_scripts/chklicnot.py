import os

for root,dir,files in os.walk("/home/ubuntu"):
    for file in files:
        if file.lower().startswith("license") or file.lower().startswith("notice"):
           print(f"{root}/{file}")

