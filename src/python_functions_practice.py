def return_10(): #no argument passed in to brackets so no value needed
    return 10

def add (first_number, second_number):
    sum_of_numbers = first_number + second_number
    return first_number + second_number

def subtract (first_number, second_number):
    sum_of_numbers = first_number - second_number
    return first_number - second_number

def multiply (first_number, second_number):
    sum_of_numbers = first_number * second_number
    return first_number * second_number

def divide (first_number, second_number):
    sum_of_numbers = first_number / second_number
    return first_number / second_number

def length_of_string (test_string):
    string_length_calc = len(test_string) #need to create the variable test_string
    return string_length_calc
    
def join_string (string_1, string_2):
    total_string = string_1 + string_2
    
    return total_string

# print(join_string("Mary had a little lamb, ", "its fleece was white as snow"))

def add_string_as_number(first_string, second_string):
    total = int(first_string) + int(second_string)

    return total 



def number_to_full_month_name(month_number):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    return month_names[month_number - 1]

def number_to_short_month_name(number):
    list_of_short_months = ["a","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    number_to_short_month_name=list_of_short_months[int(number)]
    return number_to_short_month_name