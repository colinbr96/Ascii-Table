# Ascii-Table

The Ascii-Table project is a simple converter from Python lists to multi-line strings that represent them. It is useful for quickly visualizing lists in the terminal.

Ascii-Table is easy to use:
```
import ascii_table.py
my_list = [
    ["Name", "Age", "Major"],
    ["Colin", 20, "Comp Sci"],
    ["Billy Bob", 30, "English"]
]
print(ascii_table.tableify(my_list))
```
The above script will output:
```sh
+-----------+-----+----------+
| Name      | Age | Major    |
+-----------+-----+----------+
| Colin     | 20  | Comp Sci |
+-----------+-----+----------+
| Billy Bob | 30  | English  |
+-----------+-----+----------+
```
