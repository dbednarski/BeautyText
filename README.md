# BeautyText

This is a package used for text formatting – specifically for limiting the number of characters per line. It consists of a Python module with the `BeautyText`class, and an executable script that implements it.

### Directory structure

- `beautytext`: BeautyText module directory
- `examples`: example files for testing

---

## Installation

Open a terminal and enter the root directory of this package.

- To install locally (i.e., only for your user), run:
```bash
python setup.py install --user
```

- To install globally, run:
```bash
sudo python setup.py install
```

### Installation requirements

- Python ≥ 2.7
- [setuptools](https://pypi.org/project/setuptools)
- [numpy](https://www.numpy.org/)

---

# The package

## `beautytext` module

The `beautytext` module consists of a single homonym class. A description of its attributes and methods can be found in the file `beautytext/BeautyText.py` itself. The class allows third-party implementations of its functionality, and it is recommended to import it as follows:

```python
from beautytext.BeautyText import BeautyText
```

---

## `beautytext` script

The script `beautytext/script.py` is installed in the system as the executable `beautytext`. It is an implementation of the class features that reads a text file and prints the content in the terminal with a maximum character limit per line. It can be called using the syntax:

```text
beautytext [-h] [-j] [-n <num_char>] [-s (single|double)] <file>
```

- Required parameter:
  - `<file>`: path to the input file containing the text to be processed

- Optional parameters:
  - `-h`, `--help`: displays the program help message
  - `-j`, `--justify`: enables justified text
  - `-n <num_char>`, `--num_char <num_char>`: maximum number of characters per line (default: 40)
  - `-s (single|double)`, `--separator (single|double)`: paragraph separator in the input text. If `single`, interprets line breaks as paragraph separators, while `double` interprets single line breaks as continuation of the previous line, requiring a blank line between paragraphs. (default: `double`)

### Exit status

After the script finishes execution, a standard exit status code is returned to the system:

- 0: if the processing was completed successfully
- 1: if an error occurred

---

## Usability

A backslash followed by a space (`\ `) can be used to explicitly mark content that must not be split across lines. Example:

> The Pythagorean Theorem states that the sum of the squares of the legs is equal to the square of the hypotenuse, that is, c²\ =\ a²\ +\ b².

This prevents the mathematical formula from being split into two lines. The result after running the script is:

> The Pythagorean Theorem states that the sum  
> of the squares of the legs is equal to the  
> square of the hypotenuse, that is,  
> c² = a² + b².

Without the backslashes in the input text, the output would be:

> The Pythagorean Theorem states that the sum  
> of the squares of the legs is equal to the  
> square of the hypotenuse, that is, c² = a²  
> + b².

---

## Tests

After installation, run the two tests below from the root directory.


### Tests 1

```bash
beautytext examples/input_1.txt                 # compare with examples/output_1_double.txt
beautytext -j examples/input_1.txt              # compare with examples/output_1_double_just.txt
beautytext -s single examples/input_1.txt       # compare with examples/output_1_single.txt
```

### Tests 2

```bash
beautytext -s single examples/input_2.txt       # compare with examples/output_2_single.txt
beautytext -j -s single examples/input_2.txt    # compare with examples/output_2_single_just.txt
```

---

## Author

Daniel Bednarski Ramos  
daniel.bednarski.ramos@gmail.com

---

## License

GNU GPLv3
