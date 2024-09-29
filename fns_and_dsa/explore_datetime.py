from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date():
    now = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = now + timedelta(days = number_of_days)
    print("Current date and time: ", future_date.strftime("%Y-%m-%d"))
def main():
    display_current_datetime()
    calculate_future_date()
if __name__ == "__main__":
    main()