import os


#path = '/home/rachna/Desktop/dockerdemo/test_folder'
 path ='/mnt/shared_from_host'

for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as f:
        if filename.endswith("txt"):
            c = 0
            for line in f.readlines():
                c += len(line.split())
            print("Filename:", filename, "Word Count:", c)