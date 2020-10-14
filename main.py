"""
Created on Tue Oct 13 01:12:38 2020

@author: Saad Malik
"""

from logic import*

with open('textForCovertuner.txt', 'r') as file:
    data = file.read().replace('\n', '')

main = readability(data)

def run():
    print("\n")
    print('Your results are below. Thank you for using CoverTuner')
    print('{} words'.format(main.Word_count()))
    print('{} meaningful words'.format(main.meaningfulWordsCount()))
    print('{} is the proportion of meaningful words'.format(main.meani_prop()))
    print(main.top_mean_words())
    print('{} is the first singular count'.format(main.usage_i_me_my_mine()))
    print('{} is the first singular proportion'.format(main.first_sing()))
    print('{} is the readability score'.format(main.FleschReadingEase()))
    print('--Complete--')

if __name__ == "__main__":  
    run()
    