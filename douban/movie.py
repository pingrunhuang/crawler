class Movie:
    def __init__(self, name, rating, comments=None):
        self.name = name
        self.rating = rating
        self.comments = comments
   
    def generate_wordcount(self):
        """Generate wordcount based on the movie's comment
        """
        from wordcloud import WordCloud
        wordcloud = WordCloud(background_color='white', max_words=200)
        wordcloud.generate(self.comments)
        # show the word cloud
        wordcloud.to_image().show()
        