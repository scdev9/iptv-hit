"""
This file is part of Scdev's iptvhit.  Scdev's iptvhit is free software: 
you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
Scdev's iptvhit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with Scdev's iptvhit.
If not, see <https://www.gnu.org/licenses/>. 
"""

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
