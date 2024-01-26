# from pathlib import Path
# import cash_on_hand
# import profit_loss
# import overheads

# def main():
#     # Call the functions to get the results
#     overheads_output = overheads.overheads_function()
#     cash_output = cash_on_hand.cash_on_hand_function()
#     profit_output = profit_loss.profit_function()

#     # Writing to the summary_report.txt file
#     file_path = Path(r"C:\project_summary\summary_report.txt")

#     with file_path.open(mode="w", encoding="UTF-8") as file:
#         # Write Scenario 1
#         file.write("SCENARIO 1\n")
#         file.write("1. Salary Expense is the highest overheads in “overheads.csv”\n")
#         file.write("2. Each value on the current day is higher than the previous day in “cash_on_hand.csv” and “profit_and_loss.csv”\n\n")

#         # Write the overheads output
#         file.write("[HIGHEST OVERHEADS] " + overheads_output + "\n")

#         # Write the cash_on_hand and profit_and_loss outputs
#         file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
#         file.write("[HIGHEST CASH SURPLUS] DAY: AMOUNT:\n")
#         file.write("[NET PROFIT SURPLUS] DAY: AMOUNT:\n")
#         file.write("[HIGHEST NET PROFIT SURPLUS] DAY: AMOUNT:\n\n")



from pathlib import Path
import cash_on_hand
import profit_loss
import overheads

 # Writing to the summary_report.txt file
file_path = Path(r"C:\project_summary\summary_report.txt")
file_path.touch()

with file_path.open(mode="w", encoding="UTF-8") as file:

    # Call the functions to get the results
    overheads_output = overheads.overheads_function()
    cash_output = cash_on_hand.cash_function()
    profit_output = profit_loss.profit_function()


        # Write the results to the file
    file.write(overheads_output)
    file.write(cash_output)
    file.write(profit_output)
