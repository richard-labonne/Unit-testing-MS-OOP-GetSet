class Square:
    def __init__(self, h, w):
        if h is not w:
            raise Exception("Not square")

        self.height = h		
        self.width = w		

    @property 
    def height(self):
        return self.__height
    @property 
    def width(self):
        return self.__width 

    def set_sides(self, h, w):
        if h is not w:
            raise Exception("Not square")

        self.height = h	
        self.width = w	

    @height.setter 
    def height(self, new_value):
        if new_value > 0:
          self.__height = new_value 
        else:
          raise Exception("Value must be larger than 0")
    @width.setter 
    def width(self, new_value):
        if new_value > 0:
          self.__width = new_value	
        else:
          raise Exception("Value must be larger than 0")