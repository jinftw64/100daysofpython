# 100 Days of Code
# Day 6

# Follow along right edge of maze
# 1. Turn right
# 2. Go straight if can't go right
# 3. Turn left as last resortself.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_right():
    turn_right()
    move()

while not at_goal():
    while not right_is_clear():
        turn_right()
    turn_right()
    if front_is_clear():
        move()
    else:
        pass
