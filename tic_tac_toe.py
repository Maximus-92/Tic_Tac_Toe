import time
import sys
import random


# n_dim = None

def my_custom_print(text: str, delay=0.0005):
    '''
    Функция создающая тайпинг-эффект (просто выебнуться)

    Аргументы:
        text(str): непосредственно что выводим
        delay(float): задержка в секундах
    '''
    for single_character in text:
        sys.stdout.write(single_character)
        sys.stdout.flush()
        time.sleep(delay)





def greetings():
    '''
    Небольшая необязательная функция которая просто выводит приветственное сообщение для юзера.
    '''

    my_custom_print(
        """
        ДОБРО ПОЖАЛОВАТЬ В ИГРУ

    Ты запустил АГРЕССИВНЫЕ КРЕСТИКИ-НОЛИКИ созданные за пару часов на коленке.
    Игра была создана как ответ на брошенный вызов товарища.
    
    
    ПРАВИЛА ВЗАИМОДЕЙСТВИЯ С СИЕМ ТВОРЕНИЕМ:
    
    - Введи число которое определит размеры поля (формат n*n)
    - Минимальный размер поля 3*3
    - Максимальный размер 9*9 (больше делать нет смысла)
    - Определись ты за крестики или нолики
    - Постарайся не проиграть
    - Если найдёшь баг - поздравляю, ты обнаружил единственную ошибку во Вселенной, созданную исключительно для того, чтобы дать тебе ложную надежду
    - Если проиграешь - твой компьютер сам откроет калькулятор и предложит посчитать, сколько раз ты сегодня разочаровал человечество
    - Если выиграешь - тебе просто повезло\n
        """
        )





def create_table() -> list:
    '''
    Задаем настройки и размер таблицы (может быть любых размеров, удобно для генерализации).
    Функция сама запросит число n, создаст и вернет таблицу размером n*n в виде списка
    '''   
    
    random_response_to_numerical_mistakes = [
    "\nЧисло, блядь. Просто число. Больше двух",
    "\nТы калькулятор сломать пытаешься?",
    "\nМозг включи. Хотя бы на минималках.",
    "\nЭто неправильное число, гений. Попробуй ещё раз",
    "\nЯ просил нормальное число, лох",
    "\nОшибка ввода. Ты конченый? Еще раз условия повторить?",
    "\nПиздец. Нет слов...",
    "\nНеверный ввод. Ты думал я дебил и не поставлю проверку ввода?",
    "\nВведи верное число, лох. Ты не пройдешь дальше пока не введешь нормальное число"
    ]
    
    
    while True:
        try:
            my_custom_print('\nВведи размер поля числом: ')
            
            global n_dim
            n_dim = int(input())
            
            if not 3 <= n_dim <= 9:
                raise ValueError
            
            my_custom_print('\nФух....Ты знаешь цифры и умеешь читать правила, горжусь тобой\n')
            break
        except ValueError:
            print(random.choice(random_response_to_numerical_mistakes))

    
    # зададим список заполненный единицами - так как он изменяемый тип, буду менять потом на х и о (просто нули на о похожи, бесит, поэтому единицы)
    # я ленивый, поэтому сделаю list comprehension
    generated_table = [[1 for y in range(n_dim)] for x in range(n_dim)]
    return generated_table
    





def player_assignment():
    '''
    Тут настраиваем наших игроков и закрепляем за ними символы
    '''   
    
    random_response_to_symbol_mistakes = [
    "\nБудь человеком. Или 'x', или 'o' ",
    "\nТы это по приколу делаешь или как? условия читал?",
    "\nЯ ж написал...'x' или'o'. Не нужно тут устраивать свои тесты",
    "\nЭто неправильный значок, гений. Попробуй ещё раз",
    "\nЯ просил нормальный символ, лошара",
    "\nОшибка ввода. Ты конченый? Еще раз условия повторить?",
    "\nПиздец. Нет слов...",
    "\nНеверный ввод. Ты по ходу слепой",
    "\nВведи верный символ, молю всех богов. Ты ж не пройдешь дальше пока не введешь правильно"
    ]
    
    
    while True:
        try:
            my_custom_print('\nНапиши какой символ хочешь на английской клавиатуре (формат ввода: x или o): ')
            global player_symbol
            player_symbol = input().lower()
            
            if player_symbol not in ('x', 'o'):
                raise ValueError
            
            my_custom_print('\nОтлично, едем дальше...\n')
            break
        except ValueError:
            print(random.choice(random_response_to_symbol_mistakes)) 





def your_arch_nemesis(player_symbol):
    '''
    Создадим соперника-компа и отдадим ему оставшийся символ
    '''
    global arch_enemy_symbol
    arch_enemy_symbol = 'o' if player_symbol == 'x' else 'x'
    return arch_enemy_symbol





def player_combinations():   
    player_one_win_combination = ['x' for x in range(n_dim)]
    player_two_win_combination = ['o' for x in range(n_dim)]
    return player_one_win_combination, player_two_win_combination




