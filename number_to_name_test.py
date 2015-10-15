# Testing template for number_to_name()

###################################################
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "The argument 'number' must be in 0 to 4 range!"



###################################################
# Test calls to number_to_name()
print number_to_name(0)
print number_to_name(1)
print number_to_name(2)
print number_to_name(3)
print number_to_name(4)
print number_to_name(5)


###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors
# error