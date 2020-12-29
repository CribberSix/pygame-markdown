# Changelog for 'pygame-markdown' package 

#### 1.0.9
- Feature: Introduction of a new function `render_background(boolean)` to enable the user to enable/disable the background if needed.
- Bugfix: A crash occurred when the scrollbar was disabled and the user used the mousewheel 
while the mouse was within the textarea. 

#### 1.0.8
- Bugfix: When the first word of a block necessitated an immediate linebreak (the word is longer than the line), 
a variable wasn't instantiated and caused the code to crash. (Thanks [Paul](https://github.com/pmp-p)!)

#### 1.0.6
- Documentation revised
- Bugfix in the recognition of code-blocks

#### 1.0.5
- Feature: Rounded corners for inline-code background.
- Feature: Rounded corners for code-block background.

#### 1.0.4
- Bugfix: Background coloring was off with margin.

#### 1.0.3
- Feature: Implemented click-and-drag for vertical scrollbar.

#### 1.0.2
- Improvement: separated setting the markdown file from instantiation to allow for rendering of new files without new instantiation.
- Improvement: revised documentation.

#### 1.0.1
- Bugfix: Indentation of lines in lists after linebreaks due to long lines fixed.


# 1.0.0
- Initial stable version. 
