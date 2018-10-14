## Tutorial 1


## Creating Variables. These store values such as numbers or sentences

string = 'This sentence is also known as string'
number = 390

## Using print

# You can print numbers or strings
print(34)
print("I am printing a sentence")

# You can print variables
print(string)
print(number)


## Using IF commands (have to use == operator)

# For if commands, you can compare any variable to any number of string
if (number == 34):
    print("The number is the same")

if (number == string):
    print("The string and then number are the same")

if (string == "This sentence is also known as string"):
    print("The string is the same")

# Note that the if command will only work if the statement being compared is true

## Nested IF commands (multiple if commands at once. Pay attention to the spacing)

if (number == 390):
    if (string == 'This sentence is also known as string'):
        print("This will only print if both the statements above are true")
    print("This will only print if the first if statement is true")

print("This will print even if the if statements aren't true")
