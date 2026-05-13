import random
points = 0
chance = 3
while chance > 0:
    guess_num = int(input("Guess a number (0-9):"))
    orig_num = random.randint(0,9)
    print(orig_num)
    chance-=1
    if guess_num == orig_num:
        points+=1
print(f"Your score is --> {points}")
if points == 3:
    print("You Won !")
else:
    print("You Lost")
