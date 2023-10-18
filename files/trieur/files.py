import os

items = os.listdir()
dirs = [item for item in items if os.path.isdir(item)]

if "downloads" not in dirs:
    print("Le fichier 'downloads' n'existe pas !")
    exit(1)

download_items = os.listdir("downloads")
files = [item for item in download_items if os.path.isfile(f"downloads/{item}")]

for dir in ["music", "image", "video"]:
    if dir not in dirs:
        os.mkdir(dir)

for file in files:
    file_type = file.split('.')[1]

    match file_type:
        case "png":
            os.rename(f"downloads/{file}", f"image/{file}")
        case "mp3":
            os.rename(f"downloads/{file}", f"music/{file}")
        case "mp4":
            os.rename(f"downloads/{file}", f"video/{file}")