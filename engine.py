import random

product = 0
total = 0
correct1 = 0
correct2 = 0
score = 0
			
def checker(f,s): #evaluates player's input (f & s)
    global score
    global correct1 
    global correct2
    if (f, s) == (correct2, correct1) or (s, f) == (correct2, correct1):
        score += 1

def game(): #returns variables used in the game 
    global product 
    global total
    global correct1 #factor1
    global correct2 #factor2
    
    primer = 0 #avoids generating prime numbers as product
    while primer==0:
        product = random.randint(4,99)
        for x in range(2,product-1):
            if product%x == 0:
                primer+=1
        
    factor = random.randint(2,product-1) 
    while product%factor!=0:
        factor = random.randint(2,product-1)
    correct1 = factor
    correct2 = int(product/factor)
    total = correct1+correct2


'''
Sources:
Downey, A. B. (2012, October). How to Think Like a Computer Scientist [PDF].
Holkner, A. (2017, February 21). Pyglet Documentation [PDF].
'''
