
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.
def number_attributes(**kwargs):
    count = 0
    for key in kwargs:
        count += 1
        # first time through: count = 0 + 1 = 1
        # second time through: count = 1 + 1 = 2
        # third time through: count = 2 + 1 = 3
    return count    
print(number_attributes(height=180, weight=75, age=30)) # Should return 3   








# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.
def list_attributes(**kwargs):
    values_list = []
    for value in kwargs.values():
        values_list.append(value)
    return values_list
print(list_attributes(hobby="painting", city="New York", profession="engineer"))
# Should return ["painting", "New York", "engineer"]










# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:

# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black
