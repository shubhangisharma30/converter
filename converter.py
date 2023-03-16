#Unit Converter 
num1 = input("Enter the value: ")

unit1 = input("Enter the unit 1: ")
unit2 = input ("Enter the value to which we need to convert to: ")

#m to cm 
if unit1 == "m" and unit2 == "cm":
    ans= float(num1)*100
    print(ans)

#cm to m
elif unit1 == "cm" and unit2 == "m":
    ans= float(num1)/100
    print(ans)

#mm to cm
elif unit1 == "mm" and unit2 == "cm":
    ans= float(num1)/10
    print(ans)

#cm to mm
elif unit1 == "mm" and unit2 == "cm":
    ans= float(num1)*10
    print(ans)

#mm to m 
elif unit1 == "mm" and unit2 == "m":
    ans= float(num1)/1000
    print(ans)

#m to mm
elif unit1 == "m" and unit2 == "mm":
    ans= float(num1)*1000
    print(ans)

#km to m
elif unit1 == "km" and unit2 == "m":
    ans= float(num1)*1000
    print(ans)

#km to mm
elif unit1 == "km" and unit2 == "mm":
    ans= float(num1)*1000000
    print(ans)

#m to km
elif unit1 == "m" and unit2 == "km":
    ans= float(num1)/1000
    print(ans)

#mm to km
elif unit1 == "mm" and unit2 == "km":
    ans= float(num1)/1000000
    print(ans)

#ft to cm 
elif unit1 == "ft" and unit2 == "cm":
    ans= float(num1)*30.48
    print(ans)

#ft to mm
elif unit1 == "ft" and unit2 == "mm":
    ans= float(num1)*304.8
    print(ans)

#ft to inch 
elif unit1 == "ft" and unit2 == "inch":
    ans= float(num1)*12
    print(ans)

#inch to cm
elif unit1 =="inch" and unit2=="cm":
    ans = float(num1)*2.54
    print(ans)

#inch to mm
elif unit1 =="inch" and unit2=="mm":
    ans = float(num1)*25.4
    print(ans)

#cm to inch 
elif unit1 =="cm" and unit2=="inch":
    ans = float(num1)/2.54
    print(ans)

