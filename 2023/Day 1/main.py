import sys

# adding first and last chars of the written number to avoid deleting overlapping chars
# between written numbers
written_numbers = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def get_numeric(word):
    ini = None
    fin = None

    for c in word:
        if c.isnumeric():
            ini = c
            break
    
    for c in word[::-1]:
        if c.isnumeric():
            fin = c
            break
    
    ini = '0' if ini is None else ini
    fin = '0' if fin is None else fin

    return int(ini+fin)

def translate_text_into_numbers(words):
    new_words = []

    for word in words:
        new_word = word
        for text, num in written_numbers.items():
            new_word = new_word.replace(text, num)
        new_words.append(new_word)
    
    return new_words

def part1(words):
    return sum([get_numeric(word) for word in words])

def part2(words):
    new_words = translate_text_into_numbers(words)
    return part1(new_words)

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2] if len(sys.argv)>2 else sys.argv[1]

    words_p1 = open(file1, "r").read().split("\n")
    words_p2 = open(file2, "r").read().split("\n")

    print(part1(words_p1))
    print(part2(words_p2))