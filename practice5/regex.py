import re

# 1 task
pattern1 = r"ab*"
text1 = input()
if re.fullmatch(pattern1, text1):
    print("Match")
else:
    print("No match")

# 2 task
pattern2 = r"ab{2,3}"
text2 = input()
if re.fullmatch(pattern2, text2):
    print("Match")
else:
    print("No match")

# 3 task
text3 = input()
pattern3 = r"[a-z]+_[a-z]+"
print(re.findall(pattern3, text3))

# 4 task
text4 = input()
pattern4 = r"[A-Z][a-z]+"
print(re.findall(pattern4, text4))

# 5 task
pattern5 = r"a.*b"
text5 = input()
if re.fullmatch(pattern5, text5):
    print("Match")
else:
    print("No match")

# 6 task
text6 = input()
print(re.sub(r"[ ,\.]", ":", text6))

# 7 task
text7 = input()
words7 = text7.split("_")
camel = words7[0]
for word in words7[1:]:
    camel += word.capitalize()
print(camel)

# 8 task
text8 = input()
print(re.findall(r"[A-Z][a-z]*", text8))

# 9 task
text9 = input()
print(re.sub(r"([A-Z])", r" \1", text9).strip())

# 10 task
text10 = input()
print(re.sub(r"([A-Z])", r"_\1", text10).lower())