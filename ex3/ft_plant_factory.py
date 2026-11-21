class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old")

plants = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Forn", 15, 120)
]

print("=== Plant Factory Output ===")

for plant in plants:
    plant.show()