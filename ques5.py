user_input = input("Enter a string to save to file: ")
with open("C:/Users/anshi/OneDrive/Desktop/Python and ML/Practice.txt",'w') as file:
    file.write(user_input)
print("Your input hass been saved to file")