import unittest 
from toy_robot import RobotToy

class RobotToyTest(unittest.TestCase): 
	
	def setUp(self): 
		self.robo=RobotToy()

	def test_move_North(self):	
		self.robo.X = 2 
		self.robo.Y = 2
		self.robo.Ori = "NORTH"
		new_robo=RobotToy()
		new_robo.place_counter(2,3,"NORTH")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
 
	def test_move_South(self):	
		self.robo.X = 2 
		self.robo.Y = 2
		self.robo.Ori = "SOUTH"
		new_robo=RobotToy()
		new_robo.place_counter(2,1,"SOUTH")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
		
	def test_move_East(self):	
		self.robo.X = 2 
		self.robo.Y = 2
		self.robo.Ori = "EAST"
		new_robo=RobotToy()
		new_robo.place_counter(3,2,"EAST")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
	
	def test_move_West(self):	
		self.robo.X = 2 
		self.robo.Y = 2
		self.robo.Ori = "WEST"
		new_robo=RobotToy()
		new_robo.place_counter(1,2,"WEST")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
		
	def test_move_North_boundry(self):	
		self.robo.X = 2 
		self.robo.Y = 4
		self.robo.Ori = "NORTH"
		new_robo=RobotToy()
		new_robo.place_counter(2,4,"NORTH")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
 
	def test_move_South_boundry(self):	
		self.robo.X = 2 
		self.robo.Y = 0
		self.robo.Ori = "SOUTH"
		new_robo=RobotToy()
		new_robo.place_counter(2,0,"SOUTH")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
		
	def test_move_East_boundry(self):	
		self.robo.X = 4 
		self.robo.Y = 2
		self.robo.Ori = "EAST"
		new_robo=RobotToy()
		new_robo.place_counter(4,2,"EAST")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 
	
	def test_move_West_boundry(self):	
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "WEST"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"WEST")
		self.robo.move()
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori) 	

	def test_change_orientation_Left_for_North(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "NORTH"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"WEST")
		self.robo.change_orientation("LEFT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Right_for_North(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "NORTH"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"EAST")
		self.robo.change_orientation("RIGHT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
			
	def test_change_orientation_Left_for_South(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "SOUTH"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"EAST")
		self.robo.change_orientation("LEFT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Right_for_South(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "SOUTH"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"WEST")
		self.robo.change_orientation("RIGHT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Left_for_East(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "EAST"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"NORTH")
		self.robo.change_orientation("LEFT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Right_for_East(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "EAST"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"SOUTH")
		self.robo.change_orientation("RIGHT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Left_for_West(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "WEST"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"SOUTH")
		self.robo.change_orientation("LEFT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_change_orientation_Right_for_West(self):
		self.robo.X = 0 
		self.robo.Y = 2
		self.robo.Ori = "WEST"
		new_robo=RobotToy()
		new_robo.place_counter(0,2,"NORTH")
		self.robo.change_orientation("RIGHT")
		self.assertEqual(self.robo.X,new_robo.X) 
		self.assertEqual(self.robo.Y,new_robo.Y) 
		self.assertEqual(self.robo.Ori,new_robo.Ori)
	
	def test_place_counter(self):	
		self.robo.place_counter(2,3,"NORTH")
		self.assertEqual(self.robo.X,2) 
		self.assertEqual(self.robo.Y,3) 
		self.assertEqual(self.robo.Ori,"NORTH")

	

if __name__ == '__main__': 
	unittest.main() 
