# Define the decorator that works with any number of arguments
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to say_hello function
@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Apply the decorator to another function with two parameters
@log_function_call
def add_numbers(a, b):
    print(f"The sum is: {a + b}")

# Call the decorated functions
say_hello("Alice")
add_numbers(10, 20)
