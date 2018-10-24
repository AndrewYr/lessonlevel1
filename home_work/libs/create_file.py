import os
def main() :
    answer = ''
    while answer != 'q':
        answer = input("Создать директории? (Y/N/q)")
        if answer == 'Y':
            i = 1
            while i < 10:
                create_file('dir_{}'.format(i))
                i += 1
        elif answer == 'N':
            print("До свидания!")
        else:
            print("Неизвестный ответ")

def create_file(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('Директория dir_{} создана'.format(name))
    except FileExistsError:
        print('Директория dir_{} уже существует'.format(name))


if __name__ == '__main__':
    main()

