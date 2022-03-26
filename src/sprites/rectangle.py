from PIL import ImageDraw, Image
from io import BytesIO

class Rectangle:
    def __init__(self, x: int, y: int, fill_color: tuple, border_width: int, border_color: tuple):
        self.x = x
        self.y = y
        self.fill_color = fill_color
        self.border_width = border_width
        self.border_color = border_color
        self.memory_file = BytesIO()
        
        __img = Image.new('RGB', (self.x, self.y))
        __draw = ImageDraw.Draw(__img)
        # __draw.rectangle((self.x, self.y), self.fill_color, self.border_color, self.border_width)
        __draw.rectangle([(0,0), (self.x, self.y)], self.fill_color)
        __img.save(self.memory_file, 'PNG')
