# from pathlib import Path
# import csv

# def compute_net_profit_differences(net_profit_data):
#     differences = []

#     for i in range(11, min(91, len(net_profit_data))):
#         try:
#             current_profit = int(net_profit_data[i][1].replace(",", ""))
#             previous_profit = int(net_profit_data[i - 1][1].replace(",", ""))
#             difference = current_profit - previous_profit
#             differences.append(difference)
#         except (ValueError, IndexError):
#             # Skip rows with non-numeric data or index errors
#             pass

#     return differences
# def identify_highest_increment_decrement(differences):
#     if all(diff > 0 for diff in differences):
#         max_increment = max(differences)
#         day_of_max_increment = differences.index(max_increment) + 12
#         return f"Maximum Increment: Day {day_of_max_increment}, Amount: USD {max_increment}"

#     elif all(diff < 0 for diff in differences):
#         max_decrement = min(differences)
#         day_of_max_decrement = differences.index(max_decrement) + 12
#         return f"Maximum Decrement: Day {day_of_max_decrement}, Amount: USD {max_decrement}"

#     else:
#         deficit_days = [day + 11 for day, diff in enumerate(differences) if diff < 0]
#         top_3_deficits = sorted([(day, differences[day - 11]) for day in deficit_days],
#                                 key=lambda x: x[1], reverse=True)[:3]
#         return f"Top 3 Deficits: {top_3_deficits}"

# def profit_function(input_csv_path, output_csv_path):
#     csv_file_path = Path(input_csv_path)
#     output_file_path = Path(output_csv_path)

#     try:
#         with csv_file_path.open(mode="r", encoding="UTF-8", newline="") as file:
#             reader = csv.reader(file)
#             for _ in range(7):
#                 next(reader)
#             net_profit_data = list(reader)
#     except FileNotFoundError:
#         return f"CSV file not found at: {csv_file_path}"

#     differences = compute_net_profit_differences(net_profit_data)
#     result = identify_highest_increment_decrement(differences)

#     # Additional processing or reporting based on the identified result can be added here

#     return result

# # Specify your input and output file paths
# input_csv_path = r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Overheads.csv"
# output_txt_path = r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\project_group\summary_report.txt"

# profit_function(input_csv_path, output_txt_path)

from pathlib import Path
import csv

def analyze_net_profit_trend(net_profit):
    differences = []

    for i in range(1, len(net_profit)):
        try:
            current_profit = float(net_profit[i][4])
            previous_profit = float(net_profit[i-1][4])
            difference = current_profit - previous_profit
            differences.append(difference)
        except (ValueError, IndexError):
            # Skip rows with non-numeric data or index errors
            pass

    if not differences:
        return "[NET PROFIT TRENDS] Unable to determine the trend."

    if all(diff >= 0 for diff in differences):
        max_increment = max(differences)
        day_of_max_increment = differences.index(max_increment) + 2  # Adjust index for differences
        return f"[NET PROFIT INCREMENT] Day {day_of_max_increment}, Amount: USD {max_increment}"

    elif all(diff <= 0 for diff in differences):
        max_decrement = min(differences)
        day_of_max_decrement = differences.index(max_decrement) + 2  # Adjust index for differences
        return f"[NET PROFIT DECREMENT] Day {day_of_max_decrement}, Amount: USD {max_decrement}"

    else:
        deficit_days = [(day, differences[day - 2]) for day, diff in enumerate(differences, start=2) if diff < 0]

        # Sort the deficit days based on the amount in descending order using a custom comparison function
        deficit_days.sort(key=deficit_sort_key, reverse=True)

        # Select the top 3 deficits
        top_3_deficits = deficit_days[:3]

        deficit_output = "\n".join(f"[PROFIT DEFICIT] Day; {day}, AMOUNT: USD{amount}" for day, amount in top_3_deficits)
        return f"[NET PROFIT FLUCTUATION] {deficit_output}"

def deficit_sort_key(item):
    # Custom comparison function to be used as the key parameter for sort
    return item[1]

def profit_function():
    # create a file to csv file.
    file_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\profits_and_Loss.csv")
    fp_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\project_group\summary_report.txt")

    # read the csv file to append profit and quantity from the csv.
    with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        net_profit = [row for row in reader]

    # Analyze net profit trend
    trend_analysis = analyze_net_profit_trend(net_profit)

    # Perform additional analysis or reporting based on the identified result

    # Write the result to the output text file
    with fp_write.open(mode="a", encoding="UTF-8") as output_file:
        output_file.write(trend_analysis + "\n")

    print("Analysis result written to:", fp_write)

# Call the function to perform the analysis and write the result to the output file
profit_function()