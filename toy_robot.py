# This class performs all the operations of the Toy Robot

class RobotToy:
    X = 0
    Y = 0
    Ori = 'NORTH'

    def place_counter( self, x, y, ori ):
        if (x >= 0 and x <= 4 and y >= 0 and y <= 4):
            self.X = x
            self.Y = y
            self.Ori = ori
        else:
            print("Ensure both co-ordinates are between 0 to 4")

    def change_orientation(self,newMove):
        if newMove == "LEFT":
            if self.Ori == "NORTH":
                self.Ori = "WEST"
            elif self.Ori == "WEST":
                self.Ori = "SOUTH"
            elif self.Ori == "SOUTH":
                self.Ori = "EAST"
            elif self.Ori == "EAST":
                self.Ori = "NORTH"
        else:
            if self.Ori == "NORTH":
                self.Ori = "EAST"
            elif self.Ori == "WEST":
                self.Ori = "NORTH"
            elif self.Ori == "SOUTH":
                self.Ori = "WEST"
            elif self.Ori == "EAST":
                self.Ori = "SOUTH"

    def report_position(self):
        print(self.X, self.Y, self.Ori)

 
    def move(self):
        if self.Ori == "NORTH" and self.Y < 4:
                self.Y = self.Y + 1
        elif self.Ori == "SOUTH" and self.Y > 0:
                self.Y = self.Y - 1
        elif self.Ori == "EAST" and self.X < 4:
                self.X = self.X + 1
        elif self.Ori == "WEST" and self.X > 0:
                self.X = self.X - 1


def main():
    command = "START"
    robo = RobotToy()
    robo.place_counter(0,0,"NORTH")

    while command != "QUIT":
        print('-'*30 )
        command = str(input("Input Command \n 1.PLACE \n 2.MOVE \n 3.LEFT\\RIGHT \n 4.REPORT \n 5.QUIT \n")).strip().upper()
        print('-'*30 )
        if command == "PLACE":
            x_input = int(input("Enter Non-Negative X Coordinate \n"))
            y_input = int(input("Enter Non-Negative Y Coordinate \n"))
            orientation = str(input("Enter Direction of the Toy to be placed \n")).strip().upper()
            robo.place_counter(x_input, y_input, orientation)
            
        if command == "MOVE":
            robo.move()

        if command == "LEFT" or command == "RIGHT":
            robo.change_orientation(command)
            
        if command == "REPORT":
            robo.report_position()
        


if __name__== "__main__":
    main()