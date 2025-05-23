import re
import os
from google.colab import files
uploaded = files.upload()
overall_total_sum = 0
for filename in uploaded.keys():
  print(f'Processing file "{filename}"')
  try:
    content = uploaded[filename].decode('utf-8')
    numbers = re.findall(r'\d+', content)
    file_sum = sum(int(number) for number in numbers)
    print(f"The sum of all numbers in '{filename}' is: {file_sum}")
    overall_total_sum += file_sum

  except Exception as e:
    print(f"Error processing file {filename}: {e}")

print(f"\nOverall sum of numbers across all files: {overall_total_sum}")
