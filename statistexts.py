print("Importing the necessary libraries...")

from PyPDF2 import PdfFileWriter, PdfFileReader
from collections import Counter, defaultdict
from tqdm import tqdm
from helper import stats_functions, plot_functions
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import cmd
import argparse
import nltk
import string


''' File Reader'''

## TODO add argparse rather than asking for keyboard input

def add_wordcount_to_dict(words_from_page, total_word_count):
    '''Update the count of total words within the text'''
    for key in words_from_page.keys():
        if key not in total_word_count.keys():
            total_word_count[key] = words_from_page[key]
        else:
            total_word_count[key] += words_from_page[key]

def read_pdf(pdf_name):
	return PdfFileReader(open(pdf_name, "rb"))
	
def pdf_to_txt(txt_name = "txt_file.txt", encoding = 'utf-8'):
	return open(txt_name, "w", encoding=encoding)

def write_and_count(pdf_text, text_file):
	
	total_word_count = dict()

	totalNumPages = pdf_text.numPages

	print("#### Writing the pdf into a txt file and counting the number of each word in the text ####")
	
	for page in tqdm(range(totalNumPages)):
		# extracts the text from a page
		page_text = pdf_text.getPage(page).extractText()
		# write it into the new txt file
		text_file.write(page_text)
		#remove '\n' and punctuations
		page_content = page_text.lower().replace('\n', '').translate(str.maketrans('', '', string.punctuation)).split(' ')
		
		#count the numbe rof occurrences of each word in that page and add it to dictionary
		dict_words_page = Counter(page_content)
		add_wordcount_to_dict(dict_words_page, total_word_count)
	return total_word_count
	
def open_txt(file_name, encoding = 'utf-8'):
	return open(file_name, "r")
 
def tokenize(stop_words, txt_file):

	tokens = nltk.word_tokenize(txt_file.lower())
	tokens = [token  for token in tokens if token.isalpha() and token not in stop_words]
	text = nltk.Text(tokens)
	
	return tokens, text
	
def count_words(text):
    length_count =  defaultdict(int)

    for word in text:
        number_of_chars = len(word)
        length_count[number_of_chars]+=1

    plt.figure(figsize=(15,8))
    sb.barplot(x = list(length_count.keys()), y = list(length_count.values()))
    plt.xlabel("Length of words", fontsize = 15)
    plt.ylabel("# of times of occurrence", fontsize = 15)
    plt.title("How many words of each length are there in the text", fontsize = 25)
    
    return length_count
    
def main():
	print("Please enter the name of the path to the pdf file you want to analyse:")
	file_name = input()
	#file_name = "domCasmurro.pdf" #uncomment this line to use the pdf file that is already in the folder
	assert type(file_name) == str
	
	# read pdf file
	pdf_input = read_pdf(file_name)
	
	print("Please enter the name of the path to the new txt file generated from the pdf:")
	txt_name = input()
	#txt_name = "book_content.txt" #uncomment this line to use this default name in the .txt document
	assert type(txt_name) == str
	
	# creates a txt file with the content of the pdf
	text_file = pdf_to_txt(txt_name = txt_name)
	
	total_word_count = write_and_count(pdf_input, text_file)
	
	# read txt file
	written_file= open_txt(txt_name)
	read_written = written_file.read()
	
	# get stopwords in portuguese (need to change if using to analyse texts in another language)
	sw = stopwords.words('portuguese')
	
	tokens, text = tokenize(stop_words = sw, txt_file = read_written)
	 
	#plot_functions.plot_dispersion(text, ['capitu', 'bentinho'])

	print("#### Now computing some statistics ####")
	print("Computing TTR:")
	
	ttr = stats_functions.ttr(text)
	print(f"TTR = {ttr}")
	
	print("#### Computing lexical diversity D and its standard deviation over several samples extract from the text ####")
	d, std_d = stats_functions.compute_D(text)
	print(f"D = {d:.2f}")
	print(f"D standard deviation = {std_d:.2f}")
	
	print("#### Counting the number of occurrence of each word in the text to display it as a bar plot ####")
	_ = count_words(text)
	
	print("#### Creating a word cloud ####")
	_ = plot_functions.plot_word_cloud(read_written, sw)
	
	print("#### Word frequency plot ####")
	frequency = nltk.FreqDist(w.lower() for w in tokens if w not in sw)
	_ = plot_functions.plot_freq(frequency)
	
if __name__ == "__main__":
	main()

	
	
	

	
	
	
	
	
	
	
	
	
	