def move_checker(comb_1:list, comb_2:list, table:list) -> bool:  
    '''
    Задача у этой функции проверить что есть выигрышная комбинация и вернуть True или False.
    В зависимости от результата игра либо продолжается, либо прекращается.
    '''
    
    # создаем список строк с горизонтальными комбинациями
    row_list = table

    # создаем список с вертикальными комбинациями
    column_list = []
    for i in range(n_dim):
        current_column = [row[i] for row in table]
        column_list.append(current_column)

    # создаем список с диагональными комбинациями
    first_diagonal_list = [table[i][i] for i in range(n_dim)]
    second_diagonal_list = [table[i][n_dim - 1 - i] for i in range(n_dim)]

    # теперь создадим список со всем комбинациями что сейчас есть в игре, чтоб потом удобно было по ним пробегаться и сравнивать
    combined_list = column_list + row_list
    combined_list.append(first_diagonal_list)
    combined_list.append(second_diagonal_list)
    
    # проверка на выигрыш - возвращаем Тру или Фолс
    return True if comb_1 in combined_list or comb_2 in combined_list else False




def print_the_board(table):
    '''
    Функция выводит на экран поле и каждый раз оно будет обновляться и показывать где крестики и нолики
    '''
    n_dim = len(table)
    print('  ' * n_dim)
    my_custom_print('Введи координаты клетки, куда хочешь поставить крестик или нолик (ряд и колонку) без пробела\n')
    print('  ' * n_dim)
    line = '  ' + '----' * n_dim + '-'

    print('    ' + '   '.join(str(i + 1) for i in range(n_dim)))
    
    # вывести всю таблицу по размерам
    for i, row in enumerate(table):
        print(line)
        cells = [' ' if cell == 1 else cell for cell in row]
        print(f'{i + 1} | ' + ' | '.join(cells) + ' |')

    print(line)







def player_makes_move(table, symbol):
    '''
    Правила хода для игрока с проверкой (а то еще поставишь какую нить ерунду, да еще и не туда)
    '''
    while True:
        move = input(f'Игрок {symbol}, введи координаты (например, 12): ')

        if len(move) != 2 or not move.isdecimal():
            my_custom_print('Хоспаде. Введи ровно две цифры!\n')
            continue

        row = int(move[0]) - 1
        col = int(move[1]) - 1

        if not (0 <= row < n_dim and 0 <= col < n_dim):
            my_custom_print('Мимо. Давай еще раз\n')
            continue

        if table[row][col] != 1:
            my_custom_print('Клетка занята, не видишь что ли?\n')
            continue

        table[row][col] = symbol
        return






def enemy_makes_move(table, symbol, n_dim):
    '''
    Соперник рандомно смотрит на числа в таблице и если это единица (т.е. свободная клетка), то ставит туда свой символ
    '''
    while True:
        x = random.randint(0, n_dim - 1)
        y = random.randint(0, n_dim - 1)
        
        if table[x][y] == 1:
            table[x][y] = symbol
            break
    # print_the_board(table)

    

def who_starts_first():
    '''
    Ну тут просто, надо просто подкинуть монетку и решить кто ходит первым.
    Не переживай, я решу за тебя
    '''
    two_options = [0, 1]
    
    # эта переменная нам потом пригодиться для того, чтоб определиться в какой последовательности ходим
    global starter
    
    # можно по разному выбрать рандом, я решил че то так пойти
    if random.choice(two_options) == 0:
        print('\nПервым ходит твой соперник')
        starter = 0
        enemy_makes_move(main_table, arch_enemy_symbol, n_dim)
    else:
        print('\nТы ходишь первым')
        starter = 1
        print_the_board(main_table)
        player_makes_move(main_table, player_symbol)



# если ничья, то надо как то завершить игру
def if_board_full(table):
    return all(cell != 1 for row in table for cell in row)




def final_board_view(table):
    print('\n' * 3)
    my_custom_print('\n_______ИГРА ЗАВЕРШЕНА_______\n')
    if starter == 1:
        my_custom_print('Тебе просто повезло сегодня...')
    elif starter == 0:
        my_custom_print('Твой соперник тебя уделал')
    else:
        my_custom_print('Ничья. Случайное везенье, не более')
    
    print('\n' * 2)
    n_dim = len(table)
    print('  ' * n_dim)
    line = '  ' + '----' * n_dim + '-'

    print('    ' + '   '.join(str(i + 1) for i in range(n_dim)))
    
    # вывести всю таблицу по размерам
    for i, row in enumerate(table):
        print(line)
        cells = [' ' if cell == 1 else cell for cell in row]
        print(f'{i + 1} | ' + ' | '.join(cells) + ' |')

    print(line)










if __name__ == "__main__":
    # тут основная последовательность включений функций
    # пропускаю через try/except чтоб словить исключения
    try:
        greetings()
        main_table = create_table()
        player_assignment()
        your_arch_nemesis(player_symbol)
        player_one, player_two = player_combinations()

        # тут уже начинается сама игра
        who_starts_first()

        # короче пока нет выигрышного паттерна - продолжаем играть
        while move_checker(player_one, player_two, table=main_table) == False:
            if if_board_full(main_table):
                starter = 2
                break
            print_the_board(main_table)
            if starter == 1:                       # вот она и пригодилась, можно ее потом обновить и определить порядок ходов
                enemy_makes_move(main_table, arch_enemy_symbol, n_dim)
                starter = 0
            else:
                player_makes_move(main_table, player_symbol)
                starter = 1


        final_board_view(main_table)

    except (KeyboardInterrupt, EOFError):
        print('\n\nТы прервал игру, слабак. Возвращайся, когда будешь готов проиграть')
        sys.exit(0)










