from pathlib import Path
import cash_on_hand
import profit_loss
import overheads

# Define file paths for input CSV files
file_path_read_cash = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Cash_on_hand.csv")
file_path_write_cash = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")
file_path_read_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Profit_loss.csv")
file_path_write_profit_loss = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")
file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Overheads.csv")
file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")

# Open the file in write mode
with file_path_write_cash.open(mode="w", encoding="UTF-8") as file:
    
    # Call the functions with the correct file paths
    overheads_output = overheads.overheads_function()
    cash_output = cash_on_hand.cash_function(file_path_read_cash, file_path_write_cash)

    # Handle the case where cash_output is None
    if cash_output is not None:
        file.write(cash_output + "\n")


    profit_output = profit_loss.profit_loss_function(file_path_read_profit_loss, file_path_write_profit_loss)

    # Handle the case where profit_output is None
    if profit_output is not None:
        file.write(profit_output + "\n")
 