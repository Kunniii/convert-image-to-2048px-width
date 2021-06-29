from PIL     import Image
from sys     import argv
from math    import floor
from os      import listdir, mkdir
from os.path import abspath, isdir

# # input series of files
# scan the dir
# take width and height
# calculate size relatively
# convert to png
# save

_w = 2048
the_path = ""
files = []
total = 0

if not argv[1:]:
    the_path = input("Drag and drop your folder here: ")
    if '"' in the_path:
        the_path = the_path.replace('"', '')
    if "'" in the_path:
        the_path = the_path.replace("'", "")
else:
    the_path = argv[1]

par_path = the_path
the_path = the_path + "\\converted"

if not isdir(the_path):
    mkdir(the_path)

def scan(par_path):
    lst = listdir(par_path)
    global files
    files = []
    for i in lst:
        if "." in i:
            if i.split(".")[1].lower() in ["jpg", "png"]:
                files.append(f"{par_path}\\{i}")
    with open(the_path+"\\file_dir.txt", "w+") as f:
        for i in files:
            print(i, file=f)
    global total 
    total = len(files)
    print(f"Found {total} files.")

def convert(img):
    ow = oh = 0
    iw = ih = 0

    i = Image.open(img);
    (iw, ih) = i.size
    
    scale = iw / _w

    ow = floor(iw / scale)
    oh = floor(ih / scale)

    i = i.resize((ow, oh))
    
    img = img.split("\\")[-1]

    # print(f"{img}", end="\r")
    
    i.save(f"{the_path}\\{img.split('.')[0]}.png")
    
    # print(f"{img} Done!")

def show_progress(total):
    leng = 50
    fill = "="
    remain = abs(len(files) - total)
    rate = remain / total
    filled = int(leng * rate)
    progress = fill * filled + " " * (leng - filled)
    t = f" [{remain}/{total}] | [{progress}]"
    print(t, end="\r")
    

def main():
    scan(par_path)
    while files:
        convert(files.pop())
        show_progress(total)

if __name__ == "__main__":
    main()
