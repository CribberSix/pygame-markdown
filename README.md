# pygame-markdown

A simple python function to blit Markdown text on a python surface.

## Second header for internal tests.
- This is another text
- This is another text
- This is another text
Text
### Third header for internal tests.

This is a text beneath the third text header. A bit longer: 
The lstrip() method will remove leading whitespaces, 
newline and tab characters on a string beginning. Lorem Ipsum whoop. 

```Python
a = 500
print("Hello World:" + str(500))
```
     
# Contributing
I welcome pull requests from the community. 
Please take a look at the [TODO](https://github.com/CribberSix/pygame-markdown/blob/master/TODO.txt) file for opportunities to help this project. 

Please ensure it fulfills the following requirements:
- It must pass [PEP8](https://www.python.org/dev/peps/pep-0008/). You can check your code's PEP8 compliance [here](http://pep8online.com/checkresult).
- Pull Request's must be adequately formatted, described and fulfill at least one of the following purposes:
    - Bugfixing    
    - New functionality (extending the existing functionalities)
    - Enhancement concerning performance, code readability, or usage. 
- The README is updated accordingly.



### Markdown element implementations

| Element       | Markdown Syntax     | Status |
| :------------- | :---------- | :---------- |
|  Heading | # h1 <br/>## h2 <br/>### h3   | DONE |
| Block of code   | \``` <br/>print("Hello World!") <br/> \``` | DONE |
| Inline code | \`print("Hello World")\` | TODO |
| Unordered List | - First item <br/>- Second item <br/>-Third Item |  DONE | 
| Ordered List | 1. First item <br/>2. Second item <br/>3.Third Item | TODO |
| Bold |  \*\*bold text\*\* | TODO |
| Cursive | \*italicized text\* |TODO |
| Blockquote | \> blockquote | TODO |
| Horizontal rule | --------- | TODO |

