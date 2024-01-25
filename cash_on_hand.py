from pathlib import Path
import csv

def cash_function():
    # Get the current working directory
    

    # Define paths to CSV and output file using current_directory
    fp_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_Hand.csv")
    fp_write = (r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\summary_report.txt")

    # Read cash data from CSV
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.DictReader(file)
        cash_data = [row for row in reader]

    deficit_days = []
    output = ""

    # Process data from day 11 to day 90
    for day in range(11, min(91, len(cash_data))):
        current_amount = int(cash_data[day]["Amount"])
        previous_amount = int(cash_data[day - 1]["Amount"])

        if current_amount <= previous_amount:
            deficit_days.append(day)

    if deficit_days:
        for day in deficit_days:
            current_amount = int(cash_data[day]["Amount"])
            previous_amount = int(cash_data[day - 1]["Amount"])
            deficit = previous_amount - current_amount
            deficit_day = int(cash_data[day]["Day"])
            output += f"[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}\n"
    else:
        max_amount = max(int(row["Amount"]) for row in cash_data)
        max_day = max(int(row["Day"]) for row in cash_data if int(row["Amount"]) == max_amount)

        previous_day = max_day - 1
        previous_day_amount = next(int(row["Amount"]) for row in cash_data if int(row["Day"]) == previous_day)

        surplus = max_amount - previous_day_amount
        output += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}\n"

    return output
    print(output)
