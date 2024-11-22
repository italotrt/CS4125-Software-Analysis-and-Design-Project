import random

from sklearn.ensemble import RandomForestClassifier

from model.models.base import BaseModel

seed = random.randint(1, 1000)

class RandomForest(BaseModel):
    def __init__(self) -> None:
        super(RandomForest, self).__init__()
        self.model = RandomForestClassifier(n_estimators=1000, random_state=seed, class_weight='balanced_subsample')

    def train(self, X, y) -> None:
        print(f"Training {self.__class__.__name__} model...")
        self.model.fit(X, y)

    def predict(self, X) -> list:
        print(f"Predicting using {self.__class__.__name__}...")
        predictions = self.model.predict(X)
        return predictions

    def __str__(self):
        return "random_forest"