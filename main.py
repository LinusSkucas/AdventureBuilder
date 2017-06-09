def road2():
	print("On road 2")

class section():
    "A section of the text based game"
    def __init__(self, name, description,getable, useable, directions):
        self.name = name
        self.longName = description
        self.getable = list(getable)
        self.useable = list(useable)
        self.directions = dict(directions)

    def look(self):
        return self.longName

road = section("Road", "Long road", getable=["shovel", "hoe"], useable=["stuff"], directions={"w": road2})
print(road.look)
