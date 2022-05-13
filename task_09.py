#The following would extract and print the vowels found in string
def vowel_extract(data):
    data = data.lower()
    vowels = ['a','e','i','o','u']
    vowels_in_data = []
    for letter in data:
        if letter in vowels:
            vowels_in_data.append(letter)
    print("Vowels: " + ", ".join(set(vowels_in_data)))   


vowel_extract("Friend")      