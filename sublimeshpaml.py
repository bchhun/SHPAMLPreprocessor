#coding:utf-8
import sublime, sublime_plugin
import shpaml, os


class SHPAMLPreprocessor(sublime_plugin.EventListener):
	def on_post_save(self, view):

		current_file_path = view.file_name() 
		path = ""

		if current_file_path:
			path, current_file_name = os.path.split(current_file_path)
		else:
			return

		if current_file_name.endswith(".shpaml"):

			if ".html" in current_file_name or ".xml" in current_file_name:
				new_file_name = current_file_name.replace(".shpaml", "")
			else:
				new_file_name = current_file_name.replace(".shpaml", ".html")

			with open(current_file_path, "r") as f:
				read_data = f.read()
			
			with open(os.path.join(path, new_file_name), "w") as f:
				f.write(shpaml.convert_text(read_data))
