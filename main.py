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

	def look(self):
		print(self.longName)
		
	def drop(self, tool):
		if tool not in self.useable.keys():
			print("You Can't use that.")
		else:
			#print("Using {}..." % tool)
			toolfunc = self.useable[tool]
			toolfunc()
				

road = section("Road", "Long road", getable={"shovel":getshovel}, useable={"stuff":usestuff}, directions={"w": road2})
road.look()
road.drop("junk")
