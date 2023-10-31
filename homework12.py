import os

os.mkdir("Harry Potter")

from HomeWork12.films_titles import films_titles
# Створення піддиректорій на основі назв фільмів
for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_directory = os.path.join("Harry Potter", film_title)
    os.mkdir(film_directory)
    print(f"Створено дерикторію '{film_title}'")

import string

for film in films_titles["results"]:
    film_title = film["title"].replace(":", "")
    film_directory = os.path.join("Harry Potter", film_title)

    # Створення тек від A до Z
    for letter in string.ascii_uppercase:
        letter_directory = os.path.join(film_directory, letter)
        os.mkdir(letter_directory)
        print(f'Дерикторію "{letter_directory}" створено.')

print('Усі теки створені від A до Z в кожній піддиректорії фільму.')

from HomeWork12.films_awards import *

film_awards_list = []

for film_award in films_awards[0]['results']:
    award_info = {
        'type': film_award['type'],
        'award_name': film_award['award_name'],
        'award': film_award['award']

    }
    film_awards_list.append(award_info)

for i, film_awards in enumerate(film_awards_list):
    print([film_awards])

sorted_film_awards = sorted(film_awards_list, key = lambda film: film['award_name'])

film_folder = film_title


for film_award in sorted_film_awards:
    award_name = film_award['award_name']
    award_letter = award_name[0].upper()


    letter_directory = os.path.join(film_folder, film_award['award_name'][0].upper())


    if not os.path.exists(letter_directory):
        os.makedirs(letter_directory)

    file_path = os.path.join(letter_directory, f"{award_name}.txt")
    with open(file_path, 'w') as award_file:
        award_file.write(f"Award Name: {film_award['award_name']}\n")
        award_file.write(f"Award Type: {film_award['type']}\n")
        award_file.write(f"Award: {film_award['award']}\n")

print('Усі файли створені успішно.')









