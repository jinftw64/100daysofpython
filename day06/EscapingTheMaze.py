# 100 Days of Code
# Day 6

# Follow along right edge of maze
# 1. Turn right
# 2. Go straight if can't go right
# 3. Turn left as last resort.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        while not front_is_clear():
            turn_left()
        move()
