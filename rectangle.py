from figures.figurecolor import*

class Rectangle():

 def _init_(self,width=20,height=10,color=FigureColor()):
  self._width = width
  self._height = height
  self._color = color
  self._area = width * height

 def get_area(self):
  return self._area
 
 def get_color(self):
  return self._color
 
 def _repr_(self):
  return f"Прямоугольник площадью {self._area}, цвет: {str(self._color)}"

