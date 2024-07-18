#Calculating Time in HH:MM:SS format whwn a user give seconds in input

Time = int(input("Enter time in second = "))
if(Time < 0):
    print("enter positive number")
elif(Time < 3600):
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{min} minutes: {sec} second")
else:
    Hour = Time//3600
    sec1 = Time%3600
    min = sec1//60
    sec = sec1%60
    print(f"{Hour} Hour: {min} min: {sec} seconds")
print("Conversion Sucessful")

# UNDERSTANDING ELIF USING A PROBLEM - CALCULATING PROFIT AND LOSS BASED ON COST AND SELLING PRICE.
cp = int(input("Enter cost price (in rs) - "))
sp = int(input("Enter selling price (on rs) - "))
if(cp < 0):
    print(" Inavlid cost price ")
elif(sp < 0):
    print(" Inavlid selling price ")
else:
    if(sp > cp):
        print("Profit: Rs" , (sp-cp))
    elif(sp > cp):
        print("Loss: Rs" , (cp-sp))
    else:
        print(" No profit no loss ")