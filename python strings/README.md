# Python String Exercises

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This repository contains a collection of **20 Python scripts** designed to practice and master string manipulation. Each script (`question1.py` to `question20.py`) solves a specific problem, ranging from basic operations to more complex logic involving `itertools` and data formatting.

## 📖 Table of Contents

- [Project Structure](#-project-structure)
- [Key Highlights & Examples](#-key-highlights--examples)
- [Prerequisites](#-prerequisites)
- [How to Run](#-how-to-run)
- [Topics Covered](#-topics-covered)

## 📂 Project Structure

Here is a quick reference guide to the exercises included in this repository:

| File | Challenge / Description | Key Concepts |
|------|-------------------------|--------------|
| `question1.py` | Calculate string length without `len()` | Loops, Counters |
| `question2.py` | Count character frequency | Dictionaries |
| `question3.py` | Create a string from first 2 & last 2 chars | Slicing |
| `question4.py` | Replace first char occurrences with `$` | String Manipulation |
| `question5.py` | Swap first two chars of two strings | Concatenation, Slicing |
| `question6.py` | Add 'ing' or 'ly' suffix | Conditionals |
| `question7.py` | Replace 'not...poor' with 'good' | `find()`, Substrings |
| `question8.py` | Find length of the longest word | Lists, `max()` |
| `question9.py` | Remove character at index `n` | Indexing |
| `question10.py` | Sort unique words from comma-separated list | `set()`, `sorted()`, `split()` |
| `question11.py` | Context-aware uppercase conversion | String Methods |
| `question12.py` | Reverse string if length is multiple of 4 | Logic, Reversing |
| `question13.py` | Check start of string | `startswith()` |
| `question14.py` | Number formatting (Currency/Decimal) | f-strings, format |
| `question15.py` | Count repeated chars | `collections`, `defaultdict` |
| `question16.py` | Print character index | `enumerate()` |
| `question17.py` | Convert string to list | Type Casting |
| `question18.py` | Swap commas and dots | `maketrans()`, `translate()` |
| `question19.py` | Find smallest and largest words | Loops, Comparison |
| `question20.py` | Remove consecutive duplicates | `itertools.groupby` |

## 🌟 Key Highlights & Examples

Below are examples of what each script accomplishes:

### 1. Calculate Length (`question1.py`)
Calculates the length of a string using a loop instead of the built-in `len()` function.
```python
Input:  'google.com'
Output: 10
```

### 2. Character Frequency (`question2.py`)
Counts how many times each character appears in a string.
```python
Input:  'google.com'
Output: {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
```

### 3. String Slicing (`question3.py`)
Generates a string using the first two and last two characters of the input.
```python
Input:  'w3resource'
Output: 'w3ce'
```

### 4. Character Replacement (`question4.py`)
Replaces all occurrences of the first character with `$`, except for the first one itself.
```python
Input:  'restart'
Output: 'resta$t'
```

### 5. String Swaping (`question5.py`)
Swaps the first two characters of two strings and concatenates them.
```python
Input:  'abc', 'xyz'
Output: 'xyc abz'
```

### 6. Add Suffix (`question6.py`)
Adds 'ing' to the end of a string (if length >= 3). If it already ends in 'ing', adds 'ly'.
```python
Input:  'string'
Output: 'stringly'
```

### 7. 'Not...Poor' replacement (`question7.py`)
Replaces the substring starting with 'not' and ending with 'poor' with 'good'.
```python
Input:  'The lyrics is not that poor!'
Output: 'The lyrics is good!'
```

### 8. Longest Word (`question8.py`)
Identifies the length of the longest word in a list.
```python
Input:  ['PHP', 'Exercises', 'Backend']
Output: 9
```

### 9. Remove Index (`question9.py`)
Removes the character at the specified index `n`.
```python
Input:  'Python', 0
Output: 'ython'
```

### 10. Word Sorting (`question10.py`)
Accepts a comma-separated sequence of words and prints the unique words in sorted order.
```python
Input:  'red, white, black, red, green, black'
Output: 'black, green, red, white'
```

### 11. Conditional Uppercase (`question11.py`)
Converts string to uppercase if it contains at least 2 uppercase characters in the first 4 letters.
```python
Input:  'PyThon'
Output: 'PYTHON'
```

### 12. Conditional Reverse (`question12.py`)
Reverses the string only if its length is a multiple of 4.
```python
Input:  'abcd' (Length 4)
Output: 'dcba'
```

### 13. Starts With Check (`question13.py`)
Checks if a string starts with a specific substring (e.g., "py").
```python
Input:  'python'
Output: True
```

### 14. Number Formatting (`question14.py`)
Demonstrates formating floating point numbers to 2 decimal places.
```python
Input:  3.1415926
Output: 3.14
```

### 15. Count Repeated Characters (`question15.py`)
Counts occurrences of characters in a string.
```python
Input:  'thequickbrownfoxjumpsoverthelazydog'
Output: o 4, e 3, u 2, h 2, r 2, t 2...
```

### 16. Enumerate Characters (`question16.py`)
Prints each character along with its index position.
```python
Input:  'w3r'
Output: 'Current character w position at 0'...
```

### 17. String to List (`question17.py`)
Converts a string directly into a list of characters.
```python
Input:  'Apple'
Output: ['A', 'p', 'p', 'l', 'e']
```

### 18. Swap Commas & Dots (`question18.py`)
Swaps commas and dots in a string (useful for currency localization).
```python
Input:  '32.054,23'
Output: '32,054.23'
```

### 19. Smallest & Largest Word (`question19.py`)
Finds the smallest and largest words in a given string.
```python
Input:  'It is a long string'
Output: Smallest: 'a', Largest: 'string'
```

### 20. Remove Consecutive Duplicates (`question20.py`)
Collapses consecutive duplicate characters into a single character using `itertools`.
```python
Input:  'aabcdaee'
Output: 'abcdae'
```

## 🛠 Prerequisites

- **Python 3.x**: Ensure you have Python installed. You can check by running:
  ```bash
  python --version
  ```

## 🚀 How to Run

1.  **Clone the repository** or download the files to your local machine.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the files.
4.  Run a specific script using:

    ```bash
    python question1.py
    ```
    *(Replace `question1.py` with the file you wish to run)*

## 📚 Topics Covered

- **String Traversal & Slicing**: Accessing and modifying parts of strings.
- **Built-in Methods**: Mastery of `find`, `replace`, `translate`, `split`, `join`, etc.
- **Data Structures**: Using `lists`, `dictionaries`, and `sets` for string processing.
- **Libraries**: Intro to standard libraries like `itertools` and `collections`.
- **Logic**: constructing algorithms to solve text-based problems.

---
*Happy Coding!*
