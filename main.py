class section():
	"A section of the text based game"
	def __init__(self, name, description, getable, useable, directions):
		self.name = name
		self.longName = description
		self.getable = dict(getable)
		self.useable = dict(useable)
		self.directions = dict(directions)

	def name(self):
		print(self.name)
	
	def look(self):
		print(self.name)
		print(self.longName)
		
	def drop(self, tool):
		if tool not in self.useable.keys():
			print("You Can't use that.")
		else:
			#print("Using {}..." % tool)
			toolfunc = self.useable[tool]
			toolfunc()
			
	def get(self, tool):
		if tool not in self.getable.keys():
			print("You Can't get that.")
		else:
			#print("Getting {}..." % tool)
			toolfunc = self.getable[tool]
			toolfunc()
			
			
	def move(self, wanted):
		if wanted not in self.directions.keys():
			print("You Can't move there..")
		else:
			#print("Getting {}..." % tool)
			#wanted.name()
			print("moved "+wanted)
			
class cursor():
	"This class does nothing. Maybe one day it will auto. create childs"
	pass
		

class cursorBag(cursor):
	def __init__(self, bag):
		self.bag = list(bag)
		
	def addBag(self, useObj):
		self.bag.append(useObj)
	
	def delBag(self, useObj):
		self.bag.remove(useObj)
		
	def lookBag(self):
		return self.bag
		
	def inBag(self, useObj):
		if useObj in self.bag:
			return True
		else:
			return False
			
class cursorPoints(cursor):
	def __init__(self,points):
		self.points = int(points)
		
	def addPoints(self, Points):
		self.points = self.points + Points
	
	def delPoints(self, Points):
		self.points = self.points - Points
		
	def setPoints(self, Points):
		self.points = Points
		
	def lookPoints(self):
		return self.points
		
class cursorPlayer(cursor):
	def __init__(self, startSection):
		self.section = startSection
		
	def __repr__(self):
		#print("Getting")
		return self.section
		
	def player(self, moveSection):
		#print("Setting")
		self.section = moveSection

############ THE FOLLOWING CODE IS FOR TESTING ########################

def roada():
	print("On road 2")
	
def getshovel():
	print("got shovel")
	

def usestuff():
	print("Used stuff")

#### sections testing


road = section("Road", "Long road", getable={"shovel":getshovel}, useable={"junk":usestuff}, directions={"w": roada})
road2 = section("Path", "Long path", getable={"shovel":getshovel}, useable={"junk":usestuff}, directions={"e": road})
road.look()
road.drop("junk")
road.get("shovel")
road.move("w")

##### cursor testing

bag = []
points = 0

cursorBag = cursorBag(bag)
cursorBag.addBag("Junk")
cursorBag.addBag("Fat Cat")
cursorBag.addBag("nothing")
cursorBag.delBag("Junk")
print(cursorBag.lookBag())
print(cursorBag.inBag("Fat Cat"))

cursorPlayer = cursorPlayer(road)
print(cursorPlayer)


