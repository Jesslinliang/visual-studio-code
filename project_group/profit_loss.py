from pathlib import Path
import csv
def profit_function():
    # create a file to csv file.
    file_read = Path(r"C:\project_group\csv_reports\Profit_and_Loss.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")

    # read the csv file to append profit and quantity from the csv.
    with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        net_profit=[] 
        for row in reader:
            net_profit.append([row[0],row[1],row[2],row[3],row[4]])

    deficit_days = []

    for day in range(1, len(net_profit)):
        current_profit = int(net_profit[day][4])
        previous_profit = int(net_profit[day-1][4])

        if current_profit <= previous_profit:
            deficit_days.append(day)

    output = ""
    if deficit_days:
        for day in deficit_days:               
            current_profit = int(net_profit[day][4])
            previous_profit = int(net_profit[day-1][4])
            deficit = previous_profit - current_profit
            deficit_day = int(net_profit[day][0])
            output += (f"\n[PROFIT DEFICIT] Day; {deficit_day}, AMOUNT: USD{deficit}")

    else:
        max_profit = float(net_profit[0][4])
        max_day = net_profit[0][0]

        for day in net_profit:
            profit = float(day[4])
            if profit > max_profit:
                max_profit = profit
                max_day = int(day[0])
        
        previous_day = int(max_day) - 1
        previous_day_profit = 0

        for day in net_profit:
            if int(day[0]) == previous_day:
                previous_day_profit = float(day[4])
                break

        surplus = max_profit - previous_day_profit
        output += (f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        output += (f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

    return output
 