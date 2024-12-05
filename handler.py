import requests
import os
from cookie import cookie


year = '2024'

def create_day(day_number):
    s = requests.session()
    s.cookies.set("session", cookie, domain="adventofcode.com")

    r = s.get(f'https://adventofcode.com/%7Byear%7D/day/%7Bday_number%7D/input')

    newpath = rf'day{day_number}/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

        with open(f'day{day_number}/input.txt', 'w', newline='') as file:
            file.write(r.text)

        file = open(f'day{day_number}/example.txt', 'w', newline='')

        for i in range(2):
            with open(f'day{day_number}/part{i+1}.py', 'w', newline="") as file:
                file.write(rf'''#MSG: Automatisch generiert | Tag {day_number} | https://adventofcode.com/%7Byear%7D/day/%7Bday_number%7D

import handler as h

file_path = 'input.txt'
with open(file_path, "r") as file:
    file_content = file.read()

lines_full = file_content.split("\n")

file_path = 'example.txt'
with open(file_path, "r") as file:
    file_content = file.read()

lines_example = file_content.split("\n")

Code start hier - -''')
    print(rf'Tag {day_number} im Advent Of Code {year} hinzugefügt')

create_day(6)