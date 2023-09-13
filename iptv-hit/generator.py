import random

# Define the length of the random numbers--------------------------------------------------------------------

random_length = 10  # You can change this to your desired length-----------------------------------------
num_numbers = 5000

# Generate and format the random numbers-----------------------------------------------------------------

random_numbers = []
for _ in range(num_numbers):
    random_number1 = ''.join([str(random.randint(0, 9)) for _ in range(random_length)])
    random_number2 = ''.join([str(random.randint(0, 9)) for _ in range(random_length)])
    random_numbers.append(f"{random_number1}:{random_number2}")

# Specify the file path to save the data----------------------------------------------------------------

file_path = 'Users.txt'

# Write the data to the file-------------------------------------------------------------------------------

with open(file_path, 'w') as file:
    file.write('\n'.join(random_numbers))

print(f"{num_numbers} random numbers ({random_length} digits each) saved to {file_path}")
