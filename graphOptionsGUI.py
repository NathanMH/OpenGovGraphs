import easygui as eg


class gui_settings:

	def __init__(self):
		window_msg   = "Choose the labels for your graph"
		window_title = "Graphing Assistant"
		field_names  = ["title", "x-label", "y-label"]
		field_values = []
		answers      = eg.multenterbox(window_msg, window_title, field_names, field_values)
		self.title   = answers[0]
		self.x_label = answers[1]
		self.y_label = answers[2]