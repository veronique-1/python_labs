def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
        
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
        
    return ' '.join(text.split())

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

#-----------------------------------------------------------------------------
import re

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))
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

print(count_freq(["a","b","a","c","b","a"]))
print(top_n(count_freq(["a","b","a","c","b","a"]), n=2))
print()
print(count_freq(["bb","aa","bb","aa","cc"]))
print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2))
