# function that calculates how many atoms are in n grams of an element
def num_atoms(grams, AW = 196.97):
    mole = grams/AW
    return mole * 6.022E23


print (num_atoms(10))
print (num_atoms(10,12.001))
print (num_atoms(10,1.008))