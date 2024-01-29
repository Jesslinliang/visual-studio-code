# from pathlib import Path
# import cash_on_hand
# import profit_loss
# import overheads

#  # Writing to the summary_report.txt file
# file_path = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")
# file_path.touch()

# with file_path.open(mode="w", encoding="UTF-8") as file:

#     # Call the functions to get the results
#     overheads_output = overheads.overheads_function()
#     cash_output = cash_on_hand.cash_function()
#     profit_output = profit_loss.profit_function()


#     # Write the results to the file
#     file.write(overheads_output)
#     file.write(cash_output)
#     file.write(profit_output)




from pathlib import Path
import cash_on_hand, profit_loss, overheads

file_path = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")
file_path.touch()


with file_path.open(mode="w", encoding="UTF-8") as file:
    overheads_output = overheads.overheads_function()
    cash_output = cash_on_hand.cash_function()
    profit_output = profit_loss.profit_function()

    # Check and convert None to an empty string
    overheads_output = overheads_output or ""
    cash_output = cash_output or ""
    profit_output = profit_output or ""

    file.write(overheads_output)
    file.write(cash_output)
    file.write(profit_output)