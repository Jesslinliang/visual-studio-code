from pathlib import Path
import csv
def profit_function():
    # create a file to csv file.
    file_read = Path(r"C:\project_group\csv_reports\Profit_loss.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")

    # read the csv file to append profit and quantity from the csv.
    with file_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        net_profit=[] 
    # Iterate over rows and store data in a dictionary
        for row in reader:
            net_profit.append({
                "day": int(row[0]),
                "item": row[1],
                "note": row[2],
                "amount": int(row[3]),
                "net_profit": int(row[4])
            })

    deficit_days = []

    #Iterate over days to comput deficit days
    for day in range(1, len(net_profit)):
        current_profit = net_profit[day]["net_profit"]
        previous_profit = net_profit[day-1]["net_profit"]
    # Check if the current day's net profit is less than the previous day's
        if current_profit <= previous_profit:
            deficit_days.append(day)

    output = ""
    if deficit_days:
        # Iterate over deficit days and compute deficit amounts
        for day in deficit_days:               
            current_profit = net_profit[day]["net_profit"]
            previous_profit = net_profit[day-1]["net_profit"]
            deficit = previous_profit - current_profit
            deficit_day = net_profit[day]["day"]
            output += (f"\n[PROFIT DEFICIT] Day; {deficit_day}, AMOUNT: USD{deficit}")

    else:
        # Find the day with the highest net ptofit
        max_profit = float(net_profit[0]["net_profit"])
        max_day = net_profit[0]["day"]

        for day in net_profit:
            profit = float(day["net_profit"])
            if profit > max_profit:
                max_profit = profit
                max_day = day_data["day"]

        # Find the net profit on the day before the highest net profit day
        previous_day = int(max_day) - 1
        previous_day_profit = 0

        for day_data in net_profit:
            if day_data["day"] == previous_day:
                previous_day_profit = float(day_data["net_profit"])
                break
        
        # Compute surplus and add to the output
        surplus = max_profit - previous_day_profit
        output += (f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        output += (f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

    return output
 