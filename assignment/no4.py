# function that returns the hirght to preserve aspect ratio 
def calc_new_height():
    width = int(input("width:"))
    height = int(input("height:"))
    new_width =int(input("new width:"))

    # calculate new height
    new_height = height/width * new_width
    return new_height
    
print("the corresponding height is:", calc_new_height())