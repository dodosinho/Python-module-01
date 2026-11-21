class	Plant:
	def	__init__(self, name, height, age, growth):
		self.name = name
		self.height = height
		self.age = age
		self.growth = growth


	def	show(self):
		print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

	def	grow(self):
		self.height += self.growth

	def	day(self):
		self.age += 1

rose = Plant("Rose", 25, 30, 0.8)
print("=== Garden Plant Growth ===")
i = 0
j = rose.height
while i < 7:
	if i == 0:
		rose.show()
		i += 1
	else:
		rose.grow()
		rose.day()
		rose.show()
		i += 1
	print(f"=== Day {i} ===")
rose.grow()
rose.day()
rose.show()
print(f"Growth this week: {rose.height - j:.1f}cm")