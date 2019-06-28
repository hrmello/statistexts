import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

plt.style.use("ggplot")

def plot_word_cloud(text, stop_words):
	'''
	Plot a word cloud from the words within the text and save it in local directory
	'''
	wc = WordCloud(stopwords = set(stop_words), background_color='white', contour_color='black', random_state=5, height=300, width=500).generate(text)
	wc.to_file("plots/wordcloud.jpg")

	return 0

def plot_freq(word_frequency, top_words = 20):
    # Compute the most frequent words and sort them in descending order 
    k = Counter(word_frequency)
    top_k = {}
    for word, value in k.most_common(top_words):
        top_k[word] = value

    # Bar plot
    fig = plt.figure(figsize=(15,8))
    plt.bar(range(len(top_k)), list(top_k.values()), align='center')
    plt.xticks(range(len(top_k)), list(top_k.keys()), rotation = 'vertical')
    plt.xlabel("Words", fontsize = 15)
    plt.ylabel("Frequency", fontsize = 15)
    plt.title(f"Word Frequency for the top {top_words} words", fontsize = 25)
    fig.savefig('plots/frequency_plot.jpg')
   
    return 0
    
def plot_dispersion(text, words, ignore_case=False, title="Lexical Dispersion Plot"):
    """
    Generate a lexical dispersion plot. 
    
    #######################################################################
    #Taken from nltk source code and modified to use plt rather than pylab#
    #######################################################################
    
    :param text: The source text		
    :type text: list(str) or enum(str)
    :param words: The target words
    :type words: list of str
    :param ignore_case: flag to set if case should be ignored when searching text
    :type ignore_case: bool
    """

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ValueError(
            'The plot function requires matplotlib to be installed.'
            'See http://matplotlib.org/'
        )

    text = list(text)
    words.reverse()

    if ignore_case:
        words_to_comp = list(map(str.lower, words))
        text_to_comp = list(map(str.lower, text))
    else:
        words_to_comp = words
        text_to_comp = text

    points = [
        (x, y)
        for x in range(len(text_to_comp))
        for y in range(len(words_to_comp))
        if text_to_comp[x] == words_to_comp[y]
    ]

    if points:
        x, y = list(zip(*points))
    else:
        x = y = ()
    fig = plt.figure(figsize = (15,8))
    plt.plot(x, y, "b|", scalex=0.1)
    plt.yticks(list(range(len(words))), words, color="b")
    plt.ylim(-1, len(words))
    plt.title(title)
    plt.xlabel("Word Offset")
    fig.savefig("plots/lexical_dispersion.jpg")
    
    return 0
