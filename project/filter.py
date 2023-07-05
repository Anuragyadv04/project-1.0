import csv
import re
input_csv = '.venv\product_data_a.csv'
# Open the input CSV file for reading
with open(input_csv, 'r') as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)

    # Open the output CSV file for writing
    with open('.venv\output.csv', 'w', newline='') as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)

        # Iterate over each row in the input CSV
        for i, row in enumerate(reader):
            # Check if it's the second row (index 1)
            if i == 1:
                # Process each cell in the second row
                processed_row = []
                for cell in row:
                    # Remove non-numeric characters using regex
                    cleaned_cell = re.sub(r'[^0-9]', '', cell)
                    processed_row.append(cleaned_cell)

                # Write the processed row to the output CSV
                writer.writerow(processed_row)
            else:
                # Write the unchanged row to the output CSV
                writer.writerow(row)

print("CSV processing complete!")