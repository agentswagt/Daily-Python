import turtle

class AjobTurtle(turtle.Turtle):
    """Ajob turtle is a class for new type of turtle"""
    def forward(self, distance):
        super().backward(distance)
    def backward(self, distance):
        super().forward(distance)
    def left(self, angle):
        print("i won't turn left")
    def right(self, angle):
        super().right(angle)

if __name__ == "__main__":
    montu = AjobTurtle()
    print(type(montu))
    montu.left(30)
    montu.forward(200)

    turtle.done()