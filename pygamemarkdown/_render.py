
def render_block(self, block: str, block_type: str, y: int) -> int:

    # Same background functionality
    if block_type == 'p':
        y = self.render_text(block, block_type, y)
    elif block_type == 'blockquote':
        y = self.render_text(block, block_type, y)

    # specific functionalities
    elif block_type == 'codeblock':
        y = self.render_codeblock(block, block_type, y)
    elif block_type == 'ol':
        y = self.render_list(block, block_type, y, True)
    elif block_type == 'ul':
        y = self.render_list(block, block_type, y, False)
    elif block_type in ('h1', 'h2', 'h3'):
        y = self.render_text(block, block_type, y)

    elif block_type == 'horizontal_line':
        y = self.draw_horizontal_line(y)

    else:
        print("ELSE:" + repr(block))  # TODO: Comment line
        y = self.render_text(block, block_type, y)

    return y
