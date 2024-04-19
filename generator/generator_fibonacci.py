def generator_fibonacci(first_n_in_serie=None):
    if first_n_in_serie == None:
        # return infinite number of  fibonnaci serie elements 
        total = None
    else: 
        total = first_n_in_serie

    counter = 1
    n1 = None
    n2 = None
    while total == None or counter <= total:
        if counter == 1:
            n1 = counter
            yield n1
        elif counter == 2:
            n2 = counter
            yield n2
        else:
            tm = n2
            n2 = n2 + n1
            n1 = n2
            yield n2
        counter += 1

