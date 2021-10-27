def convert_to_days(): 
    h=float(input("hours"))
    m=float(input("minutes"))
    s=float(input("seconds"))
    return h,m,s

def getDays(h,m,s):
    h = h/24
    m = m/1440
    s = s/86400
    return round(h+m+s,4)

h,m,s = convert_to_days()

print("the number of days is: ", getDays(h,m,s))

