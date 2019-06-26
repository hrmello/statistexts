import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

plt.style.use("ggplot")

## TODO: Fix the saving step of each plot

## TODO: Create custom dispersion plot in order to save it and make the code run 
## without stopping at the plot_dispersion function

def plot_dispersion(text, list_of_words = list()):
	'''
	Dispersion plot for each word in list_of_words
	text must be of class Text from nltk, made fomr tokenized objects
	'''
	assert len(list_of_words) != 0 #non-empty list
	plt.figure(figsize=(15,5))
	text.dispersion_plot(list_of_words)
	plt.savefig("lexical_dispersion.jpg")
	
	return 0
	
def plot_word_cloud(text, stop_words):
	'''
	Plot a word cloud from the words within the text and save it in local directory
	'''
	wc = WordCloud(stopwords = set(stop_words), background_color='white', contour_color='black', random_state=5, height=300, width=500).generate(text)
	wc.to_file("wordcloud.jpg")

	return 0

def plot_freq(word_frequency, top_words = 20):
    # Compute the most frequent words and sort them in descending order 
    k = Counter(word_frequency)
    top_k = {}
    for word, value in k.most_common(top_words):
        top_k[word] = value

    # Bar plot
    plt.figure(figsize=(15,5))
    plt.bar(range(len(top_k)), list(top_k.values()), align='center')
    plt.xticks(range(len(top_k)), list(top_k.keys()), rotation = 'vertical')
    plt.xlabel("Words", fontsize = 15)
    plt.ylabel("Frequency", fontsize = 15)
    plt.title(f"Word Frequency for the top {top_words} words", fontsize = 25)
    plt.show() 
    plt.savefig('frequency_plot.jpg')
    
    return 0
