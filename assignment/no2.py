# function that calculates your equivalent weight on another planet
def calc_weight_on_planet(earth, planetG=23.1):
    mass = earth/9.8
    return mass*planetG

print(calc_weight_on_planet(120,9.8))
print(calc_weight_on_planet(120))
print(calc_weight_on_planet(120,23.1))


