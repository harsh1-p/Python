s = "hello world"

a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())


text = " Hello World "
print(text.strip())
print(text.lstrip())
print(text.rstrip())



text = "Python is fun"

print(text.find("is"))
print(text.replace("fun","awesome"))

text = "Apple,Banana,Grapes"
print(text.split(","))


text = "Python1234"

print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isspace())