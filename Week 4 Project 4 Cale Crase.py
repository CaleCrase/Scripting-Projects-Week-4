"""
Program: Project4 Crase
Author: Cale Crase
Bouncing Ball
"""

height = int(input("How high did the ball dropped: "))
bounce = float(input("How many times did the ball bounced: "))
inital = float(input("What is the bounce's index number: "))

distance = 0
while bounce > 0:
    distance=distance + height
    height=height * inital
    distance=distance + height
    bounce-=1

    print("The total distance that the ball traveled is:",distance,"units")
