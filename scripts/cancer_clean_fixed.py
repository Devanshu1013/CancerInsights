import csv

input_file = "cancer.csv"
output_file = "cancer_clean_fixed.csv"

with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        cleaned_row = [cell.replace("\n", " ").replace("\r", " ") for cell in row]
        writer.writerow(cleaned_row)

print("✅ Cleaned CSV saved as cancer_clean_fixed.csv")