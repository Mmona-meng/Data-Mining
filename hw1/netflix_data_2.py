from collections import Counter

file_path = '/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/movie_titles.csv'


def count_unique_movie_titles(file_path):
    unique_titles = set()
    # using 'latin1' encoding for compatibility
    with open(file_path, 'r', encoding='latin1') as file:
        for line in file:
            parts = line.strip().split(',')
            # Joining all parts except the first two (MovieID and YearOfRelease)
            title = ','.join(parts[2:])
            unique_titles.add(title)
    return len(unique_titles)


total_unique_titles = count_unique_movie_titles(file_path)
print(f"Total unique movie titles: {total_unique_titles}")


def count_titles_with_four_occurrences(file_path):
    title_counter = Counter()
    with open(file_path, 'r', encoding='latin1') as file:
        for line in file:
            parts = line.strip().split(',')
            title = ','.join(parts[2:])
            title_counter[title] += 1
    four_occurrences = [title for title,
                        count in title_counter.items() if count == 4]
    return len(four_occurrences), four_occurrences


count, titles = count_titles_with_four_occurrences(file_path)
print(f"Number of movie names referring to four different movies: {count}")
print("Titles:", titles)
