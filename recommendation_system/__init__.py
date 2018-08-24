from .most_popular import Popular
from .user_based import Similarity


class Recommender(Popular, Similarity):
    def __init__(self, dataset):
        self.dataset = dataset
        Popular.__init__(self)
        Similarity.__init__(self)
