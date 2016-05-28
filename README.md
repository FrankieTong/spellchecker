# README #

This README is a for the usage of the spellchecker module. Check the `spellchecker.py` documentation for more details.

**Note:** Current implementation reads in the entire doucment and dictionary file into memory before spell checking begins leading to a issues with needing excessively large amounts of memory to performing this task. Future work includes using an input buffered approach for reading in the doucment and dictionary file in order to remove the reliance on large amounts of free memory to run this program.

### How do I get set up? ###

This program was built using Python v2.9.7

### Running the Program ###

The main program can be called directly from the command line using the following command:

`python spellchecker.py <document_file> <dictionary_file>`

Check `InputFile` and `DictionaryFile` for examples of the document and dictionary files used for input.

##### Input Parameters #####

Parameter                      | Description   
------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`document_file`                | An ASCII input file with the document to be spell checked.
`dictionary_file`              | An ASCII input file with the dictionary holding the words to be used as reference. One dictionary word per line.

##### Outputs #####

A list of words from the document that were not found in the dictionary file.

### Who do I talk to? ###

Code Owner: Frankie (Hoi-Ki) Tong <hoiki.tong@mail.utoronto.ca\>