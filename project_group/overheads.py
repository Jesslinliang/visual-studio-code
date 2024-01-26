# from pathlib import Path
# import csv
# def overheads_function():
#     # create a file to csv file.
#     fp_read = Path(r"C:\project_group\csv_reports\Overheads.csv")
#     fp_write = Path(r"C:\project_group\summary_report.txt")

#     # read the csv file to append profit and quantity from the csv.
#     with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader)  # skip header
#         Overheads =[]
#         for row in reader:
#             Overheads.append([row[0],row[1]])

#     output = ""
#     max_value = float(Overheads[0][1])
#     max_category = Overheads[0][0]

#     for category in Overheads:
#         value = float(category[1])
#         if value > max_value:
#             max_value = value
#             max_category = category[0]

    
#     output += f"[HIGHEST OVERHEADS] {max_category}: {max_value}%"

#     with fp_write.open(mode="a", encoding="UTF-8") as report_file:
#         report_file.write(output)
    
#     print("Output written to summary_report.txt")
#     return output


from pathlib import Path
import csv

def overheads_function():
    # create a file to csv file.
    fp_read = Path(r"C:\project_group\csv_reports\Overheads.csv")
    fp_write = Path(r"C:\project_group\summary_report.txt")

    # read the csv file to append profit and quantity from the csv.
    with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        Overheads = []
        for row in reader:
            Overheads.append([row[0], row[1]])

    output = ""
    max_value = float(Overheads[0][1])
    max_category = Overheads[0][0]

    for category in Overheads:
        value = float(category[1])
        if value > max_value:
            max_value = value
            max_category = category[0]

    output += f"[HIGHEST OVERHEADS] {max_category}: {max_value}%"

    try:
        # Write the output to summary_report.txt
        with fp_write.open(mode="a", encoding="UTF-8") as report_file:
            report_file.write(output)
            print("Output written to summary_report.txt")
    except Exception as e:
        print(f"Error writing to summary_report.txt: {e}")

    return output