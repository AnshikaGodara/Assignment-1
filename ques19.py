import string
 
test_str = 'Coding, in! python ;'
 
test_str = test_str.translate(str.maketrans('', '', string.punctuation))
print(test_str)