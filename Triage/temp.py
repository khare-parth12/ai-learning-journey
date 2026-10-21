import math


def softmax(scores):
    exps = {word: math.exp(score) for word, score in scores.items()}
    total = sum(exps.values())
    return {word: e / total for word, e in exps.items()}

# made-up scores for the word after "The cat sat on the"
scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}