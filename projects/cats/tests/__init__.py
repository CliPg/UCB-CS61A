"Utility functions for file and string manipulation"

import string
from math import sqrt

############################
# String utility functions #
############################

def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def remove_punctuation(s):
    """Return a string with the same contents as s, but with punctuation removed.

    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    >>> remove_punctuation("Its a lovely day dont you think")
    'Its a lovely day dont you think'
    """
    punctuation_remover = str.maketrans('', '', string.punctuation)
    return s.strip().translate(punctuation_remover)

def lower(s):
    """Return a lowercased version of s.

    >>> lower("HELLO")
    'hello'
    >>> lower("World")
    'world'
    >>> lower("hello WORLD")
    'hello world'
    """
    return s.lower()

def split(s):
    """Return a list of words contained in s, which are sequences of characters
    separated by whitespace (spaces, tabs, etc.).

    >>> split("It's a lovely day, don't you think?")
    ["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
    """
    return s.split()

#############################
# Keyboard layout functions #
#############################

KEY_LAYOUT = [["1","2","3","4","5","6","7","8","9","0","-","="],
              ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p","[","]"],
              ["a", "s", "d", "f", "g", "h", "j", "k", "l",";","'"],
              ["z", "x", "c", "v", "b", "n", "m",",",".","/"],
              [" "]]

def distance(p1, p2):
    """Return the Euclidean distance between two points

    The Euclidean distance between two points, (x1, y1) and (x2, y2)
    is the square root of (x1 - x2) ** 2 + (y1 - y2) ** 2

    >>> distance((0, 1), (1, 1))
    1.0
    >>> distance((1, 1), (1, 1))
    0.0
    >>> round(distance((4, 0), (0, 4)), 3)
    5.657
    """
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def get_key_distances():
    """Return a new dictionary mapping key pairs to distances.

    Each key of the dictionary is a tuple of two
    letters as strings, and each value is the euclidean distance
    between the two letters on a standard QWERTY keyboard, normalized

    The scaling is constant, so a pair of keys that are twice
    as far have a distance value that is twice as great

    >>> distances = get_key_distances()
    >>> distances["a", "a"]
    0.0
    >>> round(distances["a", "d"],3)
    1.367
    >>> round(distances["d", "a"],3)
    1.367
    """
    key_distance = {}

    def compute_pairwise_distances(i, j, d):
        for x in range(len(KEY_LAYOUT)):
            for y in range(len(KEY_LAYOUT[x])):
                l1 = KEY_LAYOUT[i][j]
                l2 = KEY_LAYOUT[x][y]
                d[l1, l2] = distance((i, j), (x, y))

    for i in range(len(KEY_LAYOUT)):
        for j in range(len(KEY_LAYOUT[i])):
            compute_pairwise_distances(i, j, key_distance)

    max_value = max(key_distance.values())
    return {key : value * 8 / max_value for key, value in key_distance.items()}

def count(f):
    """Keeps track of the number of times a function f is called using the
    variable call_count

    >>> def factorial(n):
    ...     if n <= 1:
    ...         return 1
    ...     return n * factorial(n - 1)
    >>> factorial = count(factorial)
    >>> factorial(5)
    120
    >>> factorial.call_count
    5
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

###########################
# Miscellaneous functions #
###########################

def deep_convert_to_tuple(sequence):
    """Deeply converts tuples to lists.
    >>> deep_convert_to_tuple(5)
    5
    >>> deep_convert_to_tuple([2, 'hi'])
    (2, 'hi')
    >>> deep_convert_to_tuple([['These', 'are', 'all'], ['tuples.']])
    (('These', 'are', 'all'), ('tuples.',))
    """
    if isinstance(sequence, list) or isinstance(sequence, tuple):
        return tuple(deep_convert_to_tuple(item) for item in sequence)
    else:
        return sequence

#test

def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selected_paragraphs = [p for p in paragraphs if select(p)]
    
    if k < len(selected_paragraphs):
        return selected_paragraphs[k]
    else:
        return ""

def about(subject):
    """
    功能:返回一个函数,即select标准,标准是文段中是否出现关键词
    """
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def related(ps):#ps是文段中的一个项
        for sub_item in subject:
            for ps_item in split(remove_punctuation(ps)):
                if sub_item == lower(ps_item):
                    return True
    return related

def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    score = 100.0
    #遍历
    for n in range(len(typed_words)):
        #长度
        if len(typed_words) > len(source_words):
                score = 50.0
        if typed_words[n] != source_words[n]:
            #大小写
            if lower(typed_words[n]) == lower(source_words[n]):
                score = 50.0
            #标点
            elif remove_punctuation(lower(typed_words[n])) ==remove_punctuation(lower(source_words[n])):
                score = 50.0
            else:
                score = 0.0
                break
    #判断typed_words是否为空
    if len(typed_words) == 0:
        if len(source_words) != 0:
            score = 0.0
    return score

def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)/5.0/elapsed*60
    # END PROBLEM 4

ps = ['hi', 'how are you?', 'fine']
s = lambda p: len(p) <= 4
print(pick(ps, s, 2))
print(len(ps[1]))
print(remove_punctuation(ps[1]).split())
about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
print(pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 1))
print(ps[0][0])
print(split('cute Dog.'))
print(accuracy('', ''))
print(wpm('hello friend hello buddy hello', 15))