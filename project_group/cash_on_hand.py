from pathlib import Path
import csv

def sort_by_second_element(item):
    return item[1]

def cash_function():
    # specific absolute paths for input and output files
    fp_read = Path(r"C:\project_group\csv_reports\Cash_on_hand.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")


# Read the csv file to append profit and quantity from the csv.
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
        cash_on_hand=[] #Store the data read from the csv file 

        for row in reader:
            cash_on_hand.append([int[0],float(row[1])])

    #Keep track of days where there is a cash deficit and surplus
    deficit_days = []  
    surplus_days = []

    # Day range from day 11 to day 90
    for day in range(11, min(90,len(cash_on_hand))):
        current_cash = int(cash_on_hand[day][1])
        previous_cash = int(cash_on_hand[day-1][1])

        if current_cash <= previous_cash:
            deficit_days.append(day, previous_cash - current_cash)
        else:
            surplus_days.append((day, current_cash - previous_cash))

    output = ""

    if deficit_days:
        deficit_days.sort(key=sort_by_second_element, reverse = True)
        for day, deficit in deficit_days[:3]:    #Limit to the top 3 deficit days
            deficit_day = int(cash_on_hand[day][0])
            output += f"\n[CASH DEFICIT] Day: {deficit_day}, AMOUNT: USD{deficit}"
            
            break # Break removed to show all top 3 deficit days
    else:
        surplus_days.sort(key=sort_by_second_element, reverse = True)
        for day, surplus in surplus_days[:3]:    # Limit to the top 3 surplus days
            surplus_day = int(cash_on_hand[day][0])
            output += f"\n[CASH SURPLUS] Day: {surplus}, AMOUNT: USD{surplus}"
            
            break # Break removed to show all top 3 surplus days

        # Initialize max_cash and max_day with values from the first element
        max_cash = float(cash_on_hand[0][1])
        max_day = cash_on_hand[0][0]

        #Iterate through the rest of the elements in cash_on_hand
        for day in cash_on_hand:
            #Extract the cash value from the current day
            cash = float(day[1])
            #Check if the current cash value is greater than the max_cash
            if cash > max_cash:
                #Update max_cash and max_day with the current values
                max_cash = cash
                max_day = day [0]
        
        previous_day = int(max_day) - 1
        previous_day_cash = 0

        for day in cash_on_hand:
            if int(day[0]) == previous_day:
                previous_day_cash = float(day[1])
                break
        
        surplus = max_cash - previous_day_cash
        output += "\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        output += f"\n[HIGHEST CASH SURPLUS] DAY: {max_day}, AMOUNT: USD{surplus}"

    # Append the result to the summary_report.txt file starting from the second line
    with fp_write.open(mode="a", encoding="UTF-8") as write_file:
        write_file.write("\n" + output)

    return output

# Call the function and print the result
result = cash_function()
print(result)




