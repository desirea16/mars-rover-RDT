class Plateau:
  def __init__(self,max_x,max_y):
    self.max_y = max_y
    self.max_x = max_x
  def validmove(self,x,y):
    if (x >= 0 and x <= self.max_x) and (y >= 0 and y <= self.max_y):
      return True 
    else: 
      return False 

class Rover: 
  def __init__(self,x,y,direction,plateau):
    self.x = x 
    self.direction = direction 
    self.y = y 
    self.plateau = plateau

  def leftspin (self):
      if self.direction =="N": 
        self.direction = "W"
      elif self.direction =="W": 
        self.direction = "S"
      elif self.direction =="S": 
        self.direction = "E"
      elif self.direction =="E": 
          self.direction = "N"

  def rightspin (self):
    if self.direction =="N": 
      self.direction = "E"
    elif self.direction =="E": 
      self.direction = "S"
    elif self.direction =="S": 
      self.direction = "W"
    elif self.direction =="W": 
        self.direction = "N"


  def move(self):
    newx = int(self.x)
    newy = int(self.y)

    if self.direction == "N":
      newy = newy + 1
    elif self.direction == "S": 
      newy = newy - 1
    elif self.direction == "E":
      newx = newx + 1
    elif self.direction == "W":
      newx = newx - 1
      
    if self.plateau.validmove(newx,newy) == True : 
      self.x = newx
      self.y = newy
    

  def instructionss(self,instructions):
    for i in instructions: 
      if i == "L":
        self.leftspin()
      elif i == "R":
        self.rightspin()
      elif i == "M":
        self.move()


  def finalpos (self):
    x_string = str(self.x)
    y_string = str(self.y)
    
    finalstring = x_string + " " + y_string + " " + self.direction 
    return finalstring
    

plat = input("Please enter 2 numbers as the area of your plateau:")

plat_parts = plat.split()
max_x = int(plat_parts[0])
max_y = int(plat_parts[1])

marsplat = Plateau (max_x,max_y)

rover1_pos = input("Please enter the position of the first rover: ")
rover1_instruction = input("Enter the instructions for your first rover:")
rover1_pos_parts = rover1_pos.split()
xstart = int(rover1_pos_parts[0])
ystart = int(rover1_pos_parts[1])
directionstart =rover1_pos_parts[2]

rover1 = Rover(xstart,ystart,directionstart, marsplat)

rover1.instructionss(rover1_instruction)
print(rover1.finalpos())

rover2_pos = input("Please enter the position of the 2nd rover: ")
rover2_instruction = input("Enter the instructions for your first rover:")
rover2_pos_parts = rover2_pos.split()
xstart = int(rover2_pos_parts[0])
ystart = int(rover2_pos_parts[1])
directionstart =rover2_pos_parts[2]
rover2 = Rover(xstart,ystart,directionstart, marsplat)
rover2.instructionss(rover2_instruction)
print(rover2.finalpos())
