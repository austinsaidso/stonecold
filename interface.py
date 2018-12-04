import pyglet
import random
from pyglet.window import key
import engine


window = pyglet.window.Window(width=640, height=480)
window.set_location(400,100)



def loadhighscore(file):
    with open(file, 'r') as f:
        score = f.read()
    return score

def savehighscore(file, scr):
    with open(file, 'w') as f:
        f.write(str(scr))

def newhighscore(score):
    global highscore
    if score > int(highscore):
        savehighscore("hiscore.txt", score)
        

game_batch = pyglet.graphics.Batch()
gameover_batch = pyglet.graphics.Batch()
title_batch = pyglet.graphics.Batch()



        
#Text Labels for Title Screen/Window & Game Over Window
title_text = pyglet.text.Label("Factor Finder", x=window.width/(10/1.67), y=330, batch= title_batch)
title_text.bold = True
title_text.font_size = 50

rules1_text = pyglet.text.Label('Welcome to Factor Finder, Human! In this game, you are given two numbers.',
                                x = window.width/2, y = window.height/1.9, anchor_x = 'center', anchor_y = 'center', batch = title_batch)
rules1_text.font_size = 10

rules_text = pyglet.text.Label('The first number has its 2 factors that when added matches the second number.',
                               x = window.width/2, y = window.height/2.1, anchor_x = 'center', anchor_y = 'center', batch = title_batch)
rules_text.font_size = 10

rules2_text = pyglet.text.Label('Directions: For 60 seconds, answers as many questions as you can by entering the two factors.',
                                    x = 20, y = window.height/2.5, batch = title_batch)
rules2_text.font_size = 10

intro_text = pyglet.text.Label("Press SPACEBAR to play!", x=150 , y=130, batch = title_batch)
intro_text.italic = True
intro_text.bold = True
intro_text.font_size = 18

gameover_text = pyglet.text.Label("", x=80, y=300, batch = gameover_batch)
gameover_text.italic = False
gameover_text.bold = True
gameover_text.font_size = 40

retry_text = pyglet.text.Label("", x=100, y=200, batch = gameover_batch)
retry_text.italic = True
retry_text.bold = True
retry_text.font_size = 18
                    

def gameplay(): #run to play game
    #geting values in engine module
    score = engine.score  
    product = engine.product
    total = engine.total
    
    global highscore
    global highscorelabel_text
    global highscore_value
    global scorelabel_text
    global sum_text
    global product_text
    global whatfactor_text
    global timelabel_text
    global score_text

    #Text labels for Game Window or Screen
    timer.text = "60"
    timer.x = 600
    timer.y = 445
    gameover_text.text = ""
    retry_text.text = ""

    highscorelabel_text = pyglet.text.Label("High Score:", x=500, y=425, batch= game_batch)
    highscorelabel_text.bold = True
    highscorelabel_text.font_size = 10

    highscore = loadhighscore("hiscore.txt") # variable that gets high score from the file  
    highscore_value = pyglet.text.Label(highscore, x=595, y=425, batch= game_batch)
    highscore_value.font_size = 10

    scorelabel_text = pyglet.text.Label("Score:", x=500, y=405 , batch= game_batch)
    scorelabel_text.bold = True
    scorelabel_text.font_size = 10

    score_text = pyglet.text.Label(str(score), x=575, y=405 , batch= game_batch)
    score_text.bold = True
    score_text.font_size = 10

    timelabel_text = pyglet.text.Label("Time left:", x=500, y=445 , batch= game_batch)
    timelabel_text.bold = True
    timelabel_text.font_size = 10

    whatfactor_text = pyglet.text.Label("What factors of      is      when combined?", x= 60, y=240, batch= game_batch)
    whatfactor_text.bold = True
    whatfactor_text.font_size = 20

    product_text = pyglet.text.Label(str(product), x= 265, y=240 , batch= game_batch)
    product_text.bold = True
    product_text.font_size = 20

    sum_text = pyglet.text.Label(str(total), x= 335, y=240, batch= game_batch)
    sum_text.bold = True
    sum_text.font_size = 20

    #to display player's input
    number_input = pyglet.text.Label("", x= 200, y=150, batch= game_batch)
    number_input.bold = True
    number_input.font_size = 50
    
    number_input1 = pyglet.text.Label("", x= 370, y=150, batch= game_batch)
    number_input1.bold = True
    number_input1.font_size = 50



    @window.event
    def on_key_press(symbol, modifiers): #for Player's Input
        global seconds
        global inputno #for conditionals below to separate player's input
        global value1 #player's input no. 1
        global value2 #player's input no. 2
        global first_answer 
        global second_answer
        if symbol == key._1:
            number_list.append("1")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._2:
            number_list.append("2")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._3:
            number_list.append("3")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._4:
            number_list.append("4")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._5:
            number_list.append("5")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._6:
            number_list.append("6")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._7:
            number_list.append("7")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._8:
            number_list.append("8")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._9:
            number_list.append("9")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key._0:
            number_list.append("0")
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key.BACKSPACE:
            number_list.pop(len(number_list)-1) #when player erases portions of his answer
            if inputno%2 == 0:
                number_input.text = "".join(number_list)
            if inputno%2 == 1:
                number_input1.text = "".join(number_list)
        elif symbol == key.ENTER: 
            inputno += 1
            if inputno%2 == 1:
                if len(number_list)==0:
                    value1=0
                else:
                    value1 = int("".join(number_list))
                del number_list[0:len(number_list)]
            if inputno%2 == 0:
                if len(number_list)==0:
                    value2=0
                else:
                    value2 = int("".join(number_list))
                del number_list[0:len(number_list)]
                engine.checker(value1, value2)#evaluates if player's input 
                engine.game() #generates product, factors, total
                score = engine.score 
                product = engine.product
                total = engine.total
                number_input.text = ""
                number_input1.text = ""
            
        
    return game_batch.draw()


