from textblob import TextBlob
import nltk
import pandas as pd


"""
Input: path for dataset which is to be analyzed,
       name with which the result should be stored.
Output: Result datasets will be generated.
"""
def textblobsentiment_de_oto(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])

    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/textblob/textblob_de_oto/nonames/{}.csv'.format(file_name),encoding="latin-1")

def textblobsentiment_de_oto_names(path,file_name):
    set = pd.read_csv(path,engine="python",encoding="latin-1")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])
    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/textblob/textblob_de_oto/withnames/{}.csv'.format(file_name),encoding="latin-1")
