from collections import Counter


class Popular:
    def __init__(self, dataset):
        self.dataset = dataset

    def _popular_calc(self):
        return Counter(ele for data in self.dataset for ele in data).most_common()

    def suggest(self, data, n=5):
        suggestions = [(ele, freq) for ele, freq in self._popular_calc() if ele not in data]
        return suggestions[:n]
