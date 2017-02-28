import easygui as eg


class gui_settings():

	def __init__(self):
		self.title = ""
		self.y_label = ""
		self.x_label = ""

	def choose_graph_labels():
		window_msg = "Choose the labels for your graph"
		window_title = "Graphing Assistant"
		field_names = ["x-label", "y-label", "title"]
		field_values = []

		field_values = eg.multenterbox(msg, title, field_names, field_values)