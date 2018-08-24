import math
from collections import defaultdict


def dot(p, q):
    return sum(map(lambda p_i, q_i: p_i * q_i, p, q))


def similarity_calc(p, q):
    return dot(p, q) / math.sqrt(dot(p, p) * dot(q, q))


class Similarity:
    def __init__(self):
        self.unique = sorted(tuple({ele for data in self.dataset for ele in data}))
        self.matrix = [[similarity_calc(p, q) for q in self._similarity_map()] for p in self._similarity_map()]

    def _similarity_vector(self, data):
        return [1 if ele in data else 0 for ele in self.unique]

    def _similarity_map(self):
        return map(self._similarity_vector, self.dataset)

    def most_similar_set_to(self, subset):
        pairs = []
        for other_set, similarity in enumerate(self.matrix[subset]):
            if subset != other_set and similarity > 0:  # find other users
                pairs += [(other_set, similarity)]  # with nonzero similarity

        return sorted(pairs,  # sort them by most similar
                      key=lambda x: x[-1], reverse=True)

    def similar(self, subset, include_current_interests=False):
        # sum up the similarities
        suggestions = defaultdict(float)
        for other_set, similarity in self.most_similar_set_to(subset):
            for ele in self.dataset[other_set]:
                suggestions[ele] += similarity

        # convert them to a sorted list
        suggestions = sorted(suggestions.items(), key=lambda x: x[-1], reverse=True)

        # and (maybe) exclude already-interests
        if include_current_interests:
            return suggestions

        else:
            return [(suggestion, weight)  # filtering the suggestion already had
                    for suggestion, weight in suggestions if suggestion not in self.dataset[subset]]

