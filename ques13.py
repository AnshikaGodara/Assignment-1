birth_year = int(input("Please enter your birth year: "))
from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year
print(age)