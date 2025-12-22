#binary file

with open("C:\\Users\\LENOVO\\Videos\\IMG_20251117_084040.jpg","rb") as f:

    content = f.read()
    print(content)


with open("copy_img.jpg", "wb") as f:
    f.write(content)




















