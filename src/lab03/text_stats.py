import sys
import os

# Добавляем папку src в пути поиска, чтобы работал импорт lib.text
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.text import normalize, tokenize, count_freq, top_n

def main():
    
    text = sys.stdin.read()
    
    if text.strip() == '':
        raise ValueError('Не был введен текст')
        
    beauty = 1 # Переменная, определяющая красивый вид (сами меняем)

    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    total_words = len(tokens)
    
    freq = count_freq(tokens)
    unique_words = len(freq)
    
    top5 = top_n(freq, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print(f"Топ-5:")

    if not beauty: # обычный вывод
        for word, count in top5:
            print(f"{word}:{count}")
            
    else: # красивый вывод
        if not top5: 
            print('Нет слов для отображения')
        else:
            max_len = max(max([len(word[0]) for word in top5]), len('слово'))
            
            head = f"{'слово':<{max_len}} | частота"
            print(head)
            print('-' * len(head))
            
            for word, count in top5:
                print(f'{word:<{max_len}} | {count}')
            print('...')

if __name__ == "__main__":
    main()