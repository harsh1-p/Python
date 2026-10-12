import re

text = "My name is Harsh,harsh"

match = re.search("Harsh",text)
if match:
    print("Match found")
    print(match.start())
    print(match.end())

matches = re.findall("harsh",text,re.IGNORECASE)
print("Matches :",matches)

new_txt = re.sub("Harsh","Aryan",text)
print(new_txt)