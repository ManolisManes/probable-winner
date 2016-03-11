import random
import sys

def getNewBoard():
   # Create a new 10x10 board data structure.
   boardRow = []
   boardCol = []
   board = []
   for x in range(10): 
      boardRow.append(x)
      boardCol.append(x)

   board = [boardRow,boardCol]
   return board     

def getRandomChests():
   # Create a list of chest data structures (two-item lists of x, y int coordinates)
    chests = []
    chests.append([random.randint(0,9), random.randint(0,9)])
    print 'The treasure chest is at', (chests)
    return chests
    

def getPlayerPosition():
    #Initialize player's random position
    x,y = [random.randint(0,9),random.randint(0,9)]
    print "Player's position is at",x,y
    return x,y

def isValidMove(x, y):
  # Return True if the coordinates are on the board, otherwise False.
  return x >= 0 and x <= 9 and y >= 0 and y <= 9

def makeMove(board, chests):
  # Checks if move is valid
  # Calculates the distance from the treasure
  # If you find a treasure, prints a message and removes it from the list
  
 global x,y,GameOver
 
 if not isValidMove(x, y):
     return False
 distance = 20 #not possible distance
 for cx, cy in chests:
  distance  = (abs(cx-x)+abs(cy-y))
 print ('The distance is', (distance))

 if distance == 0 : #you found the current treasure!
       chests.remove([x,y])
       print 'You have found the treasure!\n'
       GameOver = True      
 else :
 
  move = raw_input('Where you would like to go? Type: up/down/right/left\n')
 
  if (move !='up' and move !='down' and move !='right' and move !='left'):   #checks move, changes list's items (coordinates)
    print ('invalid move')
  elif move == 'up':
    x -=1
  elif move == 'down':
    x +=1
  elif move == 'right':
    y +=1
  elif move == 'left':
    y -=1
      
  return x,y


GameOver=False
while True:   #game_setup
    
    if (GameOver == False):
     theBoard = getNewBoard()
     theChests = getRandomChests()
     x,y = getPlayerPosition()
    
     while (GameOver == False):
     
      newMove = makeMove(theBoard,theChests)    
