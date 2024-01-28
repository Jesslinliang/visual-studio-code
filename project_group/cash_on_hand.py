from pathlib import Path
import csv

# Define a function to be used as a key for sorting by the second element of a tuple
def sort_by_second_element(item):
    return item[1]

# Define the main function for processing cash data
def cash_function():
    # specific absolute paths for input and output files
    file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_hand.csv")
    file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

    # Read the csv file to append profit and quantity from the csv.
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        cash_on_hand = []  # Store the data read from the csv file

        for row in reader:
            cash_on_hand.append([int(row[0]), float(row[1])])

    # Initialize an empty string to store the output message
    output =""

    # Check if cash-on-hand is always increasing or decreasing
    increasing = all(cash_on_hand[i][1] <= cash_on_hand[i + 1][1] for i in range(len(cash_on_hand) - 1))
    decreasing = all(cash_on_hand[i][1] >= cash_on_hand[i + 1][1] for i in range(len(cash_on_hand) - 1))

    if increasing:
        output += "\n[CASH ON-HAND] Always increasing"
    elif decreasing:
        output += "\n[CASH ON-HAND] Always decreasing"
    else:
        output += "\n[CASH ON-HAND] Fluctuates"
   
    # Keep track of days where there is a cash deficit and surplus
    deficit_days = []

    # Day range from day 11 to day 90
    for day in range(11, min(90, len(cash_on_hand))):
        current_cash = int(cash_on_hand[day][1])
        previous_cash = int(cash_on_hand[day - 1][1])

        if current_cash <= previous_cash:
            deficit_days.append((day, previous_cash - current_cash))
        else:
            deficit_days.append((day, current_cash - previous_cash))
    
    top_deficit_days = sorted(deficit_days, key=sort_by_second_element, reverse=True)[:3]

    # Find the highest increment and decrement
    highest_increment_day = None
    highest_increment_amount = 0
    highest_decrement_day = None
    highest_decrement_amount = 0

    # Iterate through the rest of the elements in cash_on_hand
    for day in range(11, min(90, len(cash_on_hand))):
        # Extract the cash value from the current day and the previous day
        current_cash = int(cash_on_hand[day][1])
        previous_cash = int(cash_on_hand[day - 1][1])

        # Calculate the increment for the current day
        increment = current_cash - previous_cash
        # Check if the increment is greater than the highest_increment_amount
        if increment > highest_increment_amount:
            highest_increment_amount = increment
            highest_increment_day = day

        # Calculate the decrement for the current day
        decrement = previous_cash - current_cash
        # Check if the decrement is greater than the highest_decrement_amount
        if decrement > highest_decrement_amount:
            highest_decrement_amount = decrement
            highest_decrement_day = day

    # Print the highest increment and decrement
    if highest_increment_day is not None:
        output += f"\n[HIGHEST INCREMENT] Day: {highest_increment_day}, Amount: USD{highest_increment_amount}"

    if highest_decrement_day is not None:
        output += f"\n[HIGHEST DECREMENT] Day: {highest_decrement_day}, Amount: USD{highest_decrement_amount}"

    # List down all the days and amounts when deficit occurs
    all_deficit_output = "\n[ALL DEFICIT DAYS]"
    deficit_days.sort(key=sort_by_second_element, reverse=True)
    for day, deficit in deficit_days:
        deficit_day = int(cash_on_hand[day][0])
        all_deficit_output += f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}"
    # Append the top 3 cash deficit to the main output
    output += all_deficit_output
    
    # Sort the top 3 deficit days by days in ascending order
    top_deficit_days.sort()

    #Append the top 3 cash deficit to the main output
    output += "\n[TOP 3 DEFICIT DAYS]"
    for i, (day, deficit) in enumerate(top_deficit_days, start=1):
        deficit_day = int(cash_on_hand[day][0])
        all_deficit_output += f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}"


    # Initialize max_cash and max_day with values from the first element
    max_cash = float(cash_on_hand[0][1])
    max_day = cash_on_hand[0][0]

    # Iterate through the rest of the elements in cash_on_hand
    for day, deficit in top_deficit_days:
        # Extract the cash value from the current day
        cash = int(cash_on_hand[day][1])
        # Check if the current cash value is greater than the max_cash
        if cash > max_cash:
            # Update max_cash and max_day with the current values
            max_cash = cash
            max_day = int(cash_on_hand[day][0])

    previous_day = int(max_day) - 1
    previous_day_cash = 0

    for day in cash_on_hand:
        if int(day[0]) == previous_day:
            previous_day_cash = int(day[1])
            break

    # Append the result to the summary_report.txt file starting from the second line
    with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
        write_file.write("\n[TOP 3 DEFICIT DAYS]\n")
        for i, (day, deficit) in enumerate(top_deficit_days, start=1):
            deficit_day = int(cash_on_hand[day][0])
            write_file.write(f"[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}\n")

        # Write all cash deficit days
        write_file.write("\n[ALL DEFICIT DAYS]\n")
        deficit_days.sort()
        for i, (day, deficit) in enumerate(deficit_days, start=1):
            deficit_day = int(cash_on_hand[day][0])
            write_file.write(f"[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}\n")

    
    
    return output


result = cash_function ()




