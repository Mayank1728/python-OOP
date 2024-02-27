from random import randint
class Player:
 def __init__(self, name):
  self.name = name
  self.pos: int = 0
 
 def roll(self):
  return randint(1, 6)

 def option(self):
  return randint(0,2)
 
class Game:
 def __init__(self):
  self.p1 = Player("P1")
  self.p2 = Player("P2")
  self.goal = 10
 
 def start_game(self):
  chance = self.p2
  while(self.p1.pos < self.goal and self.p2.pos < self.goal):
   chance = self.p2 if chance == self.p1 else self.p1
   print(chance.name, "is Playing Now currently at ", chance.pos)
   curr = chance.option()
   diceroll = chance.roll()
   if curr == 0:
    pass # don't move anywhere
   elif curr == 1:
    chance.pos += diceroll
   else:
    chance.pos -= diceroll
    chance.pos = 0 if chance.pos < 0 else chance.pos
   slogan = "Pass" if curr == 0 else "Plus" if curr == 1 else "Sub"
   print("He got", diceroll, "with ", slogan)
   print("He advances to", chance.pos)
   if chance.pos > self.goal:
    print("He goes back to ", end = "")
    chance.pos -= diceroll
    print(chance.pos)

  if(self.p1.pos > self.goal):
   print("Player 1 wins")
  else: 
   print("Player 2 wins")


match_one = Game()
match_one.start_game()
   
