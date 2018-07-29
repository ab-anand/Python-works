import unittest
import os

def analyse_text(file):
	"""Calculate the no of lines and characters in the files

	Args:
		file: the file to read

	Raises:
		IOError: IF the file doesn't exist or can't be read
	
	Returns:A tuple where the first item is the number of lines and the other
			item is number of character.
	"""
	
	char = 0
	lines = 0
	with open(file,'r') as f:
		for line in f:
			lines += 1
			char += len(line)

	return lines, char


class TextAnalysisTexts(unittest.TestCase):
	"""Tests for the 'analyse_text()' function"""

	def setUp(self):
		"""Fixture that create a text file"""
		self.filename = 'text_analysis_test_file.txt'
		with open(self.filename, 'wt') as f:
			f.write("Now we are engaged in a great civil war.\n"
					"testing whether that nation, \n"
					"or other nation so conceived and so dedicated,\n"
					"can long endure") 

	def tearDown(self):
		"""Fixture that deletes the file created"""
		try:
			os.remove(self.filename)
		except:
			pass

	def test_function_runs(self):
		"""Check if the function runs."""
		analyse_text(self.filename)

	def test_line_count(self):
		"""Check if the line count is correct or not"""
		self.assertEqual(analyse_text(self.filename)[0], 4)

	def test_character_count(self):
		"""Check if the number of characters in the file is correct or not"""
		self.assertEqual(analyse_text(self.filename)[1], 133)

	def test_no_such_file(self):
		"""Check if the exception is raised for incorrect filename"""
		with self.assertRaises(IOError):
			analyse_text('foobar')

	def test_no_deletion(self):
		"""Check the input file doesn't get deleted"""
		analyse_text(self.filename)
		self.assertTrue(os.path.exists(self.filename))


if __name__ == "__main__":
	unittest.main()

