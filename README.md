## Description
This script translates image in jpeg format to ASCII text, and stores it in file.   
Each image has been transformed to monochrome version and in pushed through filter.  
Idea and sorted array of ASCII symbols are from this article:
https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/ and I really recommend it for understanding code
## Usage
You will need next packages installed for python 3.10:
* numpy
* PIL

```
usage: python3 ascii.py [-h] [--dir DIR] [--inverse] [--mod] [--output OUTPUT] [--path PATH] [--resize RESIZE RESIZE] [--verbose]

Transform jpeg image to ASCII

optional arguments:
  -h, --help            show this help message and exit
  --dir DIR, -d DIR     Path to directory with files
  --inverse, -i         Invert image
  --mod, -m             Filter image to find edges before transformation, sharpen by default
  --output OUTPUT, -o OUTPUT

                        Output file
  --path PATH, -p PATH  Path to file
  --resize RESIZE RESIZE, -r RESIZE RESIZE
                        Resize image to x_s, y_s
  --verbose, -v
  ```
