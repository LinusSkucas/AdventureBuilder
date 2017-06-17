def road2():
	print("On road 2")
	
def getshovel():
	print("got shovel")

def usestuff():
	print("Used stuff")

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
	def __init__(self, bag, startSection, points):
		self.bag = list(bag)
		self.section = startSection
		self.points = int(points)
		
	def addBag(self, useObj):
		self.bag.append(useObj)
	
	def delBag(self, useObj):
		self.bag.remove(useObj)
		
	def lookBag():
		return self.Bag
		
	def inBag(self, useObj):
		if useObj in self.Bag:
			return True
		else:
			return False
		
	def addPoints(self, Points):
		self.points = self.points + Points
	
	def delPoints(self, Points):
		self.points = self.points - Points
		
	def setPoints(self, Points):
		self.points = Points
		
	def lookPoints(self):
		return self.points
		
road = section("Road", "Long road", getable={"shovel":getshovel}, useable={"junk":usestuff}, directions={"w": road2})
road.look()
road.drop("junk")
road.get("shovel")
road.move("w")
