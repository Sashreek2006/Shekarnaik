import re
import os
from google.colab import files

# The files.upload() function uploads individual files, not folders directly.
# To handle a folder upload, you would typically upload a zip file
# or instruct the user to select multiple files.
# The following code assumes the user will select multiple text files
# when prompted by files.upload().

uploaded = files.upload()

overall_total_sum = 0

for filename in uploaded.keys():
  print(f'Processing file "{filename}"')
  # You can optionally save the uploaded files to a directory
  # For this example, we'll process them directly from the uploaded dictionary
  # with open(filename, 'wb') as f:
  #   f.write(uploaded[filename])

  try:
    # Decode the file content assuming it's a text file
    content = uploaded[filename].decode('utf-8')

    # Find all numbers in the content using regex
    numbers = re.findall(r'\d+', content)

    # Convert the found numbers to integers and sum them for the current file
    file_sum = sum(int(number) for number in numbers)
    print(f"The sum of all numbers in '{filename}' is: {file_sum}")

    # Add the file sum to the overall total sum
    overall_total_sum += file_sum

  except Exception as e:
    print(f"Error processing file {filename}: {e}")

print(f"\nOverall sum of numbers across all files: {overall_total_sum}")
