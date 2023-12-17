# Notes

**Remember:lab05两个可选题还不会做 **

**1.列表推导式**

列表推导式是一种简洁的方式，用于从一个可迭代的对象（比如 `range`、列表、字符串等）创建一个新的列表。

在你提供的代码中：

```
pythonCopy code
all_dices = [dice() for i in range(num_rolls)]
```

这个列表推导式的结构是：

```
pythonCopy code
[expression for item in iterable]
```

具体到你的例子：

- `expression` 是 `dice()`，表示在每次迭代中调用 `dice()` 函数并将其结果作为列表的一个元素。
- `for i in range(num_rolls)` 表示迭代 `range(num_rolls)` 中的每个元素，但在代码中并没有使用 `i` 这个变量，因为它只是一个计数器。
- 整个表达式创建了一个列表，其中包含了 `num_rolls` 次调用 `dice()` 函数的结果。

这种写法在很多情况下都比使用传统的 `for` 循环和 `append` 操作更为简洁，并且通常更容易阅读。

**2.分割数**

求正整数 n 的分割数，最大部分为 m，即 n 可以分割为不大于 m 的正整数的和，并且按递增顺序排列。例如，使用 4 作为最大数对 6 进行分割的方式有 9 种。



```
1.  6 = 2 + 4
2.  6 = 1 + 1 + 4
3.  6 = 3 + 3
4.  6 = 1 + 2 + 3
5.  6 = 1 + 1 + 1 + 3
6.  6 = 2 + 2 + 2
7.  6 = 1 + 1 + 2 + 2
8.  6 = 1 + 1 + 1 + 1 + 2
9.  6 = 1 + 1 + 1 + 1 + 1 + 1
```

我们将定义一个名为 `count_partitions(n, m)` 的函数，该函数返回使用 `m` 作为最大部分对 n 进行分割的方式的数量。这个函数有一个使用树递归的简单的解法，它基于以下的观察结果：

使用最大数为 m 的整数分割 n 的方式的数量等于

1. 使用最大数为 m 的整数分割 n-m 的方式的数量，加上
2. 使用最大数为 m-1 的整数分割 n 的方式的数量

要理解为什么上面的方法是正确的，我们可以将 n 的所有分割方式分为两组：至少包含一个 m 的和不包含 m 的。此外，第一组中的每次分割都是对 n-m 的分割，然后在最后加上 m。在上面的实例中，前两种拆分包含 4，而其余的不包含。

因此，我们可以递归地将使用最大数为 m 的整数分割 n 的问题转化为两个较简单的问题：① 使用最大数为 m 的整数分割更小的数字 n-m，以及 ② 使用最大数为 m-1 的整数分割 n。

为了实现它，我们需要指定以下的基线情况：

1. 整数 0 只有一种分割方式
2. 负整数 n 无法分割，即 0 种方式
3. 任何大于 0 的正整数 n 使用 0 或更小的部分进行分割的方式数量为 0

py

```
>>> def count_partitions(n, m):
        """计算使用最大数 m 的整数分割 n 的方式的数量"""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m-1)

>>> count_partitions(6, 4)
9
>>> count_partitions(5, 5)
7
>>> count_partitions(10, 10)
42
>>> count_partitions(15, 15)
176
>>> count_partitions(20, 20)
627
```

我们可以将树递归函数视为探索不同的可能性。在这种情况下，我们探讨了使用大小为 m 的部分以及不使用这部分的可能性。第一次和第二次递归调用即对应着这些可能性。

**3.回文**

eg.

```python
def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    return reduce(lambda x, y: x + y, map(lambda word: 1 if word.lower() == word.lower()[::-1] else 0, L), 0)
```

``reduce` 是 Python 中 `functools` 模块提供的一个函数，它用于对一个序列的元素进行累积操作。具体用法为：

```
pythonCopy codefrom functools import reduce

result = reduce(function, sequence, initializer)
```

这里的参数含义如下：

- `function`: 一个具有两个参数的函数，用于对序列中的元素进行累积操作。
- `sequence`: 要进行累积操作的可迭代对象，如列表、元组等。
- `initializer` (可选): 初始值，如果提供了初始值，则会作为第一次调用累积函数时的第一个参数。如果不提供初始值，则第一次调用时使用序列的前两个元素。

以下是一个例子，演示如何使用 `reduce` 计算一个序列中所有元素的累积：

```
pythonCopy codefrom functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce 计算累积
product = reduce(lambda x, y: x * y, numbers)

print(product)
```

在这个例子中，`lambda x, y: x * y` 是一个匿名函数，用于对两个参数进行相乘操作。`reduce` 函数将这个函数应用于序列 `numbers` 中的所有元素，得到它们的累积乘积。在这里，初始值没有提供，因此第一次调用时使用了序列的前两个元素。

1. `lambda word: 1 if word.lower() == word.lower()[::-1] else 0`: 这是一个匿名函数，接受一个参数 `word`。这个函数返回 `1` 如果 `word` 是回文（忽略大小写），否则返回 `0`。

   - `word.lower()`: 将单词转换为小写，确保大小写不影响回文检查。
   - `word.lower()[::-1]`: 将转换为小写的单词反转。

   所以，这个 lambda 函数实际上在检查给定的单词是否是回文。

   **每个word实际上是一个数组**

2. `map(lambda word: 1 if word.lower() == word.lower()[::-1] else 0, L)`: `map` 函数将这个 lambda 函数应用于序列 `L` 中的每个元素。对于每个单词，如果它是回文，映射的结果就是 `1`，否则是 `0`。

**4.Dictionaries**

- 格式：

  ```python
  >>> artists = {
  ...    'Ariana Grande': 'No Tears Left To Cry',
  ...    'Marshmello': 'FRIENDS',
  ...    'Migos': ['Stir Fry', 'Walk It Talk It']
  ... }
  ```

- 调用：

  ```python
  >>> artists['Ariana Grande']
  'No Tears Left To Cry'
  >>> songs = artists['Migos']
  >>> songs[0]
  'Stir Fry'
  ```

  

- 冒号左边是键 右边是值

- 键要唯一，且只能是不可变类型（例如字符串、数字、元组）。 不能使用列表作为键

- `dict.keys()`将返回一系列键。

  ```
  >>> list(artists.keys()) # We use list() to turn the sequence into a list
  ['Ariana Grande', 'Marshmello', 'Migos', 'Charlie Puth']
  ```

- `dict.values()`将返回一个值序列。

  ```
  >>> list(artists.values())
  ['No Tears Left To Cry', 'Wolves', ['Stir Fry', 'Walk It Talk It'], 'Attention']
  ```

- `dict.items()`将返回键值元组序列。

  ```
  >>> list(artists.items())
  [('Ariana Grande', 'No Tears Left To Cry'),
   ('Marshmello', 'Wolves'),
   ('Migos', ['Stir Fry', 'Walk It Talk It']),
   ('Charlie Puth', 'Attention')]
  ```

**5.树**

- eg.

  ```python
  number_tree = tree(1,
           [tree(2),
            tree(3,
                 [tree(4),
                  tree(5)]),
            tree(6,
                 [tree(7)])])
  ```

   

  ```
     1
   / | \
  2  3  6
    / \  \
   4   5  7
  ```

   

- 构造函数
  - `tree(label, branches=[])`：label赋有树存储的值,branches是列表，即树的分支，每个分支也是一棵树
- 选择器
  - `label(tree)`：返回`tree`根节点中的值。
  - `branches(tree)`：返回给定树的分支列表（每个分支也是一棵树）
- 便利功能
  - `is_leaf(tree)`：叶子节点：只有值，没有分支，若该树是叶子节点，则返回true
  - label(branches(number_tree)[1])

branches（）返回number_tree的分支列表，[1]表示这个列表的第二个项目，label（）返回这个节点的值