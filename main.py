from generator.generator_fibonacci import generator_fibonacci


if __name__ == "__main__":
    
    first_n_element = 20
    # user_input = None
    user_input = input("please Enter a number to get the first N elements in fibonacci serie (if not entered max first 20 will be generated):")
    try:  
        first_n_element = int(user_input)
        print("User Input:", first_n_element)
    except:
        print(f"ERROR: user input '{user_input}' is not integer... set to default (20).")
        print("Default Value:", first_n_element)

    for i, element in enumerate(generator_fibonacci(first_n_element)):
        print(f"Fibonacci Element-{i+1}: {element}")
