# Statistexts Project

The code contains the initial prototype for a text analyzer that gives some statistics about a given text. In the present version, the program
- computes the [Type-Token Ratio](https://www.birmingham.ac.uk/Documents/college-artslaw/cels/essays/languageteaching/DaxThomas2005a.pdf)
- computes the [Lexical Diversity, defined as D](https://www.researchgate.net/publication/283149921_Measuring_Vocabulary_Diversity_Using_Dedicated_Software). 
- creates a [wordcloud](https://www.boostlabs.com/what-are-word-clouds-value-simple-visualizations/) with the most used words in the text.
- creates a word-frequency plot, showing the most common words and how many times they occurred in the text.
- creates a plot that shows the number of words for each possible length in the text, e.g. 10 words with 3 characters, 24 words with 5 characters and so on

# Usage

Make sure that all packages used are installed and run in the command line

`python path/to/statistexts.py`

The program will then ask for the name of the pdf file that will be analyzed and the name of the .txt file that will be created, from which all the information will be extracted.
