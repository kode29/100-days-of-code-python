def move():
    print("Hello")

def turn_left():
    print("hello")

def wall_in_front():
    print("hello")

def at_goal():
    print("hello")

def wall_on_right():
    print("hello")


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left():
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()