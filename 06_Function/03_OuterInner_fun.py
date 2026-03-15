def outer_function():
    x = 1 # Variables in the outer function

    def inner_function():
        y = 2 # Variables in the inner function
        result = x + y # Accessing variable from outer function
        return result
    
    return inner_function() # Calling the inner function

final_result = outer_function() # Calling the outer function# Calling the outer function
print("Final Result:", final_result)