import re

with open("input.txt") as file:
    passport_list = file.read().strip().split('\n\n')

REQUIRED_ENTRIES = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports_counter = 0

for passport in passport_list:
    cleaned_passport = re.split(' |\n', passport)
    entry_counter = 0
    for entry in cleaned_passport:
        entry_list = entry.split(':')
        entry_key = entry_list[0]
        if entry_key in REQUIRED_ENTRIES:
            entry_counter += 1
    if entry_counter >= 7:
        valid_passports_counter += 1


print(valid_passports_counter)



