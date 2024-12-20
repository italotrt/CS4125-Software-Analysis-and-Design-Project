from model.classification_context import Classifier
from model.models.k_nearest_neighbour import KNearestNeighbourModel


class KNearestNeighborsClassifier(Classifier):
    def __init__(self):
        super().__init__()
        self.model = KNearestNeighbourModel()