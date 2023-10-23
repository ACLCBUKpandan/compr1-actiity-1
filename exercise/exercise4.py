"""
"Generate a Python script that allows users to convert 
temperatures from Celsius to either Fahrenheit or Kelvin,
depending on their choice."

Formula:
Kelvin = celsius + 273.15
Fahrenheit = (celsius * 9/5) + 32

Note:
For the operation variable 
"F" - for fahrenheit
"K" - for Kelvin


- The user must type "F" or "K"


Bonus:
If the user inputs anything other than "F" or "K," return "error."



"""


# Do not modify
def convert_temperature(operation, celsius):
    # start coding here

    print(operation)
    print(celsius)

    result  = 0

    return result # Do not modify



# The program starts here
if __name__ == '__main__':
    print(convert_temperature("F",32)) # 89.6
    print(convert_temperature("K",32)) # 305.15


    user_input = input("Convert to Celsius to: (K or F)")
    temperature = float(input("What is the temperature: "))
    results = convert_temperature(user_input, temperature)
    print(f"{results}")





