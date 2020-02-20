import unittest

from sklearn.metrics import precision_score, recall_score

from src.train import prepare_data_and_train_model

class TestModelMetrics(unittest.TestCase):
    def test_model_precision_is_above_threshold(self):
        model, X_test, Y_test = prepare_data_and_train_model()
        Y_pred = model.predict(X_test)

        precision = precision_score(Y_test, Y_pred)

        self.assertGreaterEqual(precision, 0.6)
    
    def test_model_recall_is_above_threshold(self):
        model, X_test, Y_test = prepare_data_and_train_model()
        Y_pred = model.predict(X_test)

        precision = recall_score(Y_test, Y_pred)

        self.assertGreaterEqual(precision, 0.6)

if __name__ == '__main__':
    unittest.main()