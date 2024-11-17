from abc import ABC, abstractmethod

from scipy.stats import studentized_range_gen

from structs.objects import Email

# Strategy Pattern
class ClassificationStrategy(ABC):
    @abstractmethod
    def classify(self, email: Email):
        pass

class NaiveBayesClassifier(ClassificationStrategy):
    def classify(self, email: Email):
        # Logic
        print("Classifying with Naive Bayes")
        return "spam"

class SVMClassifier(ClassificationStrategy):
    def classify(self, email: Email):
        # Logic
        print("Classifying with SVM")
        return "not spam"

class DecisionTreeClassifier(ClassificationStrategy):
    def classify(self, email: Email):
        # Logic
        print("Classifying with Decision Tree")
        return "spam"

class RandomForestClassifier(ClassificationStrategy):
    def classify(self, email: Email):
        # Logic
        print("Classifying with Random Forest")
        return "not spam"

# Strategy Pattern
class ClassificationContext:
    strategy: ClassificationStrategy

    def __init__(self, strategy: ClassificationStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: ClassificationStrategy) -> None:
        """Allows switching the strategy dynamically."""
        self._strategy = strategy

    def classify_email(self, email: Email) -> str:
        """Classifies an email using the current strategy."""
        return self._strategy.classify(email)

# Factory Pattern
class ClassificationContextFactory:
    @staticmethod
    def create_context(strategy: str) -> ClassificationContext:
        match strategy:
            case "naive_bayes":
                return ClassificationContext(NaiveBayesClassifier())
            case "svm":
                return ClassificationContext(SVMClassifier())
            case "decision_tree":
                return ClassificationContext(DecisionTreeClassifier())
            case "random_forest":
                return ClassificationContext(RandomForestClassifier())
            case _:
                raise ValueError("Invalid strategy")