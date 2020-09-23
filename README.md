
# pygame-markdown


1. [Purpose](#Purpose)
2. [Procedure](#Procedure)
3. [Internal workings](#Internal-workings)
4. [Markdown element implementations](#Markdown-element-implementations)
5. [Contributing](#Contributing)

### Purpose

The package's class parses, interprets and renders the contents of a markdown file onto a pygame surface. 

### Procedure
##### 1. Instantiation
The class instantiation takes no parameters. 
```
md_blitter = MarkdownBlitter()  # create instance 
```

##### 2. Choose markdown file by path
To choose a markdown file to display, use the method:
```
 set_markdown(mdfile_path) 
```

The obligatory parameters: 
- `mdfile_path`: the path to the markdown file which will be displayed

##### 3. Display
To display the markdown file on a surface in a specific location use the method: 
 ```
 md_blitter.display(surface, offset_X, offset_Y, width=-1, height=-1)  
```
Obligatory parameters: 
- `surface`: the pygame surface which the text is blitted on 
- `offset_X`: the offset of the textarea from the surface's left sided border
- `offset_Y`: the offset of the textarea from the surface's top border

Optional parameters:
- `width`: the width of the textarea 
    - if no width is supplied, the entire space starting from the x-coordinate to the right side of the supplied surface is used. 
- `height`: the height of the textarea
    - if no height is supplied, the entire space starting from the y-coordinate to the bottom of the supplied surface is used.

---

### Internal workings
The class's takes an md file as a list of strings (each String is one line in the md-file) and 
uses a three stage process to blit the contents of the markdown file onto the pygame surface. 


##### Stage 1: Parsing
The text is restructured from physical lines to logical lines. 
Since markdown allows for continuation of a logical line
after a physical linebreak, the text gets rearranged into paragraphs/"blocks" depending on the content. 
 
##### Stage 2: Interpreting
Each textblock is given a tag what it contains. Examples are:
- Header (h1,h2 or h3)
- Unordered List
- Code 
- Quote
- Normal text
- Horizontal rule 

##### Stage 3: Rendering
Based on the type of the block the text is rendered with certain parameters. Examples:
- Code is indented and has a different background color 
- Quotes are indentend, have a different font color and a vertical rectangle in front of the text. 
- Horizontal rule blocks are rendered as a horizontal rectangle along the width of the textarea.

----
     
### Markdown element implementations
The following table gives an overview on which markdown elements are implemented so far and can be displayed correctly.

| Element       | Markdown Syntax     | Status |
| :------------- | :---------- | :---------- |
|  Heading | # h1 <br/>## h2 <br/>### h3   | DONE |
| Bold |  \*\*bold text\*\* | TODO |
| Cursive | \*italicized text\* |TODO |
| Block of code   | \``` <br/>print("Hello World!") <br/> \``` | DONE |
| Inline code | \`print("Hello World")\` | DONE |
| Unordered List | - First item <br/>- Second item <br/>- Third Item |  DONE | 
| Ordered List | 1. First item <br/>2. Second item <br/>3.Third Item | TODO |
| Blockquote | \> blockquote | DONE |
| Horizontal rule | --------- | DONE |

----

### Contributing
I welcome pull requests from the community. 
Please take a look at the [TODO](https://github.com/CribberSix/pygame-markdown/blob/master/TODO.txt) file for opportunities to help this project. 

Please ensure it fulfills the following requirements:
- It must pass [PEP8](https://www.python.org/dev/peps/pep-0008/). You can check your code's PEP8 compliance [here](http://pep8online.com/checkresult).
- Pull Request's must be adequately formatted, described and fulfill at least one of the following purposes:
    - Bugfixing    
    - New functionality (extending the existing functionalities)
    - Enhancement concerning performance, code readability, or usage. 
- The README is updated accordingly.
