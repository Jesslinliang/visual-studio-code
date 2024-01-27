# from pathlib import Path
# import csv

# # Function to sort items based on the second element in a tuple (used for sorting deficit_days_with_amounts)
# def sort_by_second_element(item):
#     return item[1]

# # Define the main function for processing profit and loss data
# def profit_function():
#     # specific absolute paths for input and output files
#     file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
#     file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

#     # Read the CSV file to append profit and quantity data
#     with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header
#         profit_loss_data = []
#         for row in reader:
#             profit_loss_data.append([int(row[0]), float(row[1])])

#     # Initialize an empty string to store the output message
#     output = ""

#     # Check if net profit is always increasing or decreasing
#     increasing = all(profit_loss_data[i][1] <= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))
#     decreasing = all(profit_loss_data[i][1] >= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))

#     if increasing:
#         output += "\n[NET PROFIT] Always increasing"
#     elif decreasing:
#         output += "\n[NET PROFIT] Always decreasing"
#     else:
#         output += "\n[NET PROFIT] Fluctuates"

#     # Keep track of days when there is a net profit deficit
#     deficit_days_with_amounts = []

#     # Day range from day 11 to day 90
#     for day in range(11, min(90, len(profit_loss_data))):
#         current_profit = profit_loss_data[day][1]
#         previous_profit = profit_loss_data[day - 1][1]

#         # Calculate the deficit for the current day
#         deficit = previous_profit - current_profit
#         deficit_days_with_amounts.append((day, deficit))

#     # Sort the deficit days with amounts based on the deficit amount
#     sorted_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

#     # Find the highest profit increment and decrement
#     highest_increment_day = None
#     highest_increment_amount = 0

#     # Iterate through the rest of the elements in profit_loss_data
#     for day in range(11, min(90, len(profit_loss_data))):
#         current_profit = int(profit_loss_data[day][1])
#         previous_profit = int(profit_loss_data[day - 1][1])

#         # # Extract the profit value from the current day and the previous day
#         # current_profit = profit_loss_data[day][1]
#         # previous_profit = profit_loss_data[day - 1][1]

#         # Calculate the increment for the current day
#         increment = current_profit - previous_profit
#         # Check if the increment is greater than the highest_increment_amount
#         if increment > highest_increment_amount:
#             highest_increment_amount = increment
#             highest_increment_day = day

#         # # Calculate the decrement for the current day
#         # decrement = previous_profit - current_profit
#         # # Check if the decrement is greater than the highest_decrement_amount
#         # if decrement > highest_decrement_amount:
#         #     highest_decrement_amount = decrement
#         #     highest_decrement_day = day

#     # Print the highest profit increment and decrement
#     if highest_increment_day is not None:
#         output += f"\n[HIGHEST INCREMENT] Day: {highest_increment_day}, Amount: USD{int(highest_increment_amount)}"

# else:
#     # Keep track of days when there is a net profit deficit
#     deficit_days_with_amounts = []

     
#     # List down all the days and amounts when deficit occurs
#     output += "\n[ALL DEFICIT DAYS]"
#     deficit_days_with_amounts.sort(key=sort_by_second_element, reverse=True)
#     for day, deficit in deficit_days_with_amounts:
#         deficit_day = int(profit_loss_data[day][0])
#         output += f"\n[NET PROFIT DEFICIT] Day: {deficit_day}, AMOUNT: USD{int(deficit)}"

#     # Append the result to the summary_report.txt file starting from the second line
#     with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
#         write_file.write("\n" + output)

#     return output

# # Call the profit_function to generate the summary report
# result = profit_function()
# print(result)


from pathlib import Path
import csv

# Function to sort items based on the second element in a tuple (used for sorting deficit_days_with_amounts)
def sort_by_second_element(item):
    return item[1]

# Define the main function for processing profit and loss data
def profit_function():
    # specific absolute paths for input and output files
    file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
    file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

    # Read the CSV file to append profit and quantity data
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        profit_loss_data = []
        for row in reader:
            profit_loss_data.append([int(row[0]), float(row[1])])

    # Initialize an empty string to store the output message
    output = ""

    # Check if net profit is always increasing or decreasing
    increasing = all(profit_loss_data[i][1] <= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))
    decreasing = all(profit_loss_data[i][1] >= profit_loss_data[i + 1][1] for i in range(len(profit_loss_data) - 1))

    if increasing:
        output += "\n[HIGHEST PROFIT INCREMENT] DAY: "
        
        # Find the highest profit increment
        highest_increment_day = None
        highest_increment_amount = 0

        # Iterate through the rest of the elements in profit_loss_data
        for day in range(11, min(90, len(profit_loss_data))):
            current_profit = int(profit_loss_data[day][1])
            previous_profit = int(profit_loss_data[day - 1][1])

            # Calculate the increment for the current day
            increment = current_profit - previous_profit
            # Check if the increment is greater than the highest_increment_amount
            if increment > highest_increment_amount:
                highest_increment_amount = increment
                highest_increment_day = day

        # Print the highest profit increment
        if highest_increment_day is not None:
            output += f"{int(highest_increment_day)}, AMOUNT: USD{int(highest_increment_amount)}"

    elif decreasing:
        output += "\n[HIGHEST PROFIT DECREMENT] DAY: "
        
        # Find the highest profit decrement
        highest_decrement_day = None
        highest_decrement_amount = 0

        # Iterate through the rest of the elements in profit_loss_data
        for day in range(11, min(90, len(profit_loss_data))):
            current_profit = int(profit_loss_data[day][1])
            previous_profit = int(profit_loss_data[day - 1][1])

            # Calculate the decrement for the current day
            decrement = previous_profit - current_profit
            # Check if the decrement is greater than the highest_decrement_amount
            if decrement > highest_decrement_amount:
                highest_decrement_amount = decrement
                highest_decrement_day = day

        # Print the highest profit decrement
        if highest_decrement_day is not None:
            output += f"{int(highest_decrement_day)}, AMOUNT: USD{int(highest_decrement_amount)}"

    else:
        # Keep track of days when there is a net profit deficit
        deficit_days_with_amounts = []

        # Day range from day 11 to day 90
        for day in range(11, min(90, len(profit_loss_data))):
            current_profit = profit_loss_data[day][1]
            previous_profit = profit_loss_data[day - 1][1]

            # Calculate the deficit for the current day
            deficit = previous_profit - current_profit
            deficit_days_with_amounts.append((day, deficit))

        # Sort the deficit days with amounts based on the deficit amount
        sorted_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

        # Append the top 3 net profit deficit to the main output
        output += "\n[TOP 3 PROFIT DEFICIT]"
        for i, (day, deficit) in enumerate(sorted_deficit_days, start=1):
            deficit_day = int(profit_loss_data[day][0])
            output += f"\n[HIGHEST PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

        # List down all the days and amounts when deficit occurs
        output += "\n[ALL PROFIT DEFICIT DAYS]"
        deficit_days_with_amounts.sort(key=sort_by_second_element, reverse=True)
        for day, deficit in deficit_days_with_amounts:
            deficit_day = int(profit_loss_data[day][0])
            output += f"\n[HIGHEST PROFIT DEFICIT] DAY: {deficit_day}, AMOUNT: USD{int(deficit)}"

    # Append the result to the summary_report.txt file starting from the second line
    with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
        write_file.write("\n" + output)

    return output
