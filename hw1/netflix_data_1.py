file_path_1 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_1.txt"
file_path_2 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_2.txt"
file_path_3 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_3.txt"
file_path_4 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_4.txt"

file_names = [file_path_1, file_path_2, file_path_3, file_path_4]


def count_total_records(file_names):
    total_records = 0
    for file_name in file_names:
        with open(file_name, 'r') as file:
            for line in file:
                if ',' in line:
                    total_records += 1
    return total_records


total_records = count_total_records(file_names)
print(f"Total records: {total_records}")


def count_unique_users(file_names):
    unique_users = set()
    for file_name in file_names:
        with open(file_name, 'r') as file:
            for line in file:
                if ',' in line:
                    customer_id = line.split(',')[0]
                    unique_users.add(customer_id)
    return len(unique_users)


total_unique_users = count_unique_users(file_names)
print(f"Total unique users: {total_unique_users}")


def find_year_range(file_names):
    min_year, max_year = float('inf'), 0
    for file_name in file_names:
        with open(file_name, 'r') as file:
            for line in file:
                if ',' in line:
                    date = line.strip().split(',')[-1]
                    year = int(date.split('-')[0])
                    min_year = min(min_year, year)
                    max_year = max(max_year, year)
    return min_year, max_year


min_year, max_year = find_year_range(file_names)
print(f"Data range: {min_year} to {max_year}")
