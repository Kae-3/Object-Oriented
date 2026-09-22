class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a", Parrot.species)
print("Woo is also a", Parrot.species)

print(f"{blu.name} is {blu.age} years old.")
print(f"{woo.name} is {woo.age} years old.")

class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing!"


blu = Parrot("Blu", 10)

print("Species:", Parrot.species)
print("Name:", blu.name)
print("Age:", blu.age)

print(blu.sing("'Happy'"))
print(blu.dance())