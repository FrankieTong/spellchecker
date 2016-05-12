"""Spell checking program prints out words in a document were not found in the dictionary

This program takes a dictionary file and a document file and performs a check identify which words 
in the document were not found in the dictionary.

Example:
	Given document file with the name "document" and a dictionary file named "dictionary", the main
	program can be executed as follows:

		$ python spellchecker.py document dictionary
	
Args:
	document (str): An ASCII input file with the document to be spell checked.
	dictionary (str): An ASCII input file with the dictionary holding the words to be used as reference
		for spell checking
		
The dictionary file is removed of all punctuation marks and non-words before being used.
		
Words are identified in the document file as any series of consequtive letters that are seperated by 
whitespace. Any words that are seperated by a hyphen and a whitespace are concatenated.
Puncuation marks are removed from the document before words are identified. If a word does not contain 
any letter characters in it, the word itself is removed from the dictionary check. Both punctuation marks 
and word characters are set to those defined by the string module in python by default.

"""

#Module imports
import argparse
import string

class ErrorDictionary(Exception):
	"""Custom exception class name for handling errors dealing with the dictionary
		
	"""
	pass
	
class ErrorDocument(Exception):
	"""Custom exception class name for handling errors dealing with the document
		
	"""
	pass

def readDictionaryIntoList(filename):
	"""Reads in the dictionary file into a string list
			
	Args:
		filename (str): Name of the ASCII input file with the dictionary file to be imported
			
	Raises:
		ErrorDictionary: If it could not open the dictionary file or the contents of the document
			file could not be converted to string
		
	Returns:
		list: A list of strings containing each word in the dictionary
		
	"""
	dictionary = [];
	
	#Try to read the contents of the dictionary into a string list
	try:
		with open(filename, 'r') as file:
			dictionary = file.read().splitlines()
			
	except IOError as e:
		raise ErrorDictionary("Could not open dictionary file")
	except ValueError as v:
		raise ErrorDictionary("Could not convert file data into string format for storing in list")
	except:
		#Unexpected error. Just raise.
		raise
		
	return dictionary

	
def readDocumentIntoString(filename):
	"""Reads in the document file into a string
			
	Args:
		filename (str): Name of the ASCII input file with the dcoument file to be imported
			
	Raises:
		ErrorDocument: If it could not open the document file or the contents of the document
			file could not be converted to string
		
	Returns:
		str: A string containing the contents of the document file
		
	"""
	document = '';
	try:
		with open(filename, 'r') as file:
			document = str(file.read())
			
	except IOError as e:
		raise ErrorDocument("Could not open document file")
	except ValueError as v:
		raise ErrorDocument("Could not convert file data into string format")
	except:
		#Unexpected error. Just raise.
		raise
		
	return document

	
