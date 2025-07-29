# Python provides built-in functions to create, read, write, and delete files. It uses the open() function to handle files.
"""
| **Mode** | **Description**                                                      |
| -------- | -------------------------------------------------------------------- |
| `'r'`    | Read (default). Error if file does not exist.                        |
| `'w'`    | Write. Creates file if it does not exist, **overwrites** if it does. |
| `'a'`    | Append. Creates file if it does not exist, **adds to end** of file.  |
| `'x'`    | Create. Fails if file exists.                                        |
| `'b'`    | Binary mode (e.g., images, files).                                   |
| `'t'`    | Text mode (default).                                                 |
"""
mode = 'w'
file = open("filename.txt", mode)

# 2. Reading a File
file = open('example.txt', 'r')
content = file.read()   # Reads entire content
print(content)
file.close()

# Read line by line
file = open('example.txt', 'r')
for line in file:
    print(line.strip())
file.close()

# Read specific number of characters
file = open('example.txt', 'r')
data = file.read(5)  # Reads first 5 characters
print(data)
file.close()

# 3. Writing to a File
file = open('example.txt', 'w')
file.write("Hello World!\n")
file.write("Writing to a file in Python.")
file.close()

# 4. Appending to a File
file = open('example.txt', 'a')
file.write("\nAdding more content to the file.")
file.close()

# 5. Using with Statement (Best Practice)
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)

# 6. File Operations
file = open('example.txt', 'r')
print("File Name:", file.name)
print("File Mode:", file.mode)
print("Is File Closed:", file.closed)
file.close()

# 7. Deleting a File
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
else:
    print("The file does not exist")

'''
| **Operation** | **Method**                            |
| ------------- | ------------------------------------- |
| Open a file   | `open()`                              |
| Read a file   | `read()`, `readline()`, `readlines()` |
| Write         | `write()`                             |
| Append        | `append()`                            |
| Close a file  | `close()`                             |
| Delete file   | `os.remove()`                         |

'''