# Do not modify these lines
from string import Template
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Greet

def greet(name, template="Hello, <name>!"):
    template.replace("<name>", name)
    print(template.replace("<name>", name))
greet("David")
greet("Doc")
greet("Python")
greet("Bob", "What's up, <name>!")
greet("Peet", "Power to you!: " "<name>")

# Force

def force(mass:float, body="earth"):
    planets_dict = {
    "earth": 9.7,
    "sun": 274,
    "jupiter": 24.9,
    "neptune": 11.1,
    "saturn": 10.4,
    "uranus": 8.8,
    "venus": 8.8,
    "mars": 3.7,
    "mercury": 3.7,
    "moon": 1.6,
    "pluto": 0.5
    }
    earth = mass * planets_dict.get("earth")
    if "earth":
        return earth
    sun = mass * planets_dict.get("sun")
    if "sun":
        return sun

print(force(59736.1, "earth"))
print(force(19891.1, "sun"))


#Pull

m1 = float(input("Enter the first mass: "))
m2 = float(input("Enter the second mass: "))
r = float(input("Enter the distance between the centres of the masses: "))

def pull(m1,m2,r):
    G = 6.674 * 10 ** -11
    f = G * ((m1 * m2) / r ** 2)
    if pull:
        return("the gravitational force is: ", f, "N")


#print("the gravitational force is: ", round(f, 6), "N")
#print(pull(m1, m2, r)))
pull(m1, m2, r)
