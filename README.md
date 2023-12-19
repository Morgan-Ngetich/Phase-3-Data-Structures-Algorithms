# Word Frequency and Balance Checker

## Project Description
This project consists of three Python functions:

1. `word_frequency(sentence)`: Computes the frequency of each word in a given sentence.
2. `remove_duplicates(sequence)`: Removes duplicate elements from a sequence.
3. `is_balanced(expression)`: Checks whether an expression containing brackets, parentheses, and braces is balanced.

## Table of Contents
1. [Project Description](#project-description)
2. [How the Programs Work](#how-the-programs-work)
3. [How to Use the Project](#how-to-use-the-project)
4. [Features](#features)
5. [Built With](#built-with)
6. [Authors](#authors)
7. [License](#license)

## How the Programs Work

### Word Frequency
The `word_frequency` function takes a sentence as input, splits it into words, and returns a dictionary containing the frequency of each word in the sentence.

### Remove Duplicates
The `remove_duplicates` function removes duplicate elements from a given sequence and returns a list with unique elements.

### Balance Checker
The `is_balanced` function checks whether an expression containing brackets, parentheses, and braces is balanced. It uses a stack-based approach to validate if the opening and closing brackets are balanced.

## How to Use the Project
#### To use the project: 
``` 
git@github.com:Morgan-Ngetich/phase-3-week-2-code-challenge.git
```
**Open the files with your code editor*
#### Running the Functions
```python
# Word Frequency
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

# Remove Duplicates
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)

# Balance Checker
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))
print(is_balanced(expression2))

```


## Features
- Word frequency analysis
- Removal of duplicate elements
- Expression balance checking

## Built with
- Python 3

## Authors
- [Morgan-Ngetich]()

## License
This project is licensed under the `MIT`. See the [LICENSE.md](https://github.com/Morgan-Ngetich/phase-3-week-2-code-challenge/new/main) file for details.
