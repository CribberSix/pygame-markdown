
# pygame-markdown
![PyPI](https://img.shields.io/pypi/v/pygame-markdown?color=%233775A9&label=pypi%20package&style=plastic)
![GitHub](https://img.shields.io/github/license/CribberSix/pygame-markdown?style=plastic)

1. [Purpose](#Purpose)
2. [Usage](#Usage)
3. [Internal workings](#Internal-workings)
4. [Customization](#Customization)
5. [Markdown element implementations](#Markdown-element-implementations)
6. [Limitations](#Limitations)
7. [Contributing](#Contributing)
8. [Full example](#Full-example)

----

### Purpose

The package's class parses and renders the contents of a markdown file onto a pygame surface. 

### Usage

##### 1. Instantiation and setting the markdown content
The class instantiation takes no parameter. You can set the markdown content to be rendered either as a filepath (to a markdown file) or directly from a string.
 
```Python
from pygame_markdown import MarkdownRenderer
md = MarkdownRenderer()  # create instance
# EITHER, set the markdown file to be rendered based on a filepath:
md.set_markdown(mdfile_path=mdfile_path)  
# OR, set content directly from a string.
md.set_markdown_from_string(md_string=md_string) 
```


##### 2. Set the surface, location and area 
To display the content of the markdown file on a specific surface in a specific location use the method: 

 ```Python
md.set_area(surface, offset_X, offset_Y, width=-1, height=-1)  
```

- `surface` - the pygame surface which the text is blitted on 
- `offset_X` - the offset of the text from the surface's left sided border
- `offset_Y`- the offset of the text from the surface's top border

Optional:
- `textAreaWidth` - the width of the textarea  
- `textAreaHeight` - the height of the textarea 

If no width/height is supplied, the entire length - starting from the x-/y-coordinate 
to the right/bottom side of the supplied surface - is used.

##### 3. Display
In the *pygame loop,* the method `display` renders the contents of the markdown file onto the surface. 
In order to allow for scrolling, the display method requires some values from pygame.

```python
while True:  # pygame loop
    pygame_events = pygame.event.get()  # mouse clicks
    mouse_x, mouse_y = pygame.mouse.get_pos()  # mouse position 
    mouse_pressed = pygame.mouse.get_pressed()  # mouse being held

    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed) 
```

See the bottom of this README file for a full example.

### Internal workings
The class uses a two stage process to render the contents of a markdown file onto a pygame surface. 
For an overview of the implemented syntactic markdown structures, see [Markdown element implementations](#Markdown-element-implementations).

##### Stage 1: Parsing
The markdown file is parsed to HTML using the package [markdown](https://pypi.org/project/Markdown/). 

Based on the HTML-markers for different types of paragraphs, lists and headers, the text is split into thematic blocks. 
 
##### Stage 2: Rendering
Each block is rendered based on its specifications. Inline formatting such as `bold/strong`, `italic` and `code` 
are taken into account during the rendering process. 

- Text (excluding code-blocks!) is automatically continued in the next line if the supplied width is too small for the 
paragraph to fit into one line.  
- Code is indented and has a different background color 
- Quotes are indentend, have a different font color and a vertical rectangle in front of the text. 
- Horizontal rule blocks are rendered as a horizontal rectangle along the width of the textarea.


### Customization
 
The visuals of the markdown code can be customized with the following function. 
All functions have default values for the parameters. 

##### Text Format
- Setting gaps after lines and paragraphs respectively: 
```python
md.set_line_gaps(gap_line=8, gap_paragraph=35)  # 8 & 35 are the default values
```

##### Fonts
- Setting the font for the normal text and for the code-blocks independently. 
The module uses pygame.font.SysFont. Possible options are Verdana, Arial, CourierNew, Helvetica etc. 
The Fonts are given by name as Strings.
```python
md.set_font(font_text='Arial', font_code='CourierNew')  # Arial & CourierNew are the default values
```
- Setting Font sizes for the three headers, normal text and code-blocks.
```python
md.set_font_sizes(h1=28, h2=24, h3=20, text=16, code=16, quote=16)  # these are the default values
```


##### Coloring
- Setting the background color of the markdown area
```python
md.set_color_background(r=60, g=63, b=65)  # default values
```
- Setting the general font color of via rgb codes (no default values)
```python
md.set_color_font(r=204, g=204, b=204)  # default values
```
- Setting the font color of quote-blocks via rgb codes (no default values)
```python
md.set_color_quote(r=98, g=102, b=103)  # default values
```
- Setting the background color of the code-blocks via rgb codes (no default values)
```python
md.set_code_bg_color(r=44, g=44, b=44)  # default values
```
- Setting the color of the horizontal line: 
```python
md.set_color_hline(r=44, g=44, b=44)  # default values
```


----

### Markdown element implementations
The following table gives an overview on which markdown elements are implemented so far and can be displayed correctly.

| Element       | Markdown Syntax | 
| :------------- | :---------- | 
|  Heading | # h1 <br/>## h2 <br/>### h3   | 
| Bold | Lorem \*\*bold text\*\* ipsum | 
| Italic | Lorem \*italicized text\* ipsum |
| Block of code   | \``` <br/>print("Hello World!") <br/> \``` |
| Inline code | Lorem \`print("Hello World")\` ipsum | 
| Unordered List | - First item <br/>- Second item<br/>- Third item | 
| Ordered List | 1. First item <br/>2. Second item <br/>3. Third Item |
| Blockquote | \> Lorem ipsum | 
| Horizontal rule | --- |


---

### Limitations 
> Warning: Disregarding the following limitations leads to unpredictable outcomes.

A further indented sublist within a list (2nd level items) is not possible at the moment.

Codeblocks are not wrapped. This can lead to code being displayed to the right side of the text area if a code line
is longer than the specified width of the textarea. 

Code blocks do not recognize language strings. Code highlighting is hence not implemented.

Overloading the format of a word with bold and italic at the same time is not possible. 

Inline formatting is currently only recognized if a whitespace leads and trails the formatting characters. 

Incorrect Example: 
``` 
Lorem **ipsum**. Lorem Ipsum
```
Correct example:
``` 
Lorem **ipsum.** Lorem Ipsum
```

---

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

---

### Full example

The following code is a full example of how the package can be used.

```python
import pygame
from pygame_markdown import MarkdownRenderer  # import of the package

# minimal pygame setup
pygame.init()
screenHeight = 900
screenWidth = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pygame")
pygame.display.get_surface().fill((200, 200, 200))  # background coloring

# Creating and configuring the MarkdownRenderer.
md = MarkdownRenderer()
md.set_markdown(mdfile_path="X:\\my_markdown_file.md")
# md.set_markdown_from_string(md_string)  # Alternatively directly from a string.
surface = pygame.display.get_surface()  # get existing pygame window/screen
md.set_area(surface=surface, offset_X=50, offset_Y=20, width=500, height=500)


while True:
    pygame.draw.rect(screen, (255,255,255), (0, 0, screenWidth, screenHeight))

    # get various input from pygame
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame_events:  # handle QUIT operation
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # renders the markdown text onto the surface and handles mouse input
    md.display(pygame_events, mouse_x, mouse_y, mouse_pressed) 

    pygame.display.flip()  # updates pygame window
```