def updater(dt): #updates score and generates new product and total
    global score_text
    global product_text
    global sum_text
    score_text.text = str(engine.score)
    product_text.text = str(engine.product)
    sum_text.text = str(engine.total)


seconds = 1000
timer = pyglet.text.Label("", x= 700, y= 445, batch= game_batch)
timer.font_size = 10
timer.bold= True

def go_talo():
    newhighscore(engine.score)
    pyglet.clock.unschedule(updater)
    global seconds
    engine.score = 0 #reset score back to zero
    timer.text = ""
    highscorelabel_text.text = ""
    highscore_value.text = ""
    scorelabel_text.text = ""
    whatfactor_text.text = ""
    product_text.text = ""
    timelabel_text.text = ""
    sum_text.text = ""
    score_text.text = ""
    gameover_text.text = "Your Game is over!"
    retry_text.text = "Press SPACE: Retry, ESC: Quit Game"
    
    @window.event
    def on_key_press(symbol, modifiers):
        global seconds
        global inputno
        global value1
        global value2
        global first_answer
        global second_answer
        if symbol == key.SPACE:
            inputno = 0
            value1 = 10
            value2 = 10
            seconds = 62
            gameplay()
            engine.game()
            pyglet.clock.schedule_interval(updater, 1/100)

def update(dt):
    global seconds
    global timer
    if seconds>0: 
        seconds -= 1*dt
        timer.text = str(int(seconds))
    if seconds < 1: #end of game 
        go_talo()

    

value1 = 0
value2 = 0
score = 0
number_list = list()
inputno = 0


@window.event
def on_key_press(symbol, modifiers):
    global seconds
    global inputno
    global value1
    global value2
    global first_answer
    global second_answer
    if symbol == key.SPACE:
        title_text.text = "" #clears Title Screen
        intro_text.text = ""
        rules_text.text = ""
        rules2_text.text = ""
        rules1_text.text = ""
        seconds = 62
        gameplay() #to Display Game Screen
        engine.game() 
        pyglet.clock.schedule_interval(updater, 1/100) 





@window.event
def on_draw():
    window.clear()
    title_batch.draw() #Display Text on Title Screen
    game_batch.draw() #Display Text on  Gameplay Screen
    gameover_batch.draw() #Display Text when Game is Over

pyglet.clock.schedule_interval(update, 1) #For Timer 
pyglet.app.run()

'''
Sources:
Downey, A. B. (2012, October). How to Think Like a Computer Scientist [PDF].
Holkner, A. (2017, February 21). Pyglet Documentation [PDF].
'''


