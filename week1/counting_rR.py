import requests

#please change your url here. For credentials another approach would be necessary - for security reasons
#The code could be shorter, for example: input("Enter the URL: ")
url = "https://raw.githubusercontent.com/fbrandao2k/Code_Challenging_Bentley/5897e6600691feb66634c5b61c57a93e26f9a862/OCTO-Coding-Challenge-2024-Week-1-Part-1-input.txt"

#downloads the url and counts the number or r's and R's
response = requests.get(url)
if response.ok:
    count_r = response.text.lower().count('r')
    print(f"The number of 'r' and 'R' letters in the text is: {count_r}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")