def function_with_uncommon_error(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 5
    except ZeroDivisionError:
        return "Cannot divide by zero"

result = function_with_uncommon_error(0) # Returns "Cannot divide by zero"
result2 = function_with_uncommon_error(5) # Returns 10