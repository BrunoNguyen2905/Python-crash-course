import csv

# have to pass correct delimiter to read the csv file
# with open('example.csv', mode='r', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # next(csv_reader)  # Skip header row if present
#     with open('new_output.csv', mode='w', newline='') as new_file:
#         # csv_writer = csv.writer(new_file, delimiter='-')
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for row in csv_reader:
#             # Process each row (for example, convert all text to uppercase)
#             # processed_row = [element.upper() for element in row]
#             csv_writer.writerow(row)

with open('new_output.csv', mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='\t')
    with open('new_output_1.csv', mode='w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()  # Write header row
        for row in csv_reader:
          # Method 1: mutate original row by deleting unwanted fields
            # del row['email']  # Remove unwanted field
            # csv_writer.writerow(row)
            # Build a new dict with only the fields we want (do not mutate original row)
          # Method 2: build new dict
            new_row = {
                'first_name': row.get('first_name', '').strip(),
                'last_name': row.get('email', '').strip(),
            }
            csv_writer.writerow(new_row)
    # for row in csv_reader:
    #     print(row['email'])
