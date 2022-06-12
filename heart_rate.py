"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""



howage= int(input("Please enter your age: "))

beat=220

ranget= beat - howage
bet01= .65
bet02= .85
bet03= ranget*bet01
bet04= ranget*bet02







print (f"When you exercise to strengthen your heart, you should keep your heart rate between {bet03} and {bet04} beats per minute.")



a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c

print (f"{result}")


import math

math.pi