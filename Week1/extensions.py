file = input("File name: ").lower().strip()
suffix = file[len(file)-3:]
if suffix == "gif":
    print("image/gif")
elif suffix == "jpg" or file[len(file)-4:] == "jpeg":
    print("image/jpeg")
elif suffix == "png":
    print("image/png")
elif suffix == "pdf":
    print("application/pdf")
elif suffix == "txt":
    print(f"text/{file[:file.find(".")]}")
elif suffix == "zip":
    print("application/zip")
else:
    print("application/octet-stream")

# In a file called extensions.py, implement a program that prompts the user for the name of a file and 
# then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream 
# instead, which is a common default.
