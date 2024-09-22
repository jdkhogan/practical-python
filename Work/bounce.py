# bounce.py
#
# Exercise 1.5

height = 100
bounce = 0.6
i = 1

while (i <= 10):
    height = height * bounce
    print(f'''{i} {round(height,4)}''')
    i = i + 1
    