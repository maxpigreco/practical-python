# bounce.py
#
# Exercise 1.5


height = 100  # altezza da cui cade la palla
bounce = 0

for i in range(1, 11):
    bounce = height * 3 / 5
    height = bounce
    print(round(bounce, 4))
