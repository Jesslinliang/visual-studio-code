# from pathlib import Path
# import csv

# # Function to sort items based on the first element in a tuple (used for sorting deficit_days)
# def sort_by_first_element(item):
#     return item[0]

# # Define the main function for processing net profit data
# def net_profit_deficit_function(file_path_read, file_path_write):
#     # Read the CSV file to append profit and quantity data
#     with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
#         # Use csv.reader to handle CSV parsing
#         csv_reader = csv.reader(file)
        
#         # Skip the header row
#         header = next(csv_reader)
#         net_profit_data = [list(map(float, line)) for line in csv_reader]

#     # Initialize an empty string to store the output message
#     deficit_output = ""

#     # Keep track of days when there is a net profit deficit
#     deficit_days_with_amounts = []

#     # Day range from day 11 to day 90
#     for day in range(11, min(91, len(net_profit_data))):
#         current_profit = net_profit_data[day][4]
#         previous_profit = net_profit_data[day - 1][4]

#         # Calculate the deficit for the current day
#         deficit = previous_profit - current_profit

#         if deficit > 0:
#             deficit_days_with_amounts.append((day, deficit))

#     # Sort the deficit days with amounts based on the amount (second element in the tuple)
#     sorted_deficit_days = sorted(deficit_days_with_amounts, key=lambda x: x[1], reverse=True)

#     # Append all net profit deficit days and amounts to the main output
#     deficit_output += "\n[NET PROFIT DEFICIT DAYS]"
#     for day, deficit in sorted_deficit_days:
#         deficit_day = int(net_profit_data[day][0])
#         deficit_output += f"\n[NET PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

#     # Take the top 3 net profit deficit days based on the amount
#     top3_deficit_days = sorted_deficit_days[:3]

#     # Append the top 3 net profit deficit to the main output
#     deficit_output += "\n[TOP 3 NET PROFIT DEFICIT]"
#     for i, (day, deficit) in enumerate(top3_deficit_days, start=1):
#         deficit_day = int(net_profit_data[day][0])
#         position = {1: "HIGHEST", 2: "2ND HIGHEST", 3: "3RD HIGHEST"}.get(i)
#         deficit_output += f"\n[{position} NET PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

#     # Write results to the summary_report.txt file
#     with file_path_write.open(mode="w", encoding="UTF-8", newline="") as output_file:
#         output_file.write(deficit_output)

# # Paths for input and output files
# file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
# file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

# # Call the function with file paths
# net_profit_deficit_function(file_path_read, file_path_write)

from pathlib import Path
import csv

# Function to sort items based on the first element in a tuple (used for sorting deficit_days)
def sort_by_first_element(item):
    return item[0]

# Function to sort items based on the second element in a tuple (used for sorting top 3 deficit_days)
def sort_by_second_element(item):
    return item[1]

# Define the main function for processing profit and loss data
def profit_loss_function(file_path_read, file_path_write):
    # Read the CSV file to append profit and quantity data
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # Use csv.reader to handle CSV parsing
        csv_reader = csv.reader(file)
        
        # Skip the header row
        header = next(csv_reader)
        profit_loss_data = [list(map(float, line)) for line in csv_reader]

    # Initialize an empty string to store the output message
    deficit_output = ""

    # Keep track of days when there is a net profit deficit
    deficit_days_with_amounts = []

    # Day range from day 11 to the end of the data
    for day in range(10, len(profit_loss_data)):
        current_profit = profit_loss_data[day][4]
        previous_profit = profit_loss_data[day - 1][4]

        # Calculate the deficit for the current day
        deficit = previous_profit - current_profit

        if deficit > 0:
            deficit_days_with_amounts.append((int(profit_loss_data[day][0]), deficit))

    # Sort the deficit days with amounts based on the day
    sorted_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_first_element)

    # Append all net profit deficit days and amounts to the main output
    deficit_output += "\n[NET PROFIT DEFICIT DAYS]"
    for day, deficit in sorted_deficit_days:
        deficit_output += f"\n[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{int(deficit)}"

    # Sort the top 3 net profit deficit days based on the deficit amount
    sorted_top3_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

    # Append the top 3 net profit deficit to the main output
    deficit_output += "\n[TOP 3 NET PROFIT DEFICIT]"
    for i, (day, deficit) in enumerate(sorted_top3_deficit_days, start=1):
        position = {1: "HIGHEST", 2: "2ND HIGHEST", 3: "3RD HIGHEST"}.get(i)
        deficit_output += f"\n[{position} NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{int(deficit)}"

    # Write results to the summary_report.txt file
    with file_path_write.open(mode="a", encoding="UTF-8", newline="") as output_file:
        output_file.write(deficit_output)

# Paths for input and output files
file_path_read_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
file_path_write_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

# Call the function with file paths
profit_loss_function(file_path_read_profit_loss, file_path_write_profit_loss)