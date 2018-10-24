import libs.getcwd as my_getcwd
import libs.create_file as my_create_file
import os
import re

def main() :

    answer = ''

    while answer != 'q':
        answer = input("Давайте поработаем? (Y/N/q)")
        if answer == 'Y':
            print(" [1] - Перейти в папку")
            print(" [2] - Просмотреть содержимое текущей папки")
            print(" [3] - Удалить папку")
            print(" [4] - Создать папку")
            do = int(input("Укажите номер действия: "))

            if do == 1:
                folder = input("Введите папку в который хотите попасть или * чтобы попасть в родительскую папку")
                if folder != '*':
                    for file_name in os.listdir():
                        if file_name == folder:
                            os.chdir(os.getcwd() + '\\' + folder)
                            print('Перешел')
                            main()
                            break
                    print('Невозможно перейти')
                    main()
                else:
                    os.chdir(os.getcwd())
            elif do == 2:
                print('Текушая директория '+os.getcwd())
                my_getcwd.getcwd(False,os.getcwd())
            elif do == 3:
                folder = input("Введите файл который хотите удалить ")
                for file_name in os.listdir():
                    if file_name == folder:
                        # ошибка, отказано в доступе
                        os.remove(os.path.join(os.getcwd(),folder))
                        print('Успешно удалено')
                        break
                print('Невозможно удалить, такой папки не существует')
            elif do == 4:
                folder = input("Введите файл который хотите создать ")
                for file_name in os.listdir():
                    if file_name == folder:
                        print('Невозможно создать, папка с таким наименованием уже существует')
                        break
                my_create_file.create_file(folder)
                print('Успешно создано')
            else:
                pass
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")

if __name__ == '__main__':
    main()