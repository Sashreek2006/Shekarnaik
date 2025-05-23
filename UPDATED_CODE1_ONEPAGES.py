import re
from google.colab import files
import os
uploaded = files.upload()
filename = list(uploaded.keys())[0]
print(f'User uploaded file "{filename}"')
file_content = uploaded[filename].decode('utf-8')
_numbers_iterator = iter(re.findall(r'\d+', file_content))

def getNextNumber():
  try:
    return int(next(_numbers_iterator))
  except StopIteration:
    return None

total_sum = 0
while True:
  number = getNextNumber()
  if number is None:
    break
  total_sum += number

print(f"The sum of all numbers in the file is: {total_sum}")
