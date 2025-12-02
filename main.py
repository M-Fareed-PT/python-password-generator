import string
import random

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    charset = ""

    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    if not charset:
        return None

    password = ''.join(random.choice(charset) for _ in range(length))
    return password


def menu():
    print("\n====== PYTHON PASSWORD GENERATOR ======")
    print("1. Generate Password")
    print("2. Exit")
    print("=======================================")


def generator_flow():
    print("\n--- PASSWORD GENERATION MODE ---")

    try:
        length = int(input("Enter password length (e.g. 12): "))
    except ValueError:
        print("\nInvalid length. Must be a number.")
        return

    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    )

    if password is None:
        print("\nError: You must select at least one character type!")
    else:
        print("\nGenerated Password:")
        print(password)

    input("\nPress Enter to return to menu...")


def main():
    while True:
        menu()
        choice = input("Select option (1-2): ").strip()

        if choice == "1":
            generator_flow()

        elif choice == "2":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid selection. Try again.")


if __name__ == "__main__":
    main()
