# from pathlib import Path
# import csv

# def cash_function(input_path):
#     # Read the CSV file
#     with input_path.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         header = next(reader)  # Get the header
#         cash_on_hand = [] 
#         for row in reader:
#             cash_on_hand.append([row[0], row[1]])

#     deficit_days = []

#     # Process days from 11 to 90
#     for day in range(10, min(90, len(cash_on_hand))):
#         current_cash = int(cash_on_hand[day][1])
#         previous_cash = int(cash_on_hand[day - 1][1])

#         # Check for cash deficit
#         if current_cash <= previous_cash:
#             deficit_days.append((int(cash_on_hand[day][0]), current_cash - previous_cash))

#     output = ""

#     # Check if deficit days exist
#     if deficit_days:
#         deficit_days.sort(key=lambda x: x[1], reverse=True)  # Sort by deficit amount

#         for day, deficit_amount in deficit_days:
#             output += (f"\n[CASH DEFICIT] Day: {day}, AMOUNT: USD{deficit_amount}")

#     else:
#         max_cash = float(cash_on_hand[0][1])
#         max_day = cash_on_hand[0][0]

#         # Find the day with the highest cash
#         for day in cash_on_hand:
#             cash = float(day[1])
#             if cash > max_cash:
#                 max_cash = cash
#                 max_day = day[0]

#         previous_day = int(max_day) - 1
#         previous_day_cash = 0

#         # Find the cash on the day before the highest cash day
#         for day in cash_on_hand:
#             if int(day[0]) == previous_day:
#                 previous_day_cash = float(day[1])
#                 break

#         surplus = max_cash - previous_day_cash
#         output += (f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
#         output += (f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

#     return output

# # Example usage
# input_path = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_Hand.csv")
# result = cash_function(input_path)

from pathlib import Path
import csv
def cash_function(input_path):

    # Read the CSV file
    with input_path.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the header
        cash_on_hand = [] 
        for row in reader:
            try:
                day = int(row[0])
                amount = int(row[1])
                cash_on_hand.append([day, amount])
            except (ValueError, IndexError):
                # Skip rows with non-numeric values in the "Amount" column
                continue

    deficit_days = []

    # Process days from 11 to 90
    for day in range(10, min(90, len(cash_on_hand))):
        try:
            current_cash = int(cash_on_hand[day][1])
            previous_cash = int(cash_on_hand[day - 1][1])

            # Check for cash deficit
            if current_cash <= previous_cash:
                deficit_days.append((int(cash_on_hand[day][0]), current_cash - previous_cash))
        except IndexError:
            # Handle the case where the index is out of range
            continue

    output = ""

    # Check if deficit days exist
    if deficit_days:
        # Sort deficit days by deficit amount using a custom sorting function
        deficit_days.sort(key=get_deficit_amount, reverse=True)

        for day, deficit_amount in deficit_days:
            output += (f"\n[CASH DEFICIT] Day: {day}, AMOUNT: USD{deficit_amount}")

    else:
        max_cash = float(cash_on_hand[0][1])
        max_day = cash_on_hand[0][0]

        # Find the day with the highest cash
        for day in cash_on_hand:
            cash = float(day[1])
            if cash > max_cash:
                max_cash = cash
                max_day = day[0]

        previous_day = int(max_day) - 1
        previous_day_cash = 0

        # Find the cash on the day before the highest cash day
        for day in cash_on_hand:
            if int(day[0]) == previous_day:
                previous_day_cash = float(day[1])
                break

        surplus = max_cash - previous_day_cash
        output += (f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        output += (f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

    return output

# Function to get the deficit amount for sorting
def get_deficit_amount(item):
    return item[1]

# Example usage
input_path = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_Hand.csv")
result = cash_function(input_path)
print(result)