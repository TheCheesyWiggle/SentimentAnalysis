import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk

df = pd.read_csv("Reviews.csv")

def main():
    vader_model()

def vader_model():
    # Quick EDA
    # Shows Baises in the data set

    ax1 = df['Score'].value_counts().sort_index()\
        .plot(kind="bar", 
            title="Count of Reviews by stars",
            figsize=(10,5))
    ax1.set_xlabel('Review Stars')
    plt.show()

    # Basic NLTK stuff
    example = df['Text'][50]
    tokens = nltk.word_tokenize(example)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)

    #VADER Sentiment Scoring
    from nltk.sentiment import SentimentIntensityAnalyzer
    from tqdm import tqdm

    sia = SentimentIntensityAnalyzer()
    sia.polarity_scores(example)

    # Create a tqdm wrapper around the DataFrame's iterator
    tqdm.pandas()

    res = {}

    def process_row(row):
        text = row['Text']
        myid = row['Id']
        res[myid] = sia.polarity_scores(text)

    processed_df = df.progress_apply(process_row, axis=1)

    vaders = pd.DataFrame(res).T
    print(vaders)
    vaders.reset_index().rename(columns={'index':'Id'})
    vaders.reset_index(inplace=True)  # Inplace modification to reset index
    vaders.rename(columns={'index': 'Id'}, inplace=True)  # Rename the 'index' column to 'Id'

    # Merge vaders and df based on the 'Id' column
    merged_df = pd.merge(vaders, df, on='Id', how='left')
    #plot VADERS result

    ax2 = sns.barplot(data=merged_df, x='Score', y='compound')
    ax2.set_title('Compound Score by Amazon Star Review')
    plt.show()
    print("Vader Model Finished")

main()