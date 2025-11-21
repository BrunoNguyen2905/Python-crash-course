class Character:
    def __init__(self, name, level, health, damage, speed):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.speed = speed

    def greet(self):
        return f"Hello, I am {self.name}, at level {self.level}. My health is {self.health}, damage is {self.damage}, and speed is {self.speed}."

    def double_damage(self):
        self.damage *= 2
        return self.damage

    def attack(self, other_character: Character):
        other_character.health -= self.damage
        return f"{self.name} attacked {other_character.name} for {self.damage} damage!"


# class is the blueprint for creating instances (objects)
# unique instances
warrior = Character("Aragorn", level=10, health=100, damage=15, speed=7)
mage = Character("Gandalf", level=20, health=80, damage=25, speed=5)
print(warrior.greet())  # call the method on the instance without any parameters
# print(Character.greet(warrior)) # alternative way to call the method with class name and put the instance as parameter
print(mage.greet())
warrior.double_damage()
print(f"{warrior.name}'s double damage is: {warrior.damage}")
warrior_attack = warrior.attack(mage)
print(warrior_attack)
print(f"{mage.name}'s health after attack: {mage.health}")
mage_attack = mage.attack(warrior)
print(mage_attack)
print(f"{warrior.name}'s health after attack: {warrior.health}")
