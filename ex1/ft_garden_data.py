class	Plant:
	def	__init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age

	def	show(self):
		print(f"{self.name}: {self.height}cm, {self.age} days old")

rose = Plant("Rose", 25, 30)
oaks = Plant("Oaks", 200, 365)
cactus = Plant("Cactus", 15, 90)

print("=== Garden Plant Registry ===")
rose.show()
oaks.show()
cactus.show()