# from pathlib import Path
# import csv
# def sort_by_amount(item):
#     return item[1]

# def calculate_increment(item, net_profit_filtered):
#     return item["net_profit"] - net_profit_filtered[net_profit_filtered.index(item)-1]["net_profit"]

# def calculate_decrement(item, net_profit_filtered):
#     return net_profit_filtered[net_profit_filtered.index(item) - 1]["net_profit"] - item["net_profit"]

# def profit_function():
#     # create a file to csv file.
#     file_read = Path(r"C:\project_group\csv_reports\Profit_loss.csv")
#     fp_write = Path(r"C:\project_group\summary_report.txt")

#     # read the csv file to append profit and quantity from the csv.
#     with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader) # skip header
#         net_profit=[] 
#     # Iterate over rows and store data in a dictionary
#         for row in reader:
#             net_profit.append({
#                 "day": int(row[0]),
#                 "item": row[1],
#                 "note": row[2],
#                 "amount": int(row[3]),
#                 "net_profit": int(row[4])
#             })
#     #Filter net_profit data for days from 11 to 90
#     net_profit_filtered = [data for data in net_profit if 11<= data["day"] <= 90]

#     deficit_days = []


#     #Iterate over days to comput deficit days
#     for i in range(1, len(net_profit)):
#         current_profit = net_profit[day]["net_profit"]
#         previous_profit = net_profit[i-1]["net_profit"]
#     # Check if the current day's net profit is less than the previous day's
#         if current_profit <= previous_profit:
#             deficit_days.append(net_profit_filtered[i]["day"])

#     output = ""
#     if deficit_days:
#         # Iterate over deficit days and compute deficit amounts
#         deficit_amounts = [net_profit_filtered[day]["net profit"] - net_profit_filtered[i-1]["net_profit"] for i in range (1,len(net_profit_filtered)) if net_profit_filtered [i]["day"] in deficit_days]
#         deficit_days_with_amounts = list(zip(deficit_days,deficit_amounts))
#         deficit_days_with_amounts.sort(key=sort_by_amount, reverse=True)

#         output += "\n\n[TOP 3 DEFICIT DAYS]\n"
#         for day, amount in deficit_days_with_amounts[:3]:
#             output += f"Day {day}: AMOUNT: USD{amount}\n"

#     else:
#         # Find the day with the highest net ptofit amount
#         max_increment = max(net_profit_filtered, key=calculate_increment)
#         output += f"\n[HIGHEST INCREMENT] Day: {max_increment["day"]}, AMOUNT: USD{calculate_increment(max_increment)}\n"

#     # Find the day with the highest net profit decrement
#         max_decrement = min(net_profit_filtered, key=calculate_decrement)
#         output += f"[HIGHEST DECREMENT] Day: {max_decrement["day"]}, AMOUNT:USD{calculate_decrement(max_decrement)}\n"
                                              
#     return output
 
from pathlib import Path
import csv

# Function to sort items based on the second element in a tuple (used for sorting deficit_days_with_amounts)
def sort_by_amount(item):
    return item[1]

# Function to calculate the increment in net profit for a given item
def calculate_increment(item, filtered_data):
    return item["net_profit"] - filtered_data[filtered_data.index(item) - 1]["net_profit"]

# Function to calculate the decrement in net profit for a given item
def calculate_decrement(item, filtered_data):
    return filtered_data[filtered_data.index(item) - 1]["net_profit"] - item["net_profit"]

# Function to get the amount for a deficit day
def get_deficit_amount(day, filtered_data):
    return filtered_data[day]["net_profit"] - filtered_data[day - 1]["net_profit"]

# Function to find the day with the highest net profit increment
def find_highest_increment(filtered_data):
    max_increment = filtered_data[0]

    for item in filtered_data[1:]:
        if calculate_increment(item, filtered_data) > calculate_increment(max_increment, filtered_data):
            max_increment = item

    return max_increment

# Function to find the day with the highest net profit decrement
def find_highest_decrement(filtered_data):
    max_decrement = filtered_data[0]

    for item in filtered_data[1:]:
        if calculate_decrement(item, filtered_data) > calculate_decrement(max_decrement, filtered_data):
            max_decrement = item

    return max_decrement

# Function to process profit data
def profit_function():
    # Path to the input CSV file
    file_read = Path(r"C:\project_group\csv_reports\Profit_loss.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")

    # Read the CSV file to append profit and quantity data
    with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        net_profit = []

        # Iterate over rows and store data in a dictionary
        for row in reader:
            net_profit.append({
                "day": int(row[0]),
                "item": row[1],
                "note": row[2],
                "amount": int(row[3]),
                "net_profit": int(row[4])
            })

        # Filter net_profit data for days from 11 to 90
            filtered_data = [data for data in net_profit if 11 <= data["day"] <= 90]

            deficit_days =[]
        # Iterate over days to compute deficit days
            for i in range(1,len(net_profit)):
                current_profit = net_profit[i]["net_profit"]
                previous_profit = net_profit[i-1]["net_profit"]

                # Check if the current day's net profit is less than the previous day's
                if current_profit <= previous_profit:
                    deficit_days.append(net_profit[i]["day"])

            output = ""
            if deficit_days:
                # Iterate over deficit days and compute deficit amounts
                deficit_days_with_amounts = [(day, get_deficit_amount(day,filtered_data)) for day in deficit_days]

                #Sort deficit_days_with_amounts based on amounts in descending order
                deficit_days_with_amounts.sort(key=sort_by_amount, reverse=True)

                output += "\n\n[TOP 3 DEFICIT DAYS]\n"
                for day, amount in deficit_days_with_amounts[:3]:
                    output += f"Day{day}: AMOUNT: USD{amount}\n"

            else:
                # Find the day with the highest net profit increment
                max_increment = find_highest_increment(filtered_data)
                output += f"\n[HIGHEST INCREMENT] Day: {max_increment['day']}, AMOUNT: USD{calculate_increment(max_increment, filtered_data)}\n"   

                 # Find the day with the highest net profit decrement
                max_decrement = find_highest_decrement(filtered_data)
                output += f"[HIGHEST DECREMENT] Day: {max_decrement['day']}, AMOUNT: USD{calculate_decrement(max_decrement, filtered_data)}\n"

    return output      

