import re
from google.colab import files
import os
def getNextNumber(numbers_iterator):
  try:
    return int(next(numbers_iterator))
  except StopIteration:
    return None
def processPage(file_content):
  numbers_str_list = re.findall(r'\d+', file_content)
  numbers_iterator = iter(numbers_str_list)
  page_sum = 0
  while True:
    number = getNextNumber(numbers_iterator)
    if number is None:
      break
    page_sum += number
  return page_sum
overall_total_sum = 0

print("Please upload your text files (pages of the book).")
uploaded = files.upload()

if not uploaded:
  print("No files were uploaded.")
else:
  for filename, file_content_bytes in uploaded.items():
    print(f'Processing file "{filename}"')
    try:
      file_content = file_content_bytes.decode('utf-8')
      page_sum = processPage(file_content)
      print(f"The sum of all numbers in '{filename}' is: {page_sum}")
      overall_total_sum += page_sum

    except Exception as e:
      print(f"Error processing file {filename}: {e}")

  print(f"\nOverall sum of numbers across all files: {overall_total_sum}")
