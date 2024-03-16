def check_voting_eligibility(age):
    """
    Check if the given age is eligible for voting.

    Args:
        age (int): The age of the user.

    Returns:
        str: A message indicating whether the user is eligible to vote or not.
    """
    if age >= 18:
        return "You are eligible to vote"
    else:
        return "You are not eligible to vote"


def main():
    """
    Main function to execute the program.
    """
    age = int(input("Enter your age: "))
    eligibility_message = check_voting_eligibility(age)
    print(eligibility_message)


if __name__ == "__main__":
    main()
