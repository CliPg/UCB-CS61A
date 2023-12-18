def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(s)):
        if s[i] == before:
            s.append(s[len(s)-1])
            for i in range(len(s)-1,i+1,-1):
                s[i] = s[i-1]
            s[i-1] = after
    return s

def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(s, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(s)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    total = 0
    while count < n:
        value = next(t)
        if value == x:
            total += 1
        count += 1
    return total

def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    occur_elem = []
    occur_nums = []
    try:
        while True:
                value = next(t)
                if not value in occur_elem:
                    occur_elem.append(value)
                    occur_nums.append(1)
                else:
                    for i in range(len(occur_elem)):
                        if occur_elem[i] == value:
                            occur_nums[i] += 1
                    for i in range(len(occur_nums)):
                        if occur_nums[i] == k:
                            return occur_elem[i]
    except StopIteration:
        pass

def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    helper = s[start:]
    for i in range(len(helper)):
        s[i+start] = helper[len(helper)-i-1]

test_s = [1, 5, 8, 5, 2, 3]
print(test_s)
new_s = insert_items(test_s, 5, 7)
print(new_s == test_s)
s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(count_occurrences(s2, 3, 10))
s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
print(repeated(s2, 3))
print(repeated(s2, 3))
a = [1, 2, 3, 4, 5, 6, 7]
partial_reverse(a, 2)
partial_reverse(a, 5)
print(a)
