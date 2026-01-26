# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.
list_numbers = [10, 25, -3, 42, 7]

def all_positives(list_numbers):
    for num in list_numbers:
        if num < 0:
            return False
    return True
all_positives(list_numbers)
    





# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

def sum_less(nums): s = 0 for n in nums: if 0 < n < 1000: s += n return s numbers = [1, 500, -3, 1200, 20]




# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.
def count_even(numbers): count = 0 for n in numbers: if n % 2 == 0: count += 1 return count numbers = [1, 2, 4, 7, 10, 13