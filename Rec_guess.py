import random 

random_x1 = random.randint(0,15)
random_y1 = random.randint(0,15)
random_x2 = random_x1 + random.randint(2,10)
random_y2 = random_y1 + random.randint(2,10)

class Rec():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = (x2-x1) * (y2-y1)

    def check_xy(self, player_x, player_y):  
        if self.x2 > player_x > self.x1 and self.y2 > player_y > self.y1:
            return True
        else:
            return False
    
    def check_area(self, player_area):
        if player_area == self.area:
            return True
        else:
            return False

print("Guess the point (number between 1-24)")
playerX = input("input x : ")
playerY = input("input y : ")
print("Guess the area")
playerArea = input("input area : ")
rec = Rec(random_x1, random_y1, random_x2, random_y2)

if rec.check_xy(playerX, playerY):
    print("Nice!!, You win guessing the point")
else:
    print("You lose guessing the point")

if rec.check_area(playerArea):
    print("Yay!!, You win guessing the area")
else:
    print("You lose guessing the area")