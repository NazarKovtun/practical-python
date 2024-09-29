# bounce.py
#
# Exercise 1.5
height = 100
count_fell = 0

while count_fell < 10:
    count_fell += 1
    height = height * 3 / 5
    print(count_fell, round(height, 4))
