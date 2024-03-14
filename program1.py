def copy_line(source_file, destination_file, line_number):
    
        with open(source_file, 'r') as f_source:
            lines = f_source.readlines()
            if 0 < line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(destination_file, 'w') as f_dest:
                    f_dest.write(line_to_copy)
                print(f"Строка {line_number} успешно скопирована из {source_file} в {destination_file}")
            else:
                print("Недопустимый номер строки")


source_file = input("Введите имя файла, из которого нужно скопировать: ")
destination_file = input("Введите имя файла, в который нужно скопировать: ")
line_number = int(input("Введите номер строки для копирования: "))
copy_line(source_file, destination_file, line_number)