class SpellChecker:
	"""Performs spell checking given a document and a dictionary.

	Words that are seperated by a hyphen and a whitespace are concatenated.
	
	Characters identified as punctuation will be remvoed from the document and dictionary before 
	spell checking while word_characters is used to identify words if the word contains at least 
	1 word character. Words	are defined as consequtive characters sperated by whitespace.
	
	Attributes:
		document (str): String containing the document to be spell checked
		dictionary (list): List containing strings that hold the words that will be used for spellchecking
		puncturation (str): Series of characters that identify which characters should be removed before
			identifying words. Default is set to characters identified in string.puncturation.
		word_characters (str): Series of characters that identify which characters consitute to being part
			of a word. Default is set to characters identified in string.letters.
	
	"""

	def __init__(self, document, dictionary, punctuation = string.punctuation, word_characters = string.letters):
		"""Initailization of the class
			
		Args:
			document (str): String containing the document to be checked
			dictionary (list): List of strings holding the reference strings to be checked against
			punctuation (Optional[str]): String of concatenated characters to be treated as puncuation marks and thus removed
				from the document and dictionary before spell checking. An example would be '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'.
			word_characters (Optional[str]): String of concatenated characters to be treated as word characters and used to 
				identify words in the document and dictionary. An example would be 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.
			
		"""
		self.document = document
		self.dictionary = dictionary
		self.punctuation = punctuation	#String of characters used to identify punctuation characters (ex: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
		self.word_characters = word_characters	#String of characters used to identify word characters (ex: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
	
	
	def _suffixRemoveAndConcatentate(self, input_list, suffix):
		"""Looks through each string in the list for entries that end with the suffix, removes the suffix and concatenates the entry with the next entry in the list
		
		Args: 
			input_list (list): List containing strings to be concatenated
			suffix (string): String of characters that is searched for at the end of each object in the list that
				indicates the string object should be concatenated with the next object in the list.
		
		Returns:
			list: The new list of strings with the appropriate strings concatenated
		
		"""
		for index in range(len(input_list) - 1):
			
			#Check if last characters of the word is the suffix. If it is, remove the suffix and concatenate to the next word and clear out the next word.
			if input_list[index].endswith(suffix):
				input_list[index] = str(input_list[index][:-len(suffix)]) + str(input_list[index+1])
				input_list[index+1] = ""
				
		#Filter out the empty entires in the list
		input_list = list(filter(None,input_list))
		
		return input_list
		
	def _suffixRemove(self, input_list, suffix):
		"""Looks through each string in the list for entries that end with the suffix and remove the suffix 
		
		Args: 
			input_list (list): List containing strings to be processed
			suffix (string): String of characters that is searched for at the end of each object in the list
		
		Returns:
			list: The new list of strings with the appropriate strings modified
		
		"""
		for index in range(len(input_list)):
			
			#Check if last characters of the word is the suffix. If it is, remove the suffix
			if input_list[index].endswith(suffix):
				input_list[index] = str(input_list[index][:-len(suffix)])
		
		return input_list
		
	def _stripList(self, input_list, char_remove = string.whitespace):
		"""Applies the .strip() command to every word in the input list 
		
		Args: 
			input_list (list): List containing strings to be processed
			char_remove (string): String of characters that is removed from the start and end of each entry
		
		Returns:
			list: The new list of strings with the appropriate strings modified
		
		"""
		for index in range(len(input_list)):
			
			#Check if last characters of the word is the suffix. If it is, remove the suffix
			input_list[index] = input_list[index].strip(char_remove)
		
		return input_list
		
		
	def _removePunctuation(self, input_list):
		"""Removes punctuation marks from all entries in the list
		
		Args:
			input_list (list): List of strings to have punctuation marks removed
			
		Returns:
			list: New list with punctuation marks removed
			
		"""
		empty_trans_table = string.maketrans("","")	#Empty translation table to make translate delete by default
		
		#Remove all characters in self.punctuation from every entry in the list
		for index in range(len(input_list)):
			input_list[index] = input_list[index].translate(empty_trans_table,self.punctuation)	

		#Filter out the empty entires in the list
		input_list = list(filter(None,input_list))
		
		return input_list
		
		
	def _removeNotWords(self, input_list):
		"""Removes all entries in the input list that do not contain any word characters
		
		Args:
			input_list (list): List of strings to have word characters removed
			
		Returns:
			list: New list with entires that do not have word characters removed
			
		"""
		
		empty_trans_table = string.maketrans("","")	#Empty translation table to make translate delete by default
		
		for index in range(len(input_list)):
			
			#First, we want to remove every word character in the word
			word_no_letters = input_list[index].translate(empty_trans_table,self.word_characters)
		
			#Clear out the entry if the length of the word without word_characters is the same as the length of the original word (ex: string consists of all symbols or numbers)
			if len(word_no_letters) == len(input_list[index]):
				input_list[index] = ''
			
		#Filter out the empty entires in the list
		input_list = list(filter(None,input_list))
		
		return input_list
		
		
	def _parseDocument(self):
		"""Performs parsing for the document in order to split the document string into individual words
		
		Words seperated by a hyphen across whitespace are concatenated. Punctuation marks are then all removed and
		words that do not contain word characters are discards to handle situations like numbers.

		Returns:
			list: A list of strings holding every word found in the document
			
		TODO:
			- Unsure if the strip all punction marks step is really needed. Depends on how the dictionary decides what is a word.
			
		"""
		
		#First split the document into a list seperated by whitespace
		document_list = self.document.split()
				
		#Handle the case with using "-" in order to strect words across 2 lines by looking for any word that ends with a "-" and concatenate it to the next word
		document_list = self._suffixRemoveAndConcatentate(document_list,'-')
		
		#Strip punctuation marks at the start and end of each word to make word processing easier
		document_list = self._stripList(document_list, self.punctuation)
		
		#Handle the case with words ending in "'s" (ex: Michael's) by removing the "'s" from the end of all strings if found
		document_list = self._suffixRemove(document_list,"'s")
		
		#Now go through the entire document and remove all remaining characters defined in punctuation
		document_list = self._removePunctuation(document_list)
			
		#Now we want to remove all single words that do not contain any word characters (helps with numbers being checked against dictionary)
		document_list = self._removeNotWords(document_list)
		
		return document_list
	
	
	def _checkWords(self,word_list, dictionary):
		"""Does the spell checking of the input word_list agaisnt the dictionary
		
		Changes everything to lower case before comparing

		Args:
			word_list (list): List of strings holding every word to be spell checked against
			dictionary (list): List of strings used as reference for spell checking
			
		Returns:
			list: A list of strings containing all the words that were not found in the dictionary. Duplicates are possible.
			
		"""
	
		bad_words = [];
		
		#Check all the words remaining to see if they are bad.
		for word in word_list:
		
			#Boolean to keep count if we are still checking the word against the list
			check_word = True
		
			#Compare each word in the document against the existing bad_word list
			for bad_word in bad_words:
				if check_word and word.lower() == bad_word.lower():
					break
			
			#Compare each word in the document against the existing dictionary list
			for dict_word in dictionary:
				if check_word and word.lower() == dict_word.lower():
					check_word = False
					break
		
			#If word still needs to be checked by the time it reaches here, add it to the list of bad words
			if check_word:
				bad_words.append(word)	
		
		return bad_words
	
	
	def check(self):
		"""Invokes the spell checking functionality of the class
		
		Document is parsed to concatenate words between new lines, remove punctuation marks and remove non-words
		
		Dictionary is fixed to punctuation marks and remove non-words

		Raises:
			ErrorDictionary: If dictionary is missing or is not a list of strings
			ErrorDocument: If document could not be converted to string
		
		Returns:
			list: A list of strings containing all the words that were not found in the dictionary. Duplicates are possible.
			
		"""
		
		#Check if document is a string. If not, return error
		if not isinstance(self.document, str):
			raise ErrorDocument("Document is not a string")
		
		#Check if dictionary is empty. If so, return error.
		if not self.dictionary:
			raise ErrorDictionary("Dictionary is missing")
		
		#Check if dictionary is a list. If not, return error
		if not isinstance(self.dictionary, list):
			raise ErrorDictionary("Dictionary is not a list")
			
		#Check if dictionary is a list of strings. If not, return error
		for words in self.dictionary:
			if not isinstance(words, str):
				raise ErrorDictionary("Dictionary is not a list of strings")
				
		#Input is confirmed correct. Now grab each word in the document and compare agaisnt the dictionary list
		
		#First want to clean up the dictionary words to remove not words and punctuation marks
		clean_dictionary = self._removePunctuation(self.dictionary)
		clean_dictionary = self._removeNotWords(clean_dictionary)
		
		#Then we split the document into words
		document_list = self._parseDocument()

		#Then perform the spell checking against the clean dictionary
		bad_words = self._checkWords(document_list, clean_dictionary)
		
		return bad_words
	
	
