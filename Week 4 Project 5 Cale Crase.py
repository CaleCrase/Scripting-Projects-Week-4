"""
Program: Project5 Crase
Author: Cale Crase
Population Growth Prediction
"""

organism = int(input("How many organisms are there: "))
rate = int(input("What is the growth rate(Make it greater than 0): "))
hour = int(input("How many hours will it take: "))
populations = int(input("What is the number of hours during which the population grows: "))

tp = organism
time = 1
while (time < populations):
    tp *=rate
    time += hour

print("The total population is:" +str(int(tp)))
