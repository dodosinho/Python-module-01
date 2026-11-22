class Plant:
	def	__init__(self, name, height, age):
		self.name = name
		self._height = 0.0
		self._age = 0
		if height >= 0:
			self._height = height
		else:
			print(f"{self.name}: Error, height can't be negative")
			print("Height update rejected")
		if age >= 0:
			self._age = age
		else:
			print(f"{self.name}: Error, age can't be negative")
			print("Age update rejected")
		print(f"Plant created: {self.name}: {height:.1f}cm, {age} days old")

	def	get_height(self):
		return self._height

	def	get_age(self):
		return self._age

	def	set_height(self, height):
		if height < 0:
			print(f"{self.name}: Error, height can't be negative")
			print("Height update rejected")
		else:
			self._height = height
			print(f"Height: updated: {height}cm")

	def	set_age(self, age):
		if age < 0:
			print(f"{self.name}: Error, age can't be negative")
			print("Age update rejected")
		else:
			self._age = age
			print(f"Age: updated: {age} days old")

print("=== Garden Security System ===")
rose = Plant("Rose", 15, 10)
print("")
rose.set_height(25)
rose.set_age(30)
print("")
rose.set_height(-1)
rose.set_age(-1)
print("")
print(f"Current state: {rose.name}: {rose.get_height():.1f}cm, {rose.get_age()} days old")
