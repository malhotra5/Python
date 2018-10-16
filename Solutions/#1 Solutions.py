## This is a general solutions that applies to all the scenarios. But,
## I will run only one scenario.

#Scenario 1

temperature = 25
keyword = "Fahrenheit"


if (keyword == 'Celcius'):
    if(temperature > 35):
        print("WARNING!")
    if(temperature < 20):
        print("WARNING!")

if (keyword == 'Fahrenheit'):
    if(temperature > 95):
        print("WARNING!")
    if(temperature < 68):
        print("WARNING!")
