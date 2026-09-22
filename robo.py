class Robot:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def introduce(self):
        print(f"Hello! I am {self.name}.")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


# Creating an object of Robot class
my_robot = Robot("RoboMax", "v2.0", "Silver")

# Calling the introduction method
my_robot.introduce()