import sys
from replit import clear


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


operator = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide,
    '%': modulo
}

user_input = input('''
   .----------------.  .----------------.  .----------------.  .----------------. 
  | .--------------. || .--------------. || .--------------. || .--------------. |
  | |     ______   | || |      __      | || |   _____      | || |     ______   | |
  | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
  | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
  | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
  | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
  | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
  | |              | || |              | || |              | || |              | |
  | '--------------' || '--------------' || '--------------' || '--------------' |
   '----------------'  '----------------'  '----------------'  '----------------' 
                   _____________________
                  |  _________________  |                                                           
                  | |              0. | |
                  | |_________________| |
                  |  ___ ___ ___   ___  |   Enter  "C"      --> To clear the calc
                  | | 7 | 8 | 9 | | + | |   Enter  "E"      --> Turn off 
                  | |___|___|___| |___| |   
                  | | 4 | 5 | 6 | | - | |      
                  | |___|___|___| |___| |                                                           
                  | | 1 | 2 | 3 | | x | |                                                                 
                  | |___|___|___| |___| |                                                             
                  | | . | 0 | = | | / | |                                                          
                  | |___|___|___| |___| |                                                          
                  |_____________________|   To start the calc enter --> "ON" : ''').lower()


def Turn_off():
    return sys.exit("""
                   _____________________
                  |  _________________  |
                  | |   Terminal OFF  | |
                  | |_________________| |
                  |  ___ ___ ___   ___  |
                  | | 7 | 8 | 9 | | + | |
                  | |___|___|___| |___| |
                  | | 4 | 5 | 6 | | - | |
                  | |___|___|___| |___| |
                  | | 1 | 2 | 3 | | x | |
                  | |___|___|___| |___| |
                  | | . | 0 | = | | / | |
                  | |___|___|___| |___| |
                  |_____________________| """)


if user_input == 'on':
    def calculator():
        def user_checking(check):
            if check == 'c':
                clear()
                calculator()
            elif check == 'e':
                Turn_off()

        num1 = input('first number : '.title())
        user_checking(check=num1)
        num1 = float(num1)

        for symbol in operator:
            print(symbol)

        user_symbol = input('enter the operator : ')
        user_checking(check=user_symbol)

        Run = True
        while Run:
            num2 = input('enter the another number : ')
            user_checking(check=num2)
            num2 = float(num2)

            function = operator[user_symbol]
            answer = function(num1, num2)
            num1 = answer

            user_symbol = input(f"""
                   _____________________
                  | ___________________ |
                  ||{num1}{user_symbol}{num2} = {answer}   
                  ||___________________||
                  |  ___ ___ ___   ___  |
                  | | 7 | 8 | 9 | | + | |           
                  | |___|___|___| |___| |     
                  | | 4 | 5 | 6 | | - | |
                  | |___|___|___| |___| |
                  | | 1 | 2 | 3 | | x | |   ENTER the Operator   +
                  | |___|___|___| |___| |                        -
                  | | . | 0 | = | | / | |                        *
                  | |___|___|___| |___| |                        /
                  |_____________________|                        %   : """)

            user_checking(check=user_symbol)


    calculator()
else:
    Turn_off()
