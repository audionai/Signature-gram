from turtle import Turtle , Screen
import random
random = random.Random()
screen = Screen()
screen.setup(width=900, height=450)
screen.bgcolor("black")
screen.title("Game")

mk = Turtle()
walls = []
mk.penup()
mk.shape("square")
mk.color("pink")
mk.goto(-420,-180)
game = True

# Create walls
def create_wall(x, y, w, h, color="blue"):
    wall = Turtle()
    wall.penup()
    wall.goto(x, y)
    wall.shape("square")
    wall.color(color)
    wall.shapesize(stretch_wid=h, stretch_len=w)
    walls.append(wall)
create_wall(-290, 225, 80, 1)  # Top wall
create_wall(-440, 200, 1, 45)  # Left wall
create_wall(-290, -200, 80, 1)  # Bottom wall
create_wall(420, 200, 1, 40)  # Right wall


po = [(-360, 30), (-300, 30), (-240, 30), (-180, 30), (-120, 30), (-60, 30),
      (0, 30), (60, 30), (120, 30), (180, 30), (240, 30), (300, 30), (360, 30)]
pop = [(-360, 170), (-300, -115), (-180, 170), (-60, 170), (240, -115), (300, 170),
       (360, 170), (430, -115),(500,170),(600,-115),(700,170),(720,-115)]
pmpmpm = []
for _ in range(0,18):
    x = random.randint(-200,600)
    y = -170
    num = (x,y)
    pmpmpm.append(num)
    print(pmpmpm)
    # _ = ()
# Create vertical barriers
for q in pmpmpm:
    create_wall(q[0] + 30, q[1], 2, 1)


while game:
    def add():
        for wall in walls:
            y = wall.xcor()
            if y > -450:
                y -= 20
                wall.goto(y, wall.ycor())
    def score():
        pass
    def gameover() -> bool:
        mk.goto(0,0)
        mk.write("Game Over", move=True, align="center", font=("Arial", 72, "normal"))
        return False
    def check_collision():
        for wall in walls:
            print(wall)
            if mk.distance(wall) < 25:
                game = gameover()
                return
    def move_up():
        y = mk.ycor()
        # x = mk.xcor()
        if y < 195:
            y += 20
            # x += 20
            mk.goto(mk.xcor(), y)
            # mk.goto(x, mk.ycor())
            y -= 20
            # x -= 20
            mk.goto(mk.xcor(), y)
            # mk.goto(x, mk.ycor())
            check_collision()
    def move_down():
        y = mk.ycor()
        if y > -170:
            y -= 20
            mk.goto(mk.xcor(), y)
            check_collision()
    # def move_up():
    #     y = mk.ycor()
    #     if y < 200:
    #         y += 20
    #         mk.goto(mk.xcor(), y)
    #         print("ji")
    def move_left():
        y = mk.xcor()
        if y > -420:
            y -= 20
            mk.goto(y, mk.ycor())
            check_collision()
        y = mk.xcor()
    def move_right():
        y = mk.xcor()
        if y < 420:
            if mk.xcor() >= -420 and mk.xcor() < -200:
                print("high")
                y += 20
            elif mk.xcor() >= -200 and mk.xcor() < 0:
                y+= 10
                print("low")
            elif mk.xcor() == 0:
                print("high")
                y += 1
            else:
                y+= 5
                print("low")
            mk.goto(y,mk.ycor())
            add()
            check_collision()







            score()


    screen.listen()
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.mainloop()