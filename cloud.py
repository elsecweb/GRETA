# python 3

# wordcloud maker

#adapted from work by AnkitRai01 - https://www.geeksforgeeks.org/generating-word-cloud-in-python-set-2/

############################

# before running code: 'pip install wordcloud'

# importing the necessery modules
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import csv

# file object is created
file_ob = open(r"XXX.csv") #file name you want analyzed

# reader object is created
reader_ob = csv.reader(file_ob)

# contents of reader object is stored .
# data is stored in list of list format.
reader_contents = list(reader_ob)

# empty string is declare
text = ""

# iterating through list of rows
for row in reader_contents :

	# iterating through words in the row
	for word in row :

		# concatenate the words
		text = text + " " + word

# wordcloud size
wordcloud = WordCloud(width=800, height=800, max_words=200).generate(text) #feel free to customize the size and max word number

# plot the WordCloud image
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
