# Validate
def get_age_validated():
    """Check if input is valid before converting"""
    age_input = input("Enter your age: ")

    # Validate first
    if age_input.isdigit():
        age = int(age_input)
        if 0 < age < 150:
            return age
        else:
            print("Age must be between 1 and 149")
            return None
    else:
        print("Please enter a number")
        return None

age = get_age_validated()

# Handle

def get_age_exception():
    """Try to convert, handle errors if they occur"""
    try:
        age_input = input("Enter your age: ")
        age = int(age_input)

        if not 0 < age < 150:
            raise ValueError("Age must be between 1 and 149")

        return age

    except ValueError as e:
        print(f"Invalid age: {e}")
        return None

age = get_age_exception()
