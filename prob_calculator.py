import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = list()

    def __init__(self, **kwargs):
      self.contents = list()  
      for key in kwargs.keys():
        for i in range(kwargs.get(key)):
          self.contents.append(key)
        

    def draw(self, num_balls_drawn):
        if num_balls_drawn <= len(self.contents):
          drawn_balls = list()
      
          for i in range(num_balls_drawn):
            x = random.randint(0, len(self.contents)-1)
            random_ball = self.contents.pop(x)
            drawn_balls.append(random_ball)
          return drawn_balls
        else:
          return self.contents   



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  M = 0.00
 
  for i in range(num_experiments):
    # we need deep copy because of list in class
    copy_hat = copy.deepcopy(hat)
    dct = dict()
    drawn_balls = copy_hat.draw(num_balls_drawn)
    for ball in drawn_balls:
        if ball not in dct:
            dct[ball] = 1
        else:
            dct[ball] += 1

    succ = 0  
    for key in expected_balls.keys():
      if key not in dct.keys():
        break
      elif int(expected_balls.get(key)) <= int(dct.get(key)):
        succ += 1
      else:
        break

    if succ == len(expected_balls.keys()):
      M += 1.00

  prob = M / num_experiments
  return prob