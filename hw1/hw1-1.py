import csv


def cardinality_items(filename):
    '''
    Takes a filename "*.csv" and returns an integer.
    '''
    unique_items = set()

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Add each item in the row to the set of unique items
            unique_items.update(row)

    return len(unique_items)


file_path = 'week1/basket_data.csv'
cardinality = cardinality_items(file_path)
print(cardinality)
