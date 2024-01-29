from pathlib import Path
import csv

def overheads_function():
    # Specify absolute paths for input and output files
    file_path_read = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\csv_reports\Overheads.csv")
    file_path_write = Path(r"C:\Users\jessl\OneDrive\Microsoft Teams Chat Files\visual studio code\summary_report.txt")


    # Read the CSV file to append profit and quantity from the CSV.
    print("Opening file:", file_path_read)
    with file_path_read.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            Overheads_data = []
            for row in reader:
                Overheads_data.append([row[0], row[1]])
    # Find the category with the highest overheads
    output = ""
    max_value = float(Overheads_data[0][1])
    max_category = Overheads_data[0][0]

    for category in Overheads_data:
            value = float(category[1])
            if value > max_value:
                max_value = value
                max_category = category[0]

    # Generate the output string
    output += f"[HIGHEST OVERHEADS] {max_category}: {max_value}%"

    # Write the result to the summary_report.txt file

    with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
            write_file.write(output + "\n")

    return output

# Call the function (the code inside the function must be called or it will not be executed.)
overheads_output = overheads_function()


