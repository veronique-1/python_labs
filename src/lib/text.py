def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
        
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
        
    return ' '.join(text.split())

#-----------------------------------------------------------------------------
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

#-----------------------------------------------------------------------------
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError
    return sorted(freq.items(), key = lambda x: (-x[1], x[0]))[:n]


if __name__ == '__main__':
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"bb": 2, "aa": 2, "cc": 1}
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
    
print("Все тесты пройдены!")

