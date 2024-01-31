from pathlib import Path
import csv

def sort_by_first_element(item):
    return item[0]

def sort_by_second_element(item):
    return item[1]

def profit_loss_function(file_path_read, file_path_write):
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        profit_loss_data = [list(map(float, line)) for line in csv_reader]

    deficit_output = ""
    deficit_days_with_amounts = []

    for day in range(1, len(profit_loss_data)):
        current_profit = profit_loss_data[day][4]
        previous_profit = profit_loss_data[day - 1][4]
        deficit = previous_profit - current_profit

        if deficit > 0:
            deficit_days_with_amounts.append((int(profit_loss_data[day][0]), deficit))

    sorted_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_first_element)

    deficit_output += "\n[NET PROFIT DEFICIT DAYS]"
    for day, deficit in sorted_deficit_days:
        deficit_output += f"\n[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{int(deficit)}"

    sorted_top3_deficit_days = sorted(deficit_days_with_amounts, key=sort_by_second_element, reverse=True)[:3]

    deficit_output += "\n[TOP 3 NET PROFIT DEFICIT]"
    for i, (day, deficit) in enumerate(sorted_top3_deficit_days, start=1):
        position = {1: "HIGHEST", 2: "2ND HIGHEST", 3: "3RD HIGHEST"}.get(i)
        deficit_output += f"\n[{position} NET PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{int(deficit)}"

    with file_path_write.open(mode="a", encoding="UTF-8", newline="") as output_file:
        output_file.write(deficit_output)

# Paths for input and output files
file_path_read_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
file_path_write_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

# Call the function with file paths
profit_loss_function(file_path_read_profit_loss, file_path_write_profit_loss)