# Essential Python Built-in Methods for Work & LeetCode

## String Methods

### `str.split()` and `str.join()`
```python
# Split strings into lists
text = "apple,banana,cherry"
fruits = text.split(',')  # ['apple', 'banana', 'cherry']

# Join lists into strings
result = '-'.join(fruits)  # 'apple-banana-cherry'

# LeetCode: Word processing, parsing input
# Work: CSV processing, log parsing
```

### `str.strip()`, `str.lstrip()`, `str.rstrip()`
```python
text = "  hello world  "
text.strip()   # "hello world"
text.lstrip()  # "hello world  "
text.rstrip()  # "  hello world"

# LeetCode: Clean input data
# Work: Process user input, file parsing
```

### `str.replace()` and `str.translate()`
```python
text = "hello world"
text.replace('l', 'x')  # "hexxo worxd"

# For character mapping (faster for multiple replacements)
trans = str.maketrans('aeiou', '12345')
"hello".translate(trans)  # "h2ll4"

# LeetCode: String transformations
# Work: Data cleaning, text processing
```

### `str.startswith()`, `str.endswith()`, `str.find()`, `str.count()`
```python
text = "python_script.py"
text.startswith('python')  # True
text.endswith('.py')       # True
text.find('script')        # 7 (index), -1 if not found
text.count('p')           # 2

# LeetCode: Pattern matching, substring problems
# Work: File processing, validation
```

## List Methods

### `list.append()`, `list.extend()`, `list.insert()`
```python
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4]
nums.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]

# LeetCode: Building result arrays
# Work: Data collection, list building
```

### `list.pop()`, `list.remove()`, `list.reverse()`
```python
nums = [1, 2, 3, 4, 5]
last = nums.pop()      # 5, nums = [1, 2, 3, 4]
first = nums.pop(0)    # 1, nums = [2, 3, 4]
nums.remove(3)         # nums = [2, 4] (removes first occurrence)
nums.reverse()         # nums = [4, 2] (in-place)

# LeetCode: Stack operations, array manipulation
# Work: Data processing, cleanup
```

### `list.sort()` and `sorted()`
```python
nums = [3, 1, 4, 1, 5]
nums.sort()           # [1, 1, 3, 4, 5] (in-place)
sorted_copy = sorted(nums, reverse=True)  # [5, 4, 3, 1, 1]

# Custom sorting
words = ["apple", "pie", "Washington", "book"]
sorted(words, key=len)              # Sort by length
sorted(words, key=str.lower)        # Case-insensitive sort

# LeetCode: Sorting algorithms, custom comparisons
# Work: Data analysis, reporting
```

## Dictionary Methods

### `dict.get()`, `dict.setdefault()`, `dict.pop()`
```python
data = {'a': 1, 'b': 2}
value = data.get('c', 0)        # 0 (default if key missing)
data.setdefault('c', 0)         # Returns 0, adds 'c': 0 if missing
removed = data.pop('a', None)   # 1, removes key 'a'

# LeetCode: Hash table operations, counting
# Work: Configuration management, data lookup
```

### `dict.keys()`, `dict.values()`, `dict.items()`
```python
data = {'a': 1, 'b': 2, 'c': 3}
list(data.keys())    # ['a', 'b', 'c']
list(data.values())  # [1, 2, 3]
list(data.items())   # [('a', 1), ('b', 2), ('c', 3)]

# LeetCode: Dictionary iteration, key-value processing
# Work: Data transformation, analysis
```

## Set Operations

### `set.add()`, `set.update()`, `set.remove()`, `set.discard()`
```python
s = {1, 2, 3}
s.add(4)           # {1, 2, 3, 4}
s.update([5, 6])   # {1, 2, 3, 4, 5, 6}
s.remove(1)        # {2, 3, 4, 5, 6} (raises KeyError if missing)
s.discard(10)      # No error if missing

# LeetCode: Unique elements, fast lookup
# Work: Data deduplication, membership testing
```

### Set Operations: `union()`, `intersection()`, `difference()`
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 | set2         # {1, 2, 3, 4, 5, 6} (union)
set1 & set2         # {3, 4} (intersection)
set1 - set2         # {1, 2} (difference)
set1 ^ set2         # {1, 2, 5, 6} (symmetric difference)

# LeetCode: Set theory problems, finding common elements
# Work: Data comparison, filtering
```

## Built-in Functions

### `len()`, `min()`, `max()`, `sum()`
```python
data = [1, 5, 3, 9, 2]
len(data)    # 5
min(data)    # 1
max(data)    # 9
sum(data)    # 20

# With key functions
words = ["python", "java", "go", "javascript"]
min(words, key=len)  # "go"
max(words, key=len)  # "javascript"

# LeetCode: Basic statistics, array analysis
# Work: Data analysis, validation
```

### `enumerate()` and `zip()`
```python
# enumerate - get index and value
for i, value in enumerate(['a', 'b', 'c']):
    print(f"{i}: {value}")  # 0: a, 1: b, 2: c

# zip - combine iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# LeetCode: Index tracking, parallel iteration
# Work: Data pairing, coordinated processing
```

### `map()`, `filter()`, `any()`, `all()`
```python
numbers = [1, 2, 3, 4, 5]

# map - apply function to all elements
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# filter - keep elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# any/all - boolean operations
any([True, False, False])   # True
all([True, True, False])    # False

# LeetCode: Functional programming, condition checking
# Work: Data transformation, validation
```

### `range()`, `reversed()`, `sorted()`
```python
# range - generate sequences
list(range(5))        # [0, 1, 2, 3, 4]
list(range(1, 6))     # [1, 2, 3, 4, 5]
list(range(0, 10, 2)) # [0, 2, 4, 6, 8]

# reversed - reverse any iterable
list(reversed([1, 2, 3]))     # [3, 2, 1]
list(reversed("hello"))       # ['o', 'l', 'l', 'e', 'h']

# LeetCode: Loop control, sequence generation
# Work: Iteration, data processing
```

## Type Conversion & Checking

### `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`
```python
# Type conversion
int("123")      # 123
float("3.14")   # 3.14
str(123)        # "123"
list("hello")   # ['h', 'e', 'l', 'l', 'o']
set([1,2,2,3])  # {1, 2, 3}

# LeetCode: Input parsing, data type manipulation
# Work: Data conversion, API responses
```

### `isinstance()`, `type()`
```python
isinstance(123, int)        # True
isinstance([1,2,3], list)   # True
type("hello")               # <class 'str'>

# LeetCode: Type checking, input validation
# Work: Defensive programming, data validation
```

## Advanced Built-ins

### `abs()`, `round()`, `divmod()`, `pow()`
```python
abs(-5)         # 5
round(3.14159, 2)  # 3.14
divmod(17, 5)   # (3, 2) - quotient and remainder
pow(2, 3)       # 8 (same as 2**3)
pow(2, 3, 5)    # 3 (2^3 % 5, efficient for large numbers)

# LeetCode: Mathematical operations, modular arithmetic
# Work: Financial calculations, data processing
```

### `ord()`, `chr()`, `bin()`, `hex()`, `oct()`
```python
ord('A')        # 65 (ASCII value)
chr(65)         # 'A'
bin(10)         # '0b1010'
hex(255)        # '0xff'
int('1010', 2)  # 10 (binary to decimal)

# LeetCode: Character manipulation, bit operations
# Work: Data encoding, low-level operations
```

## Pro Tips for LeetCode & Work

### 1. Dictionary for Counting (Most Common Pattern)
```python
# Instead of checking if key exists
count = {}
for char in string:
    count[char] = count.get(char, 0) + 1

# Or use setdefault
for char in string:
    count.setdefault(char, 0)
    count[char] += 1
```

### 2. List Comprehensions (Concise & Readable)
```python
# Filter and transform in one line
evens_squared = [x**2 for x in range(10) if x % 2 == 0]

# Nested comprehensions for 2D operations
matrix = [[i+j for j in range(3)] for i in range(3)]
```

### 3. String Manipulation Shortcuts
```python
# Check if string contains only digits
"123".isdigit()     # True
"12.3".isdigit()    # False

# Check character types
"A".isupper()       # True
"a".islower()       # True
"a1".isalnum()      # True
```

### 4. Efficient Set Operations
```python
# Remove duplicates while preserving order (Python 3.7+)
unique_list = list(dict.fromkeys(original_list))

# Fast membership testing
if item in my_set:  # O(1) average case
    # Much faster than 'item in my_list' which is O(n)
```

These methods form the foundation of efficient Python programming for both daily work and competitive coding. Master these, and you'll solve most problems more elegantly and efficiently!