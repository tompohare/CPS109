""" Analyzes words from a file making use of Python's built-in dictionary data type.
Creates a histogram of word lengths and other descriptive statistics.

From Think Python, Chapter 9 Case study: word play
https://greenteapress.com/thinkpython2/html/thinkpython2010.html
Download https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt
"""

def process_file(filename):
    words = dict()
    fin = open(filename)
    for word in fin:
        word_lengths(word, words)
    return words

def word_lengths(word, words):
    word = word.strip()
    words[word] = len(word)

def no_letter_e(words):
    count = 0
    for word in words:
        if has_no_e(word):
            count += 1
    return count

def has_no_e(word):
    if word.find('e') == -1:
        return True
    return False

def word_len_hist(words):
    hist = dict()
    for word in words:
        if len(word) <= 5:
            hist['1-5'] = hist.get('1-5', 0) + 1
        elif len(word) <= 10:
            hist['6-10'] = hist.get('6-10', 0) + 1
        elif len(word) <= 15:
            hist['11-15'] = hist.get('11-15', 0) + 1
        elif len(word) <= 20:
            hist['16-20'] = hist.get('16-20', 0) + 1
        else:
            hist['21+'] = hist.get('21+', 0) + 1
    return hist

def percentage(number, total):
    return round(100 * float(number) / float(total), 2)

words = process_file('words.txt')
no_e_count = no_letter_e(words)
hist = word_len_hist(words)
print(f'Total words: {len(words):,}')
print(f"Words with no 'e': {no_e_count:,}, percent: {percentage(no_e_count, len(words))}%")
