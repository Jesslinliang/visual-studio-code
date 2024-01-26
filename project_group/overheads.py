from pathlib import Path
import csv
def overheads_function():
    # create a file to csv file.
    file_path_read = Path(r"C:\project_group\csv_reports\Overheads.csv")
    file_path_write = Path(r"C:\project_group\summary_report.txt")

    #read the csv file to append profit and quantity from the csv.
    with file_path_read.open(mode="r", encoding = "UTF-8", newline ="") as file:
        reader = csv.reader(file)
        next(reader) #skip header
        Overheads_data = []
        for row in reader:
            Overheads_data.append([row[0],row[1]])

    output = ""
    max_value = float(Overheads_data[0][1])
    max_category = Overheads_data [0][0]

    for category in Overheads_data:
        value = float(category [1])
        if value > max_value:
            max_value = value
            max_category = category [0]

    output += (f"[HIGHEST OVERHEADS] {max_category}: {max_value}%")

    with file_path_write.open(mode="a", encoding="UTF-8") as write_file:
        write_file.write(output + "\n")

    return output