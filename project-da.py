#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all required libraries
import pandas
import re as regex
import string
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True) # quiet=True oder silent=True suppresses the downloading output
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import defaultdict
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.models.coherencemodel import CoherenceModel

# Import required LDA Libariers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def main():
    def remove_unwanted_characters(token):
        token = regex.sub(r'[^a-zA-Z]', ' ', token)
        return token

    def clean_raw_data(text):        
        tokens = word_tokenize(text)
        # Removing dots, special characters, and emojis 
        tokens = [remove_unwanted_characters(token) for token in tokens]
        
        # List of specific words to be removed
        unwanted_words = {'one', 'like'} 
        tokens = [token for token in tokens if token.lower() not in unwanted_words]
        
        stop_words = set(stopwords.words('english')) 
        tokens = [word for word in tokens if word.lower() not in stop_words and word not in string.punctuation]   
        
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(word) for word in tokens]
        
        # Conversion to lowercase
        tokens = [word.lower() for word in tokens]
        return tokens

    #CSV IMPORT#
    raw_data = pandas.read_csv('Musical_instruments_reviews.csv', keep_default_na=False, nrows=1000)
    # the parameter keep_default_na=False is important as otherwise libraries have issues with null values
    
    raw_reviews = raw_data["reviewText"];
    raw_summaries = raw_data["summary"];
    
    cleaned_reviews = [clean_raw_data(raw_review) for raw_review in raw_reviews]
    cleaned_summaries = [clean_raw_data(raw_summary) for raw_summary in raw_summaries]
    
    def generate_bag_of_words(text_list):
        # Prepare data > convert to strings
        text_strings = [' '.join(tokens) for tokens in text_list]

        # Create an instance of CountVectorizer because CountVectorizer expects a string
        vectorizer = CountVectorizer(ngram_range=(1,2))
       
        # Apply the vectorizer to the data
        text_bow = vectorizer.fit_transform(text_strings)

        # Determine word frequency
        word_freq = dict(zip(vectorizer.get_feature_names_out(), np.asarray(text_bow.sum(axis=0)).ravel()))
        word_freq_sorted = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

        return word_freq_sorted
        
    frequent_reviews = generate_bag_of_words(cleaned_reviews)
    frequent_summaries = generate_bag_of_words(cleaned_summaries)
    
    def bow_dataframe(word_freq_text):
        df = pandas.DataFrame(list(word_freq_text.items()), columns=['Word', 'Count'])
        # Sorted list with top 5 words
        top_5_words = df.sort_values(by='Count', ascending=False).head(5)
        return top_5_words

    df_reviews = bow_dataframe(frequent_reviews)
    print("\033[1mMost common words in reviews:\033[0m")
    print(df_reviews) # prints the most frequents words of the column reviews
    print("\n") # adds a break

    df_summaries = bow_dataframe(frequent_summaries)
    print("\033[1mMost common words in summaries:\033[0m")
    print(df_summaries) #  prints the most frequents words of the column summaries
    print("\n") # adds a break

    def tfidf_vectorize_as_single_document(token_lists):
        
        # Convert token lists into strings and combine them into a single document
        combined_text = ' '.join([' '.join(tokens) for tokens in token_lists])

        # Creation and application of the TfidfVectorizer
        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        tfidf_matrix = vectorizer.fit_transform([combined_text])

        # Convert the TF-IDF matrix into a DataFrame
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

        return tfidf_df

    review_tfidf_df = tfidf_vectorize_as_single_document(cleaned_reviews)
    summary_tfidf_df = tfidf_vectorize_as_single_document(cleaned_summaries)

    def transform_and_sort_tfidf(tfidf_df):
        # Transformation of the DataFrame
        transformed_df = tfidf_df.T.reset_index()
        transformed_df.columns = ['Word', 'Value']

        # Sorting the DataFrame in descending order by 'Value'
        sorted_df = transformed_df.sort_values(by='Value', ascending=False)

        return sorted_df

    sorted_review_tfidf = transform_and_sort_tfidf(review_tfidf_df)
    print("\033[1mWords in Column 'Review' after TF-IDF transformation:\033[0m")
    print(sorted_review_tfidf.head())
    print("\n") # adds a break

    sorted_summary_tfidf = transform_and_sort_tfidf(summary_tfidf_df)
    print("\033[1mWords in Column 'Summary' after TF-IDF transformation:\033[0m")
    print(sorted_summary_tfidf.head())
    print("\n") # adds a break

    ## Gensim - LDA Coherence Score
    def run_lda_analysis(text_list, num_topics):
        # Create a Gensim dictionary
        dictionary = corpora.Dictionary(text_list)  

        # Create a Gensim Corpus
        corpus = [dictionary.doc2bow(text) for text in text_list]
        
        # Train the LDA model
        lda_model = LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary, random_state=100, passes=10)
        
        # Calculation of the Coherence Score
        coherence_model_lda = CoherenceModel(model=lda_model, texts=text_list, dictionary=dictionary, coherence='c_v')
        coherence_lda = coherence_model_lda.get_coherence()

        print(f'\nCoherence Score ({num_topics}-topics): ', coherence_lda)
        return lda_model, coherence_lda

    # calculation coherence score for column 'Reviews' with 8 topics
    lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 8)

    # calculation coherence score for column 'Summaries' with 8 topics
    lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 8)

    # Results from review (took too long on every execution of the program)
    #lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 5) 0.2471651210039798
    #lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 6) 0.2799919362448972
    #lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 7) 0.2910895543971476
    #lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 8) 0.3085074511989887
    #lda_model_review, coherence_review = run_lda_analysis(cleaned_reviews, 9) 0.29556273834970986

    # Results from summary (took too long on every execution of the program)
    #lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 5) 0.5329306042849031
    #lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 6) 0.5360185919104373
    #lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 7) 0.5505435500322134
    #lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 8) 0.573887214693374
    #lda_model_summary, coherence_summary = run_lda_analysis(cleaned_summaries, 9) 0.5465979486599257

    ## LDA Review + Summary
    def perform_lda(text_list, n_topics=5, n_top_words=10):
        # Create and apply the TfidfVectorizer
        vectorizer = TfidfVectorizer()
        text_tfidf = vectorizer.fit_transform(text_list)

        # Create and apply the LDA
        lda = LatentDirichletAllocation(n_components=n_topics, random_state=0)
        lda.fit(text_tfidf)

        # Display the top words for each topic
        feature_names = vectorizer.get_feature_names_out()
        for topic_idx, topic in enumerate(lda.components_):
            print(f"Thema {topic_idx + 1}:")
            print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
            print()

    review_strings = [' '.join(cleaned_review) for cleaned_review in cleaned_reviews]
    summary_strings = [' '.join(cleaned_summary) for cleaned_summary in cleaned_summaries]

    print("\n") # adds a break
    print("\033[1mTopic modeling for 'Reviews' using LDA:\033[0m")
    perform_lda(review_strings)
    print("\033[1mTopic modeling for 'Summaries' using LDA:\033[0m")
    perform_lda(summary_strings)

if __name__ == '__main__':
    main()


# In[ ]:




