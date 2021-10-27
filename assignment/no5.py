def convert_temp():
    temp = int(input("temp in F:" ))
    return temp 

def convert_to_celcius(temp):
    cel = (5/9)* (temp -32)
    return cel

def convert_to_kelvin(cel):
    kel = cel +273.15
    return kel 


temp = convert_temp()
cel = convert_to_celcius(temp)
print("the temperature in farenheit is ", temp)
print("the temperature in celcius is", cel )
print("the temperature in kelvin is", convert_to_kelvin(cel))

