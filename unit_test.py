"""Quick unit test for the SpellChecker() class

Will print out either "PASS" if all the unit tests pass, or "FAIL" along with
the list of unit tests that did not pass.

Example:
	Just run the unit check program from the command line

		$ python unit_test

Current situations being tested include:
	0) File input to document and dictionary is correct
	1) No document and dictionary
	2) No document
	3) No dictionary
	4) Normal document and dictionary
	5) Normal document with numbers and dictionary
	6) Normal document and dictionary with numbers
	7) Normal document with symbols and dictionary
	8) Normal document and dictionary with character symbols
	9) Normal document and list with empty list element
	10) Normal document and list with integer list element
	11) Hyphen seperating words between lines
	12) Hyphens at the start and end of the document
	13) "'s" at the end of words
	
"""

import spellchecker as sp

case_fail = []

# Case 0: File input to document and dictionary is correct
case = 0
dictionary_path = 'DictionaryFile'
document_path = 'InputFile'

document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']

try:
	input_dictionary = sp.readDictionaryIntoList(dictionary_path)
	input_document = sp.readDocumentIntoString(document_path)
except sp.ErrorDictionary:
	case_fail.append(case)
except sp.ErrorDocument:
	case_fail.append(case)
else:
	if not input_dictionary == dictionary or not input_document == document:
		case_fail.append(case)
	

# Case 1: No document no dictionary
case = 1
document = ""
dictionary = []
result = [] #should error

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
except sp.ErrorDocument:
	pass
else:
	case_fail.append(case)
	

# Case 2: No document
case = 2
document = ""
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = [] #should return empty list

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 3: No dictionary
case = 3
document = "This is a test documnt. It contains many, interesting words. Is this a difficlt problem?"
dictionary = []
result = [] #should error with ErrorDictionary

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
else:
	case_fail.append(case)

	
# Case 4: Normal document and dictionary
case = 4
document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 5: Normal document with numbers and dictionary
case = 5
document = 'This is a 3 test documnt -4. It contains many, 7 interesting words. Is -9 this a difficlt 10 problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 6: Normal document and dictionary with numbers
case = 6
document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test', '4','7','document','it','contains','many','interesting','-5','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 7: Normal document with symbols and dictionary
case = 7
document = 'This is a 3 test documnt -4$. It contains many, %7 interesting words. Is -#9 this a difficlt !10 problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 8: Normal document and dictionary with character symbols
case = 8
document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test', '4-7','7-7','document','it','contains','many','interesting','-5+','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 9: Normal document and list with empty list element
case = 9
document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except:
	case_fail.append(case)
else:
	if not result == bad_words:
		case_fail.append(case)


# Case 10: Normal document and list with integer list element
case = 10
document = 'This is a test documnt. It contains many, interesting words. Is this a difficlt problem?'
dictionary = ['this','is','a','test','document','it',7,'contains','many','interesting','difficult','problem']
result = [] #should error with ErrorDictionary

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
else:
	if not result == bad_words:
		case_fail.append(case)

		
# Case 11: Hyphen seperating words between lines
case = 11
document = 'This is a test documnt. It contains many, interesting words. Is th-\nis a difficlt problem?'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
else:
	if not result == bad_words:
		case_fail.append(case)

		
# Case 12: Hyphens at the start and end of the document
case = 12
document = '-This is a test documnt. It contains many, interesting words. Is this a difficlt problem?-'
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
else:
	if not result == bad_words:
		case_fail.append(case)
		
		
# Case 13: "'s" at the end of words
case = 13
document = "This is a test documnt. It's contains many's, interesting words. Is this a difficlt problem's?."
dictionary = ['this','is','a','test','document','it','contains','many','interesting','difficult','problem']
result = ['documnt','words','difficlt']

try:
	spell_check = sp.SpellChecker(document, dictionary)
	bad_words = spell_check.check()
except sp.ErrorDictionary:
	pass
else:
	if not result == bad_words:
		case_fail.append(case)
		
#Print out results
if len(case_fail) > 0:
	print 'FAIL : ' + str(case_fail)
else:
	print 'PASS'	