# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 22:35:00 2020

@author: Saad Malik
"""
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
nltk.download('stopwords') 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

class coverTuner():
    
    stop_words = set(stopwords.words('english'))
    
    def __init__(self, data):
        self.data = data
        self.lowerCase = data.lower()
        
    def display(self):
        return self.data
    
    def Word_count(self):
        tokenizer = RegexpTokenizer(r'\w+')
        ans = tokenizer.tokenize(self.data)
        return len(ans)
    
    def meaningfulWordsCount(self):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(self.lowerCase)
        filtered_sentence = [w for w in tokens if not w in self.stop_words]
        return len(filtered_sentence)
    
    def meani_prop(self):
        a = self.Word_count()
        b = self.meaningfulWordsCount()
        ans = (b/a)*100
        return round(ans, 1)
    
    def top_mean_words(self):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(self.lowerCase)
        filtered_sentence = [w for w in tokens if not w in self.stop_words]
        ans = nltk.FreqDist(filtered_sentence)
        ans1 = ans.most_common(5)
        li = []
        for e in ans1:
            li.append(e[0])
        string = "Target words are {}.".format(li)    
        return string
    
    def usage_i_me_my_mine(self):
        tokenizer = RegexpTokenizer(r'\w+')
        ans = tokenizer.tokenize(self.lowerCase)
        li = []
        li2 = ['i','me','my','myself']
        for e in ans:
            if e in li2:
                li.append(e)
        return len(li)
    
    def first_sing(self):
        a = self.usage_i_me_my_mine()
        b = self.Word_count()
        ans = (a/b)*100
        return round(ans, 1)
    
    global syllable_per_word
    def syllable_per_word(self):
        word = self.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count

    def syllables_count(self):
        tokenizer = RegexpTokenizer(r'\w+')
        ans = tokenizer.tokenize(self.lowerCase)
        counter = 0
        for w in ans:
            a = syllable_per_word(w)
            counter = a + counter
        return counter
    
    def sentences_count(self):
        number_of_sentences = sent_tokenize(self.data)
        return len(number_of_sentences)
    
class readability(coverTuner):
    
    def FleschReadingEase(self):
        word_count = self.Word_count()
        sentence_count = self.sentences_count()
        syllable_count = self.syllables_count()
        avg_words_p_sentence = word_count/sentence_count
        score = 0.0 
        score = 206.835 - (1.015 * (avg_words_p_sentence)) - (84.6 * (syllable_count/ word_count))
        return round(score, 2)
