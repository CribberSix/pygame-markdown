
# pygame-markdown
![PyPI](https://img.shields.io/pypi/v/pygame-markdown?color=%233775A9&label=pypi%20package&style=plastic)
![GitHub](https://img.shields.io/github/license/CribberSix/pygame-markdown?style=plastic)


1. [Purpose](#Purpose)
2. [Usage](#Usage)
3. [Internal workings](#Internal-workings)
4. [Markdown element implementations](#Markdown-element-implementations)
5. [Contributing](#Contributing)

----

### Purpose

The package's class parses, interprets and renders the contents of a markdown file onto a pygame surface. 

### Usage
##### 1. Instantiation
The class instantiation takes no parameters. 
```Python
from src.pygamemarkdown import MarkdownRenderer
md = MarkdownRenderer()  # create instance 
```

##### 2. Choose markdown file by path
To choose a markdown file to display, use the method:

```Python
md.set_markdown(mdfile_path) 
```

- `mdfile_path` - the local path of the markdown file which will be displayed

##### 3. Display
To display the content of the markdown file on a surface in a specific location use the method: 

 ```Python
md.display(surface, offset_X, offset_Y, width=-1, height=-1)  
```
- `surface` - the pygame surface which the text is blitted on 
- `offset_X` - the offset of the text from the surface's left sided border
- `offset_Y`- the offset of the text from the surface's top border

Optional:
- `width` - the width of the textarea  
- `height` - the height of the textarea 

If no width/height is supplied, the entire length - starting from the x-/y-coordinate 
to the opposite side of the supplied surface - is used.

----

### Internal workings
The class uses a three stage process to render the contents of a markdown file onto a pygame surface. 
For an overview of the implemented syntactic markdown structures, see [Markdown element implementations](#Markdown-element-implementations).

##### Stage 1: Parsing
The text is restructured from physical lines to logical lines. 
Since markdown allows for continuation of a logical line
after a physical linebreak, the text gets rearranged into paragraphs/blocks depending on the content. 
 
##### Stage 2: Interpreting
Each block is given a tag to describe its content. Examples are:
- Header (h1,h2 or h3)
- Unordered List
- Ordered List
- Code 
- Quote
- Normal text
- Horizontal rule 

##### Stage 3: Rendering
Based on the type of the block the text is rendered with certain parameters. Examples:
- Code is indented and has a different background color 
- Quotes are indentend, have a different font color and a vertical rectangle in front of the text. 
- Horizontal rule blocks are rendered as a horizontal rectangle along the width of the textarea.
- All text is automatically continued in the next line if the supplied width is too small.  
----
     
### Markdown element implementations
The following table gives an overview on which markdown elements are implemented so far and can be displayed correctly.

A further indented unordered sublist of an unordered list item can be achieved 
by adding four spaces in front of the hyphen. The first item in an unordered list cannot be further indented, 
only sublists can be indented further.

| Element       | Markdown Syntax     | Status |
| :------------- | :---------- | :---------- |
|  Heading | # h1 <br/>## h2 <br/>### h3   | DONE |
| Bold |  \*\*bold text\*\* | TODO |
| Cursive | \*italicized text\* |TODO |
| Block of code   | \``` <br/>print("Hello World!") <br/> \``` | DONE |
| Inline code | \`print("Hello World")\` | DONE |
| Unordered List | - First item <br/>- Second item<br/>- Third item |  DONE | 
| Ordered List | 1. First item <br/>2. Second item <br/>3. Third Item | DONE |
| Blockquote | \> blockquote | DONE |
| Horizontal rule | --- | DONE |

----

### Contributing
I welcome pull requests from the community. 
Please take a look at the [TODO](https://github.com/CribberSix/pygame-markdown/blob/master/TODO.txt) file for opportunities to help this project. 

Please ensure your PR fulfills the following requirements:
- English code documentation - including doc-strings for new methods.
- Pull Requests must fulfill at least one of the following purposes:
    - Bugfixing    
    - New functionality (or extending the existing functionalities)
    - Enhancement concerning performance or ease of use. 
- The README is updated accordingly.
- Your code should pass [PEP8](https://www.python.org/dev/peps/pep-0008/). You can check your code's PEP8 compliance [here](http://pep8online.com/checkresult).
The exception is the errorcode `E501 - line too long` - because 79 characters per line is a stupid limit. 
