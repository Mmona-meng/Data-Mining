from collections import defaultdict, Counter


def process_data(rating_files, movie_titles_file, exact_rating_count):
    # Load movie titles efficiently
    movie_titles = {}
    with open(movie_titles_file, 'r', encoding='latin1') as file:
        movie_titles = {line.split(',')[0]: ','.join(
            line.strip().split(',')[2:]) for line in file}

    # Initialize counters and a dictionary to track user ratings
    user_ratings_count = Counter()
    user_ratings = defaultdict(dict)

    for file_name in rating_files:
        with open(file_name, 'r') as file:
            current_movie_id = None
            for line in file:
                if ':' in line:
                    current_movie_id = line.split(':')[0].strip()
                else:
                    user_id, rating, _ = line.strip().split(',')
                    user_ratings_count[user_id] += 1
                    if user_ratings_count[user_id] <= exact_rating_count:
                        user_ratings[user_id][current_movie_id] = int(rating)

    # Identify users who rated exactly 'exact_rating_count' movies
    target_users = [user for user, count in user_ratings_count.items(
    ) if count == exact_rating_count]
    num_target_users = len(target_users)

    # Find the lowest user ID and their 5-star movies
    five_star_movies = []
    if target_users:
        lowest_user_id = str(min(map(int, target_users)))
        five_star_movies = [movie_titles[movie_id] for movie_id,
                            rating in user_ratings[lowest_user_id].items() if rating == 5]

    return num_target_users, five_star_movies


file_path_1 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_1.txt"
file_path_2 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_2.txt"
file_path_3 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_3.txt"
file_path_4 = "/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/combined_data_4.txt"
rating_files = [file_path_1, file_path_2, file_path_3, file_path_4]

movie_titles_file = '/Users/xmeng/Documents/NEUsp24/CS6620_Data_Mining/netflix-data/movie_titles.csv'

num_target_users, five_star_movies = process_data(
    rating_files, movie_titles_file, 200)
print(f"Number of users who rated exactly 200 movies: {num_target_users}")
print("\nMovies rated 5 stars by the user with the lowest ID:")
for movie in five_star_movies:
    print(movie)
