# Sentiment Analysis

This project is my introduction to Sentiment analysis. Hopefully some cool stuff will result from this!

## Exploring the VADER model:

The vader model uses a lexical approach, where lexical features are mapped to a sentiment score in a dictionary. This even includes colloquialisms such as "LOL" or ":/". The VADER sentiment dictionary was created by a collection of human raters and their average score for each word. Defining the sentiment of a sentence is done by adding the scores of the lexical units and normalizing the result.

VADERs 5 Heuristics:
1. Punctuation
    - Exclamantion marks change the intensity of a sentence
    - E.g. Exclamation marks amplify the sentiment of a sentence proportional to the number of exclamation marks
2. Capitalization
    - Capitalization changes the intensity of a word
    - E.g. The model increments or decrements the sentiment score of a word if it capitalized
3. Degree Modifiers
    - VADER maintians a booster dictionary, which can boost or dampen the score of a word
    - E.g. The "sort of" modifier would dampen the word "cool", "sort of cool"
4. Polarity shift
    - VADER essentially has a but checker
    - E.g. "I enjoy this but i would rather do that" shows a shift in polarity after the "but" keyword
5. examining the tri-gram before a sentiment-laden lexical feature to catch polarity negation
    - Negation is captured by multiplying the sentiment score of the sentiment-laden lexical feature by an empirically-determined value 0.74

*NOTE: The VADER model is more effective on short texts*

TLDR: The VADER model is a look up table, using 5 different heuristics to determine the sentiment of a sentence.