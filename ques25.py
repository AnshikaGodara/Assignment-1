with open("C:/Users/anshi/OneDrive/Desktop/Python and ML/Practice.txt", mode = 'r') as source_file, open("C:/Users/anshi/OneDrive/Desktop/Python and ML/Practice2.txt", mode ='w')as destination_file:
    content = source_file.read()
    destination_file.write(content)
print("Content Copied")
