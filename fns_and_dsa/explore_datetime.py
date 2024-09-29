from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    # Formatting date as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    try:
        # Prompting user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculating the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Formatting future date as YYYY-MM-DD
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Display the current date and time
    current_date = display_current_datetime()
    # Calculate and display the future date
    calculate_future_date(current_date)
