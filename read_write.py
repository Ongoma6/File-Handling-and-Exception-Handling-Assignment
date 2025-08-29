# Read the content of 'notes.txt', print it, append a new line, and print the updated content.
with open('notes.txt', 'r') as f:
  content=f.read()
print(content)
with open('notes.txt', 'a') as f:
  f.write("\nDon't forget to review the OOP concepts.")
with open('notes.txt', 'r') as f:
  updated_content=f.read()
print(updated_content)  

#file handling with exception handling
try:
  with open('notes.txt', 'r') as f:
    content=f.read()
  print(content)
except FileNotFoundError:
  print("Error: The file 'notes.txt' was not found.")
except IOError:
  print("Error: An I/O error occurred while handling the file.")

