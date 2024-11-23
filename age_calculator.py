from datetime import date

def age_calculator (birthdate):
    """
    Calculate the age of a person based on their birthdate.
    
    Args:
    birthdate (datetime.date): The person's birthdate.
    
    Returns:
    int: The age in years.
    """
    today = date.today()
    age = today.year - birthdate.year
    
    # Adjust age if the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

def main():
    try:
        # Input birthdate from the user
        birth_year = int(input("Enter your birth year (YYYY): "))
        birth_month = int(input("Enter your birth month (MM): "))
        birth_day = int(input("Enter your birth day (DD): "))
        
        # Create a date object for the birthdate
        birthdate = date(birth_year, birth_month, birth_day)
        
        # Calculate and display the age
        age = age_calculator (birthdate)
        print(f"You are {age} years old.")
    
    except ValueError:
        print("Invalid date. Please enter numeric values in the correct format.")

if __name__ == "__main__":
    main()
