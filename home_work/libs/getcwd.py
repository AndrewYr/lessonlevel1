import os
def main() :
    answer = ''
    while answer != 'q':
        answer = input("Узнать все папки в текущей директории? (Y/N/q)")
        if answer == 'Y':
            getcwd(True,os.getcwd())
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")
def getcwd(folder,getcwd):

    for file_name in os.listdir(getcwd):
        if folder:
            # как можно было по другому проверить на файл?
            if file_name.find('.') == -1:
                print(file_name)
        else:
            print(file_name)
os.listdir()[0].find('.')
if __name__ == '__main__':
    main()

