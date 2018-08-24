from collections import defaultdict, Counter
import math

'''
aggregate function 合計函數
collaborative filtering 協同過濾

'''


class Rcommender:
    def __init__(self, dataset):
        self.dataset = dataset

    def _popular_calc(self):
        return Counter(ele for data in self.dataset for ele in data).most_common()

    def popular(self, data, recommendations=None):
        return [(ele, freq) for ele, freq in self._popular_calc() if ele not in data][:recommendations]

    def _dot(self, a, b):
        return sum(map(lambda ai, bi: ai * bi, a, b))

    def _unique(self):
        return sorted(tuple({ele for data in self.dataset for ele in data}))

    def _similarity_calc(self, a, b):
        return self._dot(a, b) / math.sqrt(self._dot(a, a) * self._dot(b, b))

    def _similarity_vector(self, data):
        return [1 if ele in data else 0 for ele in self._unique()]

    def _similarity_map(self):
        return map(self._similarity_vector, self.dataset)

    def _similarity_matrix(self):
        return [[self._similarity_calc(a, b) for b in self._similarity_map()] for a in self._similarity_map()]


