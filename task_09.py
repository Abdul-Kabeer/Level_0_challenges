def extract_vowels(data):
    data = data.lower()
    vowels = ['a','e','i','o','u']
    vowels_list = []
    for i in data:
        if i in vowels:
            vowels_list.append(i)
    print("Vowels: " + ", ".join(set(vowels_list)))   

extract_vowels("Real") 