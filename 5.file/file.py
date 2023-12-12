import os

# if os.path.isfile("sample.txt"):

    # f = open('sample.txt', 'w')
    # print(f.writable())
    # f.close() #when we close the file the file object is deleted from "f" or memory
    # print(f.mode)
# else:
    # print("file does not exist")

# writing to a file
if os.path.isfile("sample.txt"):
    with open("sample.txt", mode='w') as f:
        lines = ["amsterdam\n", "lucknow\n", "zurich\n"]
        n = f.writelines(lines)
        # print(n)
else:
    print("file does not exist")

# reading a file
if os.path.isfile("sample.txt"):
    with open("sample.txt", mode='r') as f:
        data = f.readlines()
        # print(data)
        for lines in data:
            print(lines.strip())
else:
    print("file does not exist")
