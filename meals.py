def main(): #initialising a main function

    text = input("What time is it? ") #asking user for input
    time = convert(text) #using the convert function to convert the input into a float value

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time") #checking if the time is within the range of meal times
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("no meal time")

def convert(time): #defining a function to convert the time into a float value

    hours, minutes = time.split(":") #splitting the input into hours and minutes

    hours = int(hours)  #converting the hours and minutes into integers
    minutes = int(minutes)

    return hours + (minutes / 60.0) #returning the time as a float value

main() #closing a program