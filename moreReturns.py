# returns a tuple

def multiple_returns(sentence):

    t = ()
    if len(sentence) == 0:
        sentence[0] = None

    t = (len(sentence), sentence[0])
    return t


sentence = "At school, I learnt C!"

length, first = multiple_returns(sentence)

print("Length: {:d} - First character: {}".format(length, first))
