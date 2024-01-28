from pathlib import Path
import csv 

# Function to sort items based on the second element in a tuple (used for sorting surplus_days_with_amounts)
def sort_by_second_element(item):
    return item[1]

# Define the main function for processing profit and loss data
def profit_function():
    # specific absolute paths for input and output files
    file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
    file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

    # Read the CSV file to append profit and quantity data
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # Skip the header row
        header = next(file)
        profit_loss_data = [list(map(float, line.strip().split(','))) for line in file]

    # Initialize an empty string to store the output message
    output = ""

    # Check if net profit is always increasing or decreasing
    increasing = all(profit_loss_data[i][1] <= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))
    decreasing = all(profit_loss_data[i][1] >= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))

    if increasing:
        output += "\n[NET PROFIT] Always increasing"
    elif decreasing:
        output += "\n[NET PROFIT] Always decreasing"
    else:
        output += "\n[NET PROFIT] Fluctuates"

    # Keep track of days when there is a net profit surplus
    surplus_days_with_amounts = []

    # Day range from day 11 to day 90
    for day in range(11, min(90, len(profit_loss_data))):
        current_profit = profit_loss_data[day][1]
        previous_profit = profit_loss_data[day - 1][1]

        # Calculate the surplus for the current day
        surplus = current_profit - previous_profit
        surplus_days_with_amounts.append((day, surplus))

    # Sort the surplus days with amounts based on the surplus amount
    sorted_surplus_days = sorted(surplus_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

    # Find the highest profit increment and decrement
    highest_increment_day = None
    highest_increment_amount = 0
    highest_decrement_day = None 
    highest_decrement_amount = 0

    # Iterate through the rest of the elements in profit_loss_data
    for day in range(11, min(90, len(profit_loss_data))):
        current_profit = profit_loss_data[day][1]
        previous_profit = profit_loss_data[day - 1][1]

        # Calculate the increment for the current day
        increment = current_profit - previous_profit
        # Check if the increment is greater than the highest_increment_amount
        if increment > highest_increment_amount:
            highest_increment_amount = increment
            highest_increment_day = day

        # Calculate the decrement for the current day
        decrement = previous_profit - current_profit
        # Check if the decrement is greater than the highest_decrement_amount
        if decrement > highest_decrement_amount:
            highest_decrement_amount = decrement
            highest_decrement_day = day

    # Print the highest profit increment and decrement
    if highest_increment_day is not None:
        output += f"\n[HIGHEST INCREMENT] Day: {highest_increment_day}, Amount: USD{int(highest_increment_amount)}"

    if highest_decrement_day is not None:
        output += f"\n[HIGHEST DECREMENT] Day: {highest_decrement_day}, Amount: USD{int(highest_decrement_amount)}"
    
    # Sort the top 3 surplus days by days in ascending order
    sorted_surplus_days.sort()

    # Append the top 3 net profit surplus to the main output
    output += "\n[TOP 3 PROFIT SURPLUS]"
    for i, (day, surplus) in enumerate(sorted_surplus_days, start=1):
        surplus_day = int(profit_loss_data[day][0])
        output += f"\n[HIGHEST PROFIT SURPLUS {i}] DAY: {surplus_day}, AMOUNT: USD{int(surplus)}"

    #sort the net profit surplus days by days in ascending order
    surplus_days_with_amounts.sort()

    output += "\n[NET PROFIT SURPLUS DAYS]"
    surplus_days_with_amounts.sort()
    for day, surplus in surplus_days_with_amounts:
        surplus_day = int(profit_loss_data[day][0])
        output += f"\n[NET PROFIT SURPLUS] DAY: {surplus_day}, AMOUNT: USD{int(surplus)}"

    # Append the result to the summary_report.txt file
    with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
        write_file.write("\n" + output)

profit_function()
