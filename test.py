import re

t = "erewrjxgdhhh"
n = 2
print(t[0:9:n])
print("956.8".isnumeric())
t = "32.8 * X^1 +"
pattern = '^(0|[1-9]\d*)(\.\d+)?\s\*\sX\^(0|[1-9]\d*)'
# x = re.search("^\d+(\.\d+)?", t)     
# x = re.search("^(0|[1-9])\d*(\.\d+)?$", t)   
x = re.search(pattern, t)
def func(str):
    print(str)

text = "hello8"

func(text[1])

x = (4, 7)

print(x[0])
pattern1 = r"\d\d"
pattern2 = pattern1 + r"\d"
x = re.search(pattern2, "224")
print("dfgdg", x)