from pprint import pprint
from typing import Tuple
import random


def create_word_table(row: int, col: int) -> list[list[str]]:
    table = [['' for _ in range(col)] for _ in range(row)]
    return table

def insert_word(word: str, word_table: list[list[str]], word_len_max: int) -> Tuple[list[list[str]], list[list[int]]]:
    # ワードを代入する関数
    # 不正な文字列validation
    if type(word) != str:
        raise ValueError("word_type_validate_error!")
    # 文字数カウントvalidation
    if len(word) > word_len_max:
        raise ValueError("word_size_validate_error!")
    
    if False:
        # TODO 文字が重なっていたら, 重ねて挿入できるかを試す.
        pass
    else: 
        insert_end_flag = 0
        while (insert_end_flag < 10):
            pos_list = [[i, j] for j in range(len(word_table[0])) for i in range(len(word_table))]
            rand_pos = random.choice(pos_list)
            rand_pos_o = random.choice([[rand_pos[0]+len(word),rand_pos[1]], [rand_pos[0],rand_pos[1]+len(word)]])
            if rand_pos[0] == rand_pos_o[0]:
                _flag = 0
                for i in range(len(word)):
                    if rand_pos[1]+len(word) > len(word_table[0]):
                        _flag = 1
                        break
                    elif word_table[rand_pos[0]][rand_pos[1]+i] != '':
                        _flag = 1
                        break
                if _flag == 0:
                    for i in range(len(word)):
                        word_table[rand_pos[0]][rand_pos[1]+i] = word[i]
                        insert_end_flag += 10

            elif rand_pos[1] == rand_pos_o[1]:
                _flag = 0
                for i in range(len(word)):
                    if rand_pos[0]+len(word) > len(word_table):
                        _flag = 1
                        break
                    elif word_table[rand_pos[0]+i][rand_pos[1]] != '':
                        _flag = 1
                        break
                if _flag == 0:
                    for i in range(len(word)):
                        word_table[rand_pos[0]+i][rand_pos[1]] = word[i]
                        insert_end_flag += 10
            insert_end_flag += 1

    word_pos = [[1,2], [5,9]]
    return word_table, word_pos

def fill_empty(word_table: list[list[str]]) -> list[list[str]]:
    # 空の文字をランダムに埋める
    katakana = [chr(i) for i in range(ord("ァ"), ord("ン")+1)]
    for y in range(len(word_table)):
        for x in range(len(word_table[0])):
            if word_table[y][x] == '':
                word_table[y][x] = random.choice(katakana)
            
    return word_table


if __name__ == "__main__":
    # TODO add input word list
    word_list = ['オオカミ', 'ライオン', 'タマリン', 'カワウソ', 'ヤマネコ', 'イヌ', 'ネコ', 'ネズミ']
    print('input table sise (ex. {row} {col})')
    table_size_row, table_size_col = map(int, input().split())
    word_table = create_word_table(table_size_row, table_size_col)
    print('input word (ex. {word_size})')
    word_size = int(input())
    insert_word('オオカミ', word_table, word_size)
    insert_word('ライオン', word_table, word_size)
    insert_word('タマリン', word_table, word_size)
    pprint(fill_empty(word_table))

