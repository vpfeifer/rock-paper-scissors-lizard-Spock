# Testing template for name_to_number()

###################################################
# name_to_number() funtion definition
def name_to_number(name):
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Invalid name : '"+ name +"' passed to name_to_number function. The valid names are rock,paper,scissors,lizard,Spock"

###################################################
# Test calls to name_to_number()
print name_to_number("rock")
print name_to_number("Spock")
print name_to_number("paper")
print name_to_number("lizard")
print name_to_number("scissors")
print name_to_number("error")


###################################################
# Output to the console should have the form:
# 0
# 1
# 2
# 3
# 4
# error