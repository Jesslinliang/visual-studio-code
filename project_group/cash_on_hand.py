from pathlib import Path
import csv

# Function to sort items based on the first element in a tuple (used for sorting deficit_days)
def sort_by_first_element(item):
    return item[0]

# Function to sort items based on the second element in a tuple (used for sorting top 3 deficit_days)
def sort_by_second_element(item):
    return item[1]

# Define the main function for processing cash data
def cash_function(file_path_read, file_path_write):
    # Read the CSV file to append profit and quantity data
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # Use csv.reader to handle CSV parsing
        csv_reader = csv.reader(file)
        
        # Skip the header row
        header = next(csv_reader)
        cash_data = [list(map(float, line)) for line in csv_reader]

    # Initialize an empty string to store the output message
    deficit_output = ""

    # Keep track of days when there is a negative cash deficit
    deficit_days_with_amounts = []

    # Day range from day 11 to the end of the data
    for day in range(1, len(cash_data)):
        current_cash = cash_data[day][1]
        previous_cash = cash_data[day - 1][1]

        # Calculate the deficit for the current day
        deficit = previous_cash - current_cash

        if deficit > 0:
            deficit_days_with_amounts.append((day + 1, deficit))  # Adjust indexing here

    # Sort the deficit days with amounts based on the day
    sorted_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_first_element)

    # Append all cash deficit days and amounts to the main output
    deficit_output += "\n[CASH DEFICIT DAYS]"
    for day, deficit in sorted_deficit_days:
        deficit_day = int(cash_data[day - 1][0])  # Adjust indexing here
        deficit_output += f"\n[CASH DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

    # Sort the top 3 cash deficit days based on the deficit amount
    sorted_top3_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

    # Append the top 3 cash deficit to the main output
    deficit_output += "\n[TOP 3 CASH DEFICIT]"
    for i, (day, deficit) in enumerate(sorted_top3_deficit_days, start=1):
        deficit_day = int(cash_data[day - 1][0])  # Adjust indexing here
        position = {1: "HIGHEST", 2: "2ND HIGHEST", 3: "3RD HIGHEST"}.get(i)
        deficit_output += f"\n[{position} CASH DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

    # Write results to the summary_report.txt file
    with file_path_write.open(mode="a", encoding="UTF-8", newline="") as output_file:
        output_file.write(deficit_output)

# Paths for input and output files
file_path_read_cash = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_hand.csv")
file_path_write_cash = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

# Call the function with file paths
cash_function(file_path_read_cash, file_path_write_cash)