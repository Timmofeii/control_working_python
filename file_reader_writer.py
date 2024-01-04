count_contacts = 0


def convert_file_to_dict(file_name):
    contacts = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(';')
            contacts[parts[0]] = parts[1:]
    return contacts


count_id = 0


def count_contact(file_name):
    lines = 0
    with open(file_name, 'r') as file:
        for line in file:
            lines += 1
    return lines


def create_new_contact(file_name):
    information = []
    current_id = count_contact(file_name)
    information.append(str(current_id))
    information.append(input("Enter contact name: "))
    information.append(input("Enter contact phone number: "))
    information.append(input("Enter contact group: "))

    with open(file_name, 'a') as file:
        file.write(";".join(information) + '\n')


def find_contact(file_name):
    name = input("Enter name who you need to find ")
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if name in line:
            print(line)


def delete_contact(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')
    id_for_delete = int(input("Enter ind for delete: "))
    if 0 <= id_for_delete <= len(lines):
        del lines[id_for_delete]
    with open(file_name, 'w') as file:
        file.writelines(lines)
    show_contacts(file_name)


# def change_contact_information(file_name):
#     id_change = int(input("Enter id who neaded to changes info: "))
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#         new_info=[input("enter name"),input("enter number") ,input("enter group")]
#         if 0<= id_change<len(lines):
#             for line in range(0,len(lines),1):
#                 if lines[line].split(';')[0] == str(id_change):
#                     lines[line].split()[1:]=';'.join(new_info)+'\n'
#                     with open( file_name,'w')as file:
#                         file.writelines(lines)
def change_contact_information(file_name):
    id_change = input("Enter id who needs to change info: ")
    new_info = [input("Enter name: "), input("Enter number: "), input("Enter group: ")]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            parts = line.strip().split(';')
            if parts[0] == id_change:
                lines[index] = f"{id_change};{';'.join(new_info)}\n"
                break  # После обновления строки, можно выйти из цикла

        with open(file_name, 'w') as file:
            file.writelines(lines)

        # for i in range(0,len(lines),1):
        #     print(lines[i].split())


def copy_line_iN_another_file(form_copy_file,in_copy_file):
    number_string=int(input("Enter number string, what you want to copy "))-1
    with open(form_copy_file,'r') as file:
        lines=file.readlines()

        with open(in_copy_file,'a') as file:
            file.write(lines[number_string]+ '\n')

def show_contacts(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')

