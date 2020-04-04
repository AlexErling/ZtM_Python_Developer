# error that crashes the program is an exception
# exceptions can cost companies millions
# need error handling

# ERRORS
# https://docs.python.org/3/library/exceptions.html
# TYPE ERRORS
# SYNTAX ERRORS
# NAME ERRORS
# INDEX ERRORS
# KEY ERROR
# ZER0 DIVISION
while True:
    try:
        age = int(input('what is your age: '))
        10 / age
        print(age)
        #raise Exception('Hey cut it out')  # If you want to break out of the program0
    except ValueError:
        print("Invalid input. Please enter a valid number")
        continue  # goes back to the top
    except ZeroDivisionError:
        print("Enter a number besides 0.")
        break
    else:  # else only runs after try is successful
        print("Thank you")
        break  # won't get to bottom line if this is here
    finally:  # finally runs regardless of everything (after succes of failure)
        print('Ok, i am finally done')
    print('Can you hear me')

# Raise exceptions when necessary
# Accepting inputs can raise the most errors

# can build try directly into function


# def sum(num1, num2):
#     try:
#         return num1 / num2
#     except (TypeError, ZeroDivisionError) as err:
#         # Err is an error object
#         # Need to be descriptive
#         print(err)
#
#
# # We can throw on our error
#
# print(sum(2, 0))
