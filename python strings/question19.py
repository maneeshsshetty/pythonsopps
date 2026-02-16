str1="a man is alive"
min=100
max=-1
letter_min=" "
letter_max=""
for i in str1.split(" "):
    min1=len(i)
    if min1<min:
        min=min1
        letter_min=i
for i in str1.split(" "):
    max1=len(i)
    if max1>max:
        min=min1
        letter_max=i
print(letter_min)
print(letter_max)
        