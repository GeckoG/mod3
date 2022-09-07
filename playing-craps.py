##import sys
##print(sys.version)
import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0

for roll in range (6000000):
    face = random.randrange(1,7) + random.randrange(1,7)
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1
    elif face == 7:
        frequency7 += 1
    elif face == 8:
        frequency8 += 1
    elif face == 9:
        frequency9 += 1
    elif face == 10:
        frequency10 += 1
    elif face == 11:
        frequency11 += 1
    elif face == 12:
        frequency12 += 1

print("Face        Frequency")
print("1          ",frequency1)
print("2          ",frequency2)
print("3          ",frequency3)
print("4          ",frequency4)
print("5          ",frequency5)
print("6          ",frequency6)
print("7          ",frequency7)
print("8          ",frequency8)
print("9          ",frequency9)
print("10         ",frequency10)
print("11         ",frequency11)
print("12         ",frequency12)
##print(f'{2:>4}{frequency2:>13}')
##print(f'{3:>4}{frequency3:>13}')
##print(f'{4:>4}{frequency4:>13}')
##print(f'{5:>4}{frequency5:>13}')
##print(f'{6:>4}{frequency6:>13}')
##print(f'{6:>4}{frequency7:>13}')
##print(f'{6:>4}{frequency8:>13}')
##print(f'{6:>4}{frequency9:>13}')
##print(f'{6:>4}{frequency10:>13}')
##print(f'{6:>4}{frequency11:>13}')
##print(f'{6:>4}{frequency12:>13}')

percentCraps = 100*((frequency2 + frequency3 + frequency12)/6000000)
percentCraps = round(percentCraps, 2)
print("You rolled craps ",(percentCraps), " percent of the time.")

percentWins = 100*((frequency7 + frequency11)/6000000)
percentWins = round(percentWins, 2)
print("You rolled a win ",(percentWins), " percent of the time.")
