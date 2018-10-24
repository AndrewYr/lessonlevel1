import os
import shutil

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = 'clone_' + filename
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

def main() :
    answer = ''
    while answer != 'q':
        answer = input("Клонировать текущий файл? (Y/N/q)")
        if answer == 'Y':
            duplicate_file(os.path.basename(__file__))
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")

if __name__ == '__main__':
    main()

