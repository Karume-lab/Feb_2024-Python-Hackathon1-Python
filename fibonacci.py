def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the specified term n.

    Args:
        n (int): The number of terms to generate in the Fibonacci sequence.

    Returns:
        list: A list containing the first n terms of the Fibonacci sequence.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence


def main():
    """
    Main function to execute the program.
    """
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))

    sequence = fibonacci_sequence(n)

    print("Fibonacci sequence:")
    print(sequence)


if __name__ == "__main__":
    main()
