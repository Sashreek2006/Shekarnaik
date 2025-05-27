import re
from google.colab import files
import os

def get_next_number(file_path):
  with open(file_path, 'r') as f:
    lines = f.readlines()
    num_lines = len(lines)
    for i, line in enumerate(lines):
      try:
        
        number = int(line.strip())
        has_more = i < num_lines - 1
        yield (number, has_more)
      except ValueError:
    
        continue

def get_sum_and_count(file_path):
  total_sum = 0
  total_count = 0
  for number, has_more in get_next_number(file_path):
    total_sum += number
    total_count += 1

  print(f"\nTotal Sum: {total_sum}")
  print(f"Total Count: {total_count}")

def main():
  print("Please upload a text file with one number per line.")
  uploaded = files.upload()

  if not uploaded:
    print("No files were uploaded.")
    return

  filename = list(uploaded.keys())[0]
  print(f'User uploaded file "{filename}"')

  with open(filename, 'wb') as f:
      f.write(uploaded[filename])

  file_path = filename

  print("\n--- Demonstrating get_sum_and_count ---")
  get_sum_and_count(file_path)

  print("\n--- Demonstrating get_next_number directly ---")
  for number, has_more in get_next_number(file_path):
    print(f"Number: {number}, Has more: {has_more}")

if __name__ == "__main__":
  main()
