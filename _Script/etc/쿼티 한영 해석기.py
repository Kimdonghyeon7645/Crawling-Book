"""
솔직히 언제 영어랑 한글 치냐;; 그래서 리스트 채우는 것도 파이썬 스크립트로 자동화
"""
# en_li = list(input("한글 입력 : "))
# ko_li = list(input("영어 입력 : "))
# print(*zip(ko_li, en_li), sep=", ")

key_li = [
    ('q', 'ㅂ'), ('w', 'ㅈ'), ('e', 'ㄷ'), ('r', 'ㄱ'), ('t', 'ㅅ'),
    ('y', 'ㅛ'), ('u', 'ㅕ'), ('i', 'ㅑ'), ('o', 'ㅐ'), ('p', 'ㅔ'),
    ('a', 'ㅁ'), ('s', 'ㄴ'), ('d', 'ㅇ'), ('f', 'ㄹ'), ('g', 'ㅎ'),
    ('h', 'ㅗ'), ('j', 'ㅓ'), ('k', 'ㅏ'), ('l', 'ㅣ'),
    ('z', 'ㅋ'), ('x', 'ㅌ'), ('c', 'ㅊ'), ('v', 'ㅍ'),
    ('b', 'ㅠ'), ('n', 'ㅜ'), ('m', 'ㅡ')
]
ko_li = [i[1] for i in key_li]
en_li = [i[0] for i in key_li]

for word in input("변환할 문자열을 입력하세요 : "):
    if word in ko_li:
        print(key_li[ko_li.index(word)][0], end='')
    elif word in en_li:
        print(key_li[en_li.index(word)][1], end='')
    else:
        print(word, end='')