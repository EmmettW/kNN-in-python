import csv

def format_dataset(filename, new_filename):
    with open(filename, 'rb') as csvfile:
        new_dataset = open(new_filename, "wb")
        reader = csv.reader(csvfile)
        writer = csv.writer(new_dataset)
        for row in reader:
            new_row = [None] * 7
            # Buying cost representation
            if repr(row[0]) == "'vhigh'":
                new_row[0] = '3.0'
            elif repr(row[0]) == "'high'":
                new_row[0] = '2.0'
            elif repr(row[0]) == "'med'":
                new_row[0] = '1.0'
            elif repr(row[0]) == "'low'":
                new_row[0] = '0.0'
            # Maintenance cost representation
            if repr(row[1]) == "'vhigh'":
                new_row[1] = '3.0'
            elif repr(row[1]) == "'high'":
                new_row[1] = '2.0'
            elif repr(row[1]) == "'med'":
                new_row[1] = '1.0'
            elif repr(row[1]) == "'low'":
                new_row[1] = '0.0'
            # Doors representation
            if repr(row[2]) == "'5more'":
                new_row[2] = '3.0'
            elif repr(row[2]) == "'4'":
                new_row[2] = '2.0'
            elif repr(row[2]) == "'3'":
                new_row[2] = '1.0'
            elif repr(row[2]) == "'2'":
                new_row[2] = '0.0'
            # Capacity representaion
            if repr(row[3]) == "'more'":
                new_row[3] = '2.0'
            elif repr(row[3]) == "'4'":
                new_row[3] = '1.0'
            elif repr(row[3]) == "'2'":
                new_row[3] = '0.0'
            # Trunk Size representaion
            if repr(row[4]) == "'big'":
                new_row[4] = '2.0'
            elif repr(row[4]) == "'med'":
                new_row[4] = '1.0'
            elif repr(row[4]) == "'small'":
                new_row[4] = '0.0'
            # Safety representaion
            if repr(row[5]) == "'high'":
                new_row[5] = '2.0'
            elif repr(row[5]) == "'med'":
                new_row[5] = '1.0'
            elif repr(row[5]) == "'low'":
                new_row[5] = '0.0'
            new_row[6] = row[6]
            # now we write new_row to csv file
            writer.writerow(new_row)