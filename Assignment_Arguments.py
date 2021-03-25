# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Greet
def greet(name='', what=""):
    greet_no_space=(f'Hello, {name}' + "!" )
    what=(f'What\'s up, {name}' + "!")
    if name == 'Doc':
        print(greet_no_space)
    if name == 'Bob':
        print(what)
greet('Doc')
greet('Bob', "What's up, {name}!")

# Force

dict_planets = {"earth": 9.7, "sun": 274, "jupiter": 24.9, "neptune": 11.1, "saturn": 10.4,
                "uranus": 8.8, "venus": 8.8, "mars": 3.7, "mercury": 3.7, "moon": 1.6, "pluto": 0.5}
mass = {"earth": 59736, "sun": 19891, "jupiter": 18986, "neptune": 10243, "saturn": 56846,
        "uranus": 86810, "venus": 48685, "mars": 64185, "mercury": 33022, "moon": 7349, "pluto": 125}
body = ("earth", "sun", "jupiter", "neptune", "saturn", "uranus", "venus", "mars", "mercury", "moon", "pluto")

#to the power of = ttpo
earth_ttpo = 10**24
times_mass_earth = earth_ttpo * mass["earth"]
final_outcome = times_mass_earth * dict_planets["earth"]
sun_ttpo = 10**30
times_mass_sun = sun_ttpo * mass["sun"]
final_outcome1 = times_mass_sun * dict_planets["sun"]
jupiter_ttpo = 10**27
times_mass_jupiter = jupiter_ttpo * mass["jupiter"]
final_outcome2 = times_mass_jupiter * dict_planets["jupiter"]
neptune_ttpo = 10**30
times_mass_neptune = neptune_ttpo * mass["neptune"]
final_outcome3 = times_mass_neptune * dict_planets["neptune"]
saturn_ttpo = 10**26
times_mass_saturn = saturn_ttpo * mass["saturn"]
final_outcome4 = times_mass_saturn * dict_planets["saturn"]
uranus_ttpo = 10**25
times_mass_uranus = uranus_ttpo * mass["uranus"]
final_outcome5 = times_mass_uranus * dict_planets["uranus"]
venus_ttpo = 10**24
times_mass_venus = venus_ttpo * mass["venus"]
final_outcome6 = times_mass_venus * dict_planets["venus"]
mars_ttpo = 10**23
times_mass_mars = mars_ttpo * mass["mars"]
final_outcome7 = times_mass_mars * dict_planets["mars"]
mercury_ttpo = 10**23
times_mass_mercury = mercury_ttpo * mass["mercury"]
final_outcome8 = times_mass_mercury * dict_planets["mercury"]
moon_ttpo = 10**22
times_mass_moon = moon_ttpo * mass["moon"]
final_outcome9 = times_mass_moon * dict_planets["moon"]
pluto_ttpo = 10**22
times_mass_pluto = pluto_ttpo * mass["pluto"]
final_outcome10 = times_mass_pluto * dict_planets["pluto"]

def force(mass=(float), body="earth"):
    if mass == 59736 and body == "earth":
        print(final_outcome)
    if mass == 19891 and body == "sun":
        print(final_outcome1)
    if mass == 18986 and body == "jupiter":
        print(final_outcome2)
    if mass == 10243 and body == "neptune":
        print(final_outcome3)
    if mass == 56846 and body == "saturn":
        print(final_outcome4)
    if mass == 186810 and body == "uranus":
        print(final_outcome5)
    if mass == 48685 and body == "venus":
        print(final_outcome6)
    if mass == 64185 and body == "mars":
        print(final_outcome7)
    if mass == 33022 and body == "mercury":
        print(final_outcome8)
    if mass == 7349 and body == "moon":
        print(final_outcome9)
    if mass == 125 and body == "pluto":
        print(final_outcome10)
force(59736, "earth")
force(19891, "sun")
force(7349, "moon")
#enzo


#Two Cars
#Apple (earth mass = 5.972e+24 (5972190000000000000000000) and distance = 6371000)
m1 = float(input("Enter the first mass: "))
m2 = float(input("Enter the second mass: "))
r = float(input("Enter the distance between the centres of the masses: "))
G = 6.674*(10**-11)
f = (G*m1*m2)/(r**2)
print("the gravitational force is: ", round(f, 6), "N")


