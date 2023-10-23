"""
Create a simple calculator in python.

The app will ask the user the operator,
the first and second operand,
then performs the operation.


Note:
- The user will type  + , - , *, / for the operator


Bonus:

- If the user inputs anything other than +, -, *, / return "error."





"""


# Do not modify
def calculator(operator, first_num, second_num):
    # Start coding here

    print(f"Operator: {operator}")
    print(f"First Operand: {first_num}")
    print(f"Second Operand: {second_num}")

    results = 0


    return results # do not modify


# The program starts here
if __name__ == "__main__":

    print("Simple Calculator")

    operator = input("What is the operator? (+, - , *, / )")
    first_num = input("First Num: ")
    second_num = input("Second Num: ")


    print(f"Results: {calculator(operator, first_num, second_num)}")





    