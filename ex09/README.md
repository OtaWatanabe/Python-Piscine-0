# My Local Calculator

This is a simple Python package created for a school assignment. It contains a function which count a matching string in a list.

## Installation

You can install this package using pip:
`pip install .`

## Usage

Here is how to use the function in your Python code:

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0
