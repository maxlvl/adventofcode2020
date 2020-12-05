input_file = open("input.txt","r")

input_dict = {}

for line in input_file:
    line_list = line.split(' ')
    allowed_amounts_list = line_list[0].split('-')
    char = line_list[1].split(':')[0]
    passw = line_list[2].strip()
    input_dict[passw] = [allowed_amounts_list, str(char)]


#{password: [1-3, char]}

valid_password_list = [] 

for element in input_dict:
    values = input_dict[element]
    allowed_amounts = values[0]
    char = values[1]
    split_element = [c for c in element]
    char_count = split_element.count(char)
    if char_count >= int(allowed_amounts[0]) and char_count <= int(allowed_amounts[1]):
        print(f"Valid password detected. Password: {element}")
        valid_password_list.append(element)

print(len(valid_password_list))
