from pathlib import Path
import csv

def cash_function():

    # create a file to csv file.
    fp_read = Path(r"C:\project_group\csv_reports\cash_on_hand.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")


# read the csv file to append profit and quantity from the csv.
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        cash_on_hand=[] 

        for row in reader:
            cash_on_hand.append([int[0],float(row[1])])

    deficit_days = []
    surplus_days = []

    
    for day in range(11, min(90,len(cash_on_hand))):
        current_cash = int(cash_on_hand[day][1])
        previous_cash = int(cash_on_hand[day-1][1])

        if current_cash <= previous_cash:
            deficit_days.append(day, previous_cash - current_cash)
        else:
            surplus_days.append((day, current_cash - previous_cash))

    output = ""

    if deficit_days:
        for day, deficit in deficit_days:
            deficit_day = int(cash_on_hand[day][0])
            output += (f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}")

    else:
        max_cash = float(cash_on_hand[0][1])
        max_day = cash_on_hand[0][0]

        for day in cash_on_hand:
            cash = float(day[1])
            if cash > max_cash:
                max_cash = cash
                max_day = day [0]
        
        previous_day = int(max_day) - 1
        previous_day_cash = 0

        for day in cash_on_hand:
            if int(day[0]) == previous_day:
                previous_day_cash = float(day[1])
                break
        
        surplus = max_cash - previous_day_cash
        output += (f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        output += (f"[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}")

    return output