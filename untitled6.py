import re
from google.colab import files
uploaded = files.upload()
for filename in uploaded.keys():
  print(f'User uploaded file "{filename}"')
  with open(filename, 'r') as f:
    content = f.read()
  numbers = re.findall(r'\d+', content)
  total_sum = sum(int(number) for number in numbers)
  print(f"The sum of all numbers in the file is: {total_sum}")

