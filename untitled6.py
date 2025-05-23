import re
from google.colab import files

# Upload the text file
uploaded = files.upload()

# Assuming only one file was uploaded
for filename in uploaded.keys():
  print(f'User uploaded file "{filename}"')
  with open(filename, 'r') as f:
    content = f.read()

  # Find all numbers in the content using regex
  numbers = re.findall(r'\d+', content)

  # Convert the found numbers to integers and sum them
  total_sum = sum(int(number) for number in numbers)

  print(f"The sum of all numbers in the file is: {total_sum}")

