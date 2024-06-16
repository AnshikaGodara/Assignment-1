def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Example usage:
your_string = "sample string"
frequency = count_character_frequency(your_string)
print(frequency)