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
    output = ""

    # Check if cash-on-hand is always increasing or decreasing
    increasing = all(cash_on_hand[i][1] <= cash_on_hand[i + 1][1] for i in range(len(cash_on_hand) - 1))
    decreasing = all(cash_on_hand[i][1] >= cash_on_hand[i + 1][1] for i in range(len(cash_on_hand) - 1))

    # Check if cash-on-hand is always increasing or decreasing
    if increasing:
        output += "\n[CASH ON HAND] Always increasing"
        # Add a line to write to the file
        with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
            write_file.write("\n[CASH ON HAND] Always increasing\n")
    elif decreasing:
        output += "\n[CASH ON HAND] Always decreasing"
        # Add a line to write to the file
        with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
            write_file.write("\n[CASH ON HAND] Always decreasing\n")
    else:
        output += "\n[CASH ON-HAND] Fluctuates" 
        # Add a line to write to the file
        with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
            write_file.write("\n[CASH ON HAND] Fluctuates\n")

    # Keep track of days where there is a cash deficit and surplus (empty list)
    deficit_days = []

    # Day range from day 11 to day 90
    for day in range(11, min(90, len(cash_on_hand))):
        current_cash = int(cash_on_hand[day][1])
        previous_cash = int(cash_on_hand[day - 1][1])

        if current_cash <= previous_cash:
            deficit_days.append((day, previous_cash - current_cash))
        else:
            deficit_days.append((day, current_cash - previous_cash))
    
    # Sort the deficit_days list in descending order by the second element (deficit amount), 
    # then select the top 3 deficit days with the highest deficit amount.
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

    #Append the result to the summary_report.txt file starting from the second line
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

    
    #Sort the top 3 deficit days by days in ascending order
    top_deficit_days.sort()

    # List down all the days and amounts when deficit occurs
    all_deficit_output = "\n[ALL DEFICIT DAYS]"
    for day, deficit in deficit_days:
        deficit_day = int(cash_on_hand[day][0])
        all_deficit_output += f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}"
    # Append the top 3 cash deficit to the main output
    output += all_deficit_output
    
   

    return output

result = cash_function ()

