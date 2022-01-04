from PIL        import Image
from sys        import argv
from math       import floor
from os         import listdir, mkdir
from os.path    import abspath, isdir
from threading  import Thread

# # input series of files
# scan the dir
# take width and height
# calculate size relatively
# convert to png
# save

files = []

if not argv[1:]:
    the_path = input("[ >>>> ] Drag or enter path to your folder: ")
    the_path = the_path.strip()
    the_path = the_path.replace('"', '')
    the_path = the_path.replace("'", "")
else:
    the_path = argv[1]

try:
    _w = int(input("[ >>>> ] Enter pixel to convert (default 2048px): "))
except:
    _w = 2048

try:
    _t = int(input("[ >>>> ] Enter amount of thread (default is 1): "))
except:
    _t = 1

par_path = the_path
the_path = the_path + "/converted"

if not isdir(the_path):
    mkdir(the_path)

def scan(par_path):
    lst = listdir(par_path)
    global files
    files = []
    for i in lst:
        if "." in i:
            if i.split(".")[1].lower() in ["jpg", "png", "jpeg"]:
                files.append(f"{par_path}/{i}")
    with open(the_path+"/file_dir.txt", "w+") as f:
        for i in files:
            print(i, file=f)
    global total 
    total = len(files)
    print(f"[ **** ] Found {total} images.\n")

def convert():
    global files
    while files:
        img = files.pop(0)
        ow = oh = 0
        iw = ih = 0

        i = Image.open(img);
        (iw, ih) = i.size
        
        scale = iw / _w

        ow = floor(iw / scale)
        oh = floor(ih / scale)

        i = i.resize((ow, oh))
        
        img = img.split("/")[-1]
        
        i.save(f"{the_path}/{img.split('.')[0]}.png")
        
    else:
        return

def show_progress():
    from time import sleep
    s = 0.1
    while True:
        converted = abs(total - len(files))
        t = f"<-     > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"< -    > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<  -   > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<   -  > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<    - > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<     -> Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s+s)
        converted = abs(total - len(files))
        t = f"<    - > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<   -  > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<  -   > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"< -    > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        converted = abs(total - len(files))
        t = f"<-     > Converting [{converted}/{total}] images."
        print(t, end='\r')
        sleep(s)
        if not files:
            converted = abs(total - len(files))
            print(f"[ Done ] Converted [{converted}/{total}] images")
            return

def convert_files():
    a = Thread(target=show_progress)
    a.start()
    workers = []
    for i in range(_t):
        workers.append(Thread(target=convert))       
    for x in workers:
        x.start()
    for x in workers:
        x.join()
    a.join()

def main():
    scan(par_path)
    convert_files()

if __name__ == "__main__":
    main()
