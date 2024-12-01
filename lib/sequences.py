def print_fibonacci(length):
    if length <= 0:
        print("[]")  # Print empty list as string to match the test
        return

    # Start the sequence
    fib_sequence = [0, 1]
    
    # Generate the sequence for length > 2
    for i in range(2, length):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    
    # Print the sequence up to the specified length
    print(fib_sequence[:length])
