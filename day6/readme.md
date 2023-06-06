
<!-- 👇👇👇follow this link👇👇👇 -->

<!-- https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json -->
<!-- ☝️☝️☝️follow this link☝️☝️☝️ -->

<!-- hurdle1 challenge -->
def dest():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
def right():
    turn_left()
    turn_left()
    turn_left()
   
for step in range(6):
    dest()
    

<!-- hurdle2 challenge -->
def dest():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
def right():
    turn_left()
    turn_left()
    turn_left()
   

while at_goal() != True:
    dest()


<!-- hurdle3 challenge -->
def dest():
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()
    
def right():
    turn_left()
    turn_left()
    turn_left()
   
while  at_goal() != True:
    if  wall_in_front():
        dest()
    else:
        move()
    

<!-- hurdel4 challenge -->
def dest():
    turn_left()
    while wall_on_right():
        move()    
    right()
    move()
    right()
    while front_is_clear():
        move()
    turn_left()
    
def right():
    turn_left()
    turn_left()
    turn_left()
   
while  at_goal() != True:
    if  wall_in_front():
        dest()
    else:
        move()
    
<!-- maze challenge -->
def right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    

while at_goal() != True:
    if right_is_clear():
        right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
   
