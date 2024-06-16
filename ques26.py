def check_starts_with(string, prefix):
    return string.startswith(prefix)

def check_ends_with(string, suffix):
    return string.endswith(suffix)

my_string = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"
print("Prefix:",check_starts_with(my_string,prefix_to_check))
print("Suffix:", check_ends_with(my_string,suffix_to_check))