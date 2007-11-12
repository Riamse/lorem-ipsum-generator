#!/usr/bin/env python
#
# This file is part of the Lorem Ipsum Generator.
# 
# The Lorem Ipsum Generator is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
# 
# The Lorem Ipsum generator is distributed in the hope that it will 
# be useful, but WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the Lorem Ipsum Generator.  If not, 
# see <http://www.gnu.org/licenses/>.
#

import pygtk
pygtk.require('2.0') 
# TODO: Cross-check the widgets and options I use with the documentation
# to see which version I really require
import gtk

import lipsum
import string

class Main:
	def __init__(self):
		self.__initialize_window()
	
	def __initialize_window(self):
		# Output area
		self.__textbuffer_output = gtk.TextBuffer()

		self.__textview_output = gtk.TextView(buffer=self.__textbuffer_output)
		self.__textview_output.set_wrap_mode(gtk.WRAP_WORD_CHAR)
		self.__textview_output.set_editable(False)
		self.__textview_output.set_left_margin(6)
		self.__textview_output.set_right_margin(6)

		self.__scrolledwindow_output = gtk.ScrolledWindow()
		self.__scrolledwindow_output.set_shadow_type(gtk.SHADOW_IN)
		self.__scrolledwindow_output.add(self.__textview_output)
		self.__scrolledwindow_output.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

		self.__alignment_output = gtk.Alignment(xalign=0.5, yalign=0.5, xscale=1.0, yscale=1.0)
		self.__alignment_output.add(self.__scrolledwindow_output)
		self.__alignment_output.set_padding(0, 0, 12, 0)

		self.__frame_output = gtk.Frame(label='<b>Output</b>')
		self.__frame_output.get_label_widget().set_use_markup(True)
		self.__frame_output.add(self.__alignment_output)
		self.__frame_output.set_shadow_type(gtk.SHADOW_NONE)

		# Options area
		self.__spinbutton_quantity = gtk.SpinButton()
		self.__spinbutton_quantity.set_range(1, 999)
		self.__spinbutton_quantity.set_increments(1, 10)
		self.__spinbutton_quantity.set_width_chars(4)
		self.__spinbutton_quantity.set_value(5)

		self.__radiobutton_quantity_paragraphs = gtk.RadioButton(label='Paragraphs')
		self.__radiobutton_quantity_sentences = gtk.RadioButton(label='Sentences', group=self.__radiobutton_quantity_paragraphs)

		self.__vbox_quantity_radiobuttons = gtk.VBox()
		self.__vbox_quantity_radiobuttons.add(self.__radiobutton_quantity_paragraphs)
		self.__vbox_quantity_radiobuttons.set_child_packing(self.__radiobutton_quantity_paragraphs, False, True, 0, gtk.PACK_START)
		self.__vbox_quantity_radiobuttons.add(self.__radiobutton_quantity_sentences)
		self.__vbox_quantity_radiobuttons.set_child_packing(self.__radiobutton_quantity_sentences, False, True, 0, gtk.PACK_START)

		self.__hbox_quantity = gtk.HBox(spacing=6)
		self.__hbox_quantity.add(self.__spinbutton_quantity)
		self.__hbox_quantity.set_child_packing(self.__spinbutton_quantity, False, True, 0, gtk.PACK_START)
		self.__hbox_quantity.add(self.__vbox_quantity_radiobuttons)
		self.__hbox_quantity.set_child_packing(self.__vbox_quantity_radiobuttons, False, True, 0, gtk.PACK_START)

		self.__alignment_quantity = gtk.Alignment(xalign=0.5, yalign=0.5, xscale=1.0, yscale=1.0)
		self.__alignment_quantity.add(self.__hbox_quantity)
		self.__alignment_quantity.set_padding(0, 0, 12, 0)

		self.__frame_quantity = gtk.Frame(label='<b>Quantity</b>')
		self.__frame_quantity.get_label_widget().set_use_markup(True)
		self.__frame_quantity.add(self.__alignment_quantity)
		self.__frame_quantity.set_shadow_type(gtk.SHADOW_NONE)
		
		self.__checkbutton_startwithlorem = gtk.CheckButton(label='Start with "Lorem ipsum..."')

		self.__alignment_options = gtk.Alignment(xalign=0.5, yalign=0.5, xscale=1.0, yscale=1.0)
		self.__alignment_options.add(self.__checkbutton_startwithlorem)
		self.__alignment_options.set_padding(0, 0, 12, 0)

		self.__frame_options = gtk.Frame(label='<b>Options</b>')
		self.__frame_options.get_label_widget().set_use_markup(True)
		self.__frame_options.add(self.__alignment_options)
		self.__frame_options.set_shadow_type(gtk.SHADOW_NONE)
		#self.__frame_options.set_child_packing(self.__checkbutton_startwithlorem, False, True, 0, gtk.PACK_START)

		self.__hbox_options = gtk.HBox(spacing=6)
		self.__hbox_options.add(self.__frame_options)
		self.__hbox_options.set_child_packing(self.__frame_options, False, True, 0, gtk.PACK_END)
		self.__hbox_options.add(self.__frame_quantity)
		self.__hbox_options.set_child_packing(self.__frame_quantity, False, True, 0, gtk.PACK_END)

		# Actions area
		self.__button_copy = gtk.Button(stock=gtk.STOCK_COPY)
		self.__button_copy.connect('clicked', self.__copy_output)

		self.__button_generate = gtk.Button(label='Generate text')
		self.__button_generate.connect('clicked', self.__generate_output)

		self.__hbox_actions = gtk.HBox(spacing=6)
		self.__hbox_actions.add(self.__button_generate)
		self.__hbox_actions.set_child_packing(self.__button_generate, False, True, 0, gtk.PACK_END)
		self.__hbox_actions.add(self.__button_copy)
		self.__hbox_actions.set_child_packing(self.__button_copy, False, True, 0, gtk.PACK_END)

		# Main window / vbox

		self.__vbox_main = gtk.VBox(spacing=12)
		self.__vbox_main.add(self.__frame_output)
		self.__vbox_main.set_child_packing(self.__frame_output, True, True, 0, gtk.PACK_START)
		self.__vbox_main.add(self.__hbox_options)
		self.__vbox_main.set_child_packing(self.__hbox_options, False, True, 0, gtk.PACK_START)
		self.__vbox_main.add(self.__hbox_actions)
		self.__vbox_main.set_child_packing(self.__hbox_actions, False, True, 0, gtk.PACK_START)
		self.__vbox_main.set_border_width(12)

		self.__window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.__window.set_title("Lorem ipsum generator")
		self.__window.connect('destroy', self.__destroy)
		self.__window.add(self.__vbox_main)
		self.__window.show_all()

		self.__clipboard = gtk.Clipboard()
	
	def main(self):
		gtk.main()

	def __destroy(self, widget, data=None):
		gtk.main_quit()
	
	def __copy_output(self, widget, data=None):
		self.__clipboard.set_text(
				self.__textbuffer_output.get_text(
					self.__textbuffer_output.get_start_iter(),
					self.__textbuffer_output.get_end_iter()
					)
				)

	def __generate_output(self, widget, data=None):
		try:
			sample = 'sample.txt'
			dictionary = 'dictionary.txt'
			generator = lipsum.generator(sample, dictionary)
		except IOError, (errno, strerror):
			error = gtk.MessageDialog(parent=self.__window, type=gtk.MESSAGE_ERROR, message_format='Could not locate one of the dictionary or sample files, "%s" or "%s", respectively.' % (dictionary, sample), buttons=gtk.BUTTONS_OK)
			def close_error(widget, data=None):
				widget.destroy()
			error.connect('response', close_error)
			error.show()
			return

		quantity = self.__spinbutton_quantity.get_value_as_int()

		text = []

		for i in range(len(text), quantity):
			if self.__radiobutton_quantity_paragraphs.get_active():
				text += [generator.generate_paragraph()]
			elif self.__radiobutton_quantity_sentences.get_active():
				text += [generator.generate_sentence()]
		
		if self.__radiobutton_quantity_paragraphs.get_active():
			if self.__checkbutton_startwithlorem.get_active():
				text[0] = generator.generate_paragraph(start_with_lorem=True)
			text = string.join(text, '\n\n')
		elif self.__radiobutton_quantity_sentences.get_active():
			if self.__checkbutton_startwithlorem.get_active():
				text[0] = generator.generate_sentence(start_with_lorem=True)
			text = string.join(text, ' ')

		self.__textbuffer_output.set_text(text)

if __name__ == "__main__":
	main = Main()
	main.main()
