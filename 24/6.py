def word_min(array_strings):
    min_count = float("inf")
    min_str = ""
    for el in array_strings:
        if min_count >= el.count("A"):
            min_count = el.count("A")
            min_str = el
    return min_str

def word_often_let(str):
    let_table = {}
    min_let = []
    min_count = float("inf")
    for el in str:
        if el not in let_table:
            let_table[el] = str.count(el)
    for key in let_table:
        if let_table[key] < min_count:
            min_count = let_table[key]
            min_let = [key]
        if let_table[key] == min_count:
            min_let.append(key)
    return min_let

f = open("24.txt", "r")
s = f.read().split("\n")
print(word_often_let(word_min(s)))
