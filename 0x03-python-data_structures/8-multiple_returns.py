#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence and type(sentence) == str:
        return (len(sentence), sentence[0])
    elif not sentence:
        return (len(sentence), None)
