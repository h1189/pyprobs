'''Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than or equal to 12 points, the function should print: “License suspended”.'''


def speed_check(x):
    demerit_points = int(0)
    if x < 70: 
        print('OK, Normal speed.')
    elif x >= 70:
        print('Crossing Speed limits.')
        demerit_points = ((x-70)//5)
        if demerit_points >= 12:
            print('Licence suspended.')
        return demerit_points

speed = float(input('enter the speed :'))
demerit = speed_check(speed)
print('Demerit points is :',demerit)