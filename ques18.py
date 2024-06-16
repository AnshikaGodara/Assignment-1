input_string1 = input("Enter the 1st string here: ")
input_string2 = input("Enter the 2nd string here: ")
input_string1 = input_string1.replace(" ","").lower()
input_string2 = input_string2.replace(" ","").lower()
if(sorted(input_string1)==sorted(input_string2)):
    print("Anagrams")

else:
    print("Not anagram")