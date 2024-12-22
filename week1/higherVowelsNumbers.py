import requests

url = "https://raw.githubusercontent.com/fbrandao2k/Code_Challenging_Bentley/refs/heads/main/OCTO-Coding-Challenge-2024-Week-1-Part-2-input.txt"
response = requests.get(url)

if response.ok:
    vowels = "aeiouy"
    lines = response.text.lower().splitlines()
    
    most_vowels = 0
    line_with_most_vowels = ""
    i_most_vowels = 0
    
    for i, line in enumerate(lines, start=1):
        count_vowels = sum(line.count(vowel) for vowel in vowels)
        print(f"Line {i-1}: {count_vowels} vowels")
        # the ">=" ensures that if there is a tie, the highest index is chosen
        if count_vowels >= most_vowels:
            most_vowels = count_vowels
            line_with_most_vowels = line
            i_most_vowels = i-1
    
    print(f"The line with the most vowels ({most_vowels}) is line ({i_most_vowels}): \"{line_with_most_vowels}\"")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")