def SpellCheckerFromFile(document_path,dictionary_path):
	"""Attempts to read in the document and dictionary file before running spell checking
	
	Args:
		document_path (str): A string containing the path name for the doucment file
		dictionary_path (str): A string containing the path name for the dictionary file
		
	Returns:
		list: A list of strings containing all the words that were not found in the dictionary. Duplicates are possible.
	
	"""
	
	#Attempt to open dictionary file and store the contents in a list.
	dictionary = readDictionaryIntoList(dictionary_path)
	
	#Attempt to open the document file and store the contents in as a string.
	document = readDocumentIntoString(document_path)
	
	#Create an instance of the SpellChecker class and run a spell check
	spell_check = SpellChecker(document, dictionary)
	bad_words = spell_check.check()
	
	return bad_words

	
	
if __name__ == "__main__":
	"""Main function of the program. Prints the words from the document not found in the dictionary onto the screan

	Args:
		document (str): An ASCII input file with the document to be spell checked.
		dictionary (str): An ASCII input file with the dictionary holding the words to be used as reference
			for spell checking
	
	"""
	
	#General argument parser directing the user how to use this program
	parser = argparse.ArgumentParser(description='Performs spell checking of a document file and against a dictionary file')
	parser.add_argument("document", help="Document file to be checked")
	parser.add_argument("dictionary", help="Dictionary file containing valid words to check against the document file. One dictionary word per line.")
	args = parser.parse_args()
	
	#Call subfunction to start the spell checking program
	bad_words = SpellCheckerFromFile(args.document, args.dictionary)
	
	#Print out the list of bad words
	for words in bad_words:
		print words
		
		