import kivy

from kivy.app import App

kivy.require('1.9.0')

from kivy.uix.widget import Widget

from kivy.uix.relativelayout import RelativeLayout

class Paint_brush(Widget)
	pass

class Drawing(RelativeLayout):
	def on_touch_down(self, touch):
		pb = Paint_brush()
		pb.center = touch.pos
		self.add_widget(pb)
	def on_touch_move(self, touch):
		pd = Paint_brush()
		pb.center = touch.pos
		self.add_widget(pb)
class DrawingApp(App):
	def build(self)
		return(Drawing)

DrawingApp().run()