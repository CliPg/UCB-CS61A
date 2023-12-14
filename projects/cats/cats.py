"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime

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
    去除字符串的标点并返回
    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    >>> remove_punctuation("Its a lovely day dont you think")
    'Its a lovely day dont you think'
    """
    punctuation_remover = str.maketrans('', '', string.punctuation)
    return s.strip().translate(punctuation_remover)

def lower(s):
    """Return a lowercased version of s.
    返回字符串的小写
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
    将字段的单词分组
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
###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """
    功能:返回文段中符合select标准的项
    """
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
    # END PROBLEM 1


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

    # END PROBLEM 2


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

    # END PROBLEM 3


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
    return len(typed)*12/elapsed
    # END PROBLEM 4


############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.
    diff_function:返回数字
    功能:返回差异最小的单词,但是差异必须在limit内
    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    #将list_word中的元素遍历代入diff_function，得到差异大小的集合，并找到min，在进行一次遍历
    diff_list = [diff_function(typed_word,list_word,limit) for list_word in word_list]
    diff_min = min(diff_list)
    for list_word in word_list:
        if diff_function(typed_word,list_word,limit) == diff_min:
            return list_word
    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if len(typed) == 1 or len(source) == 1:
        if typed[0] == source[0]:
            return 0 + abs(len(typed) - len(source))
        else:
            return 1 + abs(len(typed) - len(source))
    else:
        return feline_fixes(typed[1:],sorted[1:],limit) + feline_fixes(typed[0],source[0],limit)
    # END PROBLEM 6


############
# Phase 2B #
############


def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit < 0: # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    # Recursive cases should go below here
    if len(typed) == 0 or len(source) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return abs(len(typed) - len(source))
        # END
    elif typed[0] == source[0]:
        return minimum_mewtations(typed[1:],source[1:],limit)
    else:
        add = minimum_mewtations(typed,source[1:],limit-1)
        remove = minimum_mewtations(typed[1:],source,limit-1)
        substitute = minimum_mewtations(typed[1:],source[1:],limit-1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 1 + min(add, remove, substitute)
        # END


def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'

FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    for typed_word in typed:
        if typed_word in source:
            count += 1
    upload({'id': user_id, 'progress': count/len(source)})
    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    times = []
    for player in timestamps_per_player:
        tpp = []
        for i in range(len(player) - 1):
            tpp.append(player(i+1) - player(i))
        times.append(tpp)
    return match(words,times)
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    player_0 = []
    player_1 = []
    for i in range(len(get_all_words(match))):
        if get_all_times(match)[0][i] <= get_all_times(match)[1][i]:
            player_0.append(get_all_words(match)[i])
        else:
            player_1.append(get_all_words(match)[i])
    return [player_0,player_1]    

    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)