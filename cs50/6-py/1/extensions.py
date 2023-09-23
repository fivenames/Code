filetype = input("Filename: ")

string = filetype.lower()

if string.endswith(".gif"):
    print("image/gif")
elif string.endswith(".jpg"):
    print("image/jpg")
elif string.endswith(".jpeg"):
    print("image/jpeg")
elif string.endswith(".png"):
    print("image/png")
elif string.endswith(".pdf"):
    print("application/pdf")
elif string.endswith(".txt"):
    print("document/txt")
elif string.endswith(".zip"):
    print("compressed/zip")
else:
    print("application/octet-stream")


