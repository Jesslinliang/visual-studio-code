import csv
from pathlib import Path

def overheads_function(input_path, output_path):
    # Read the CSV file and extract relevant data
    with open(input_path, mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)  # Print the header

        # Extract data for rows where 'Day ' is between 11 and 90
        data = {}
        for row in reader:
            if "Day " in row and 11 <= int(row["Day "]) <= 90:
                data[row["Items "]] = float(row["Amount "])

    # Calculate the percentage for each category
    total_amount = sum(data.values())
    
    # Check if there is data before calculating percentages
    if total_amount == 0:
        print("No valid data for the specified range.")
        return

    percentages = {category: (amount / total_amount) * 100 for category, amount in data.items()}

    # Check if percentages dictionary is empty before finding the maximum
    if not percentages:
        print("No valid data for the specified range.")
        return

    # Find the highest overheads category
    max_category = max(percentages, key=percentages.get)
    max_value = percentages[max_category]

    # Write the transformed data to the output CSV file
    with open(output_path, mode="w", encoding="UTF-8", newline="") as file:
        file.write(f"[HIGHEST OVERHEADS] {max_category}: {round(max_value, 2)}%\n")

# Specify your input and output file paths
input_csv_path = r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Overheads.csv"
output_txt_path = r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\project_group\summary_report.txt"

# Call the function to transform the CSV data and find the highest overheads
overheads_function(input_csv_path, output_txt_path)