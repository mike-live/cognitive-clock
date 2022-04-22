import numpy as np
import matplotlib.pyplot as plt
from pathlib2 import Path
import cognitive_tests
import pickle

class cognitive_clock:
    def __init__(self):
        self.all_info = self.load_model()

    def load_model(self, models_dir='models', model_version = '1.0', export_date = '2022-04-22'):
        model_export_path = Path(models_dir) / f'model_{model_version}_{export_date}.pkl'
        with open(model_export_path, 'rb') as file:
            all_info = pickle.load(file)
        return all_info

    def prepare_data(self, tests_258, tests_274, tests_278):
        test_258 = cognitive_tests.gen_258(tests_258)
        test_274 = cognitive_tests.gen_274(tests_274)
        test_278 = cognitive_tests.gen_278(tests_278)
        cur_tests = np.concatenate([test_258, test_274, test_278])
        return cur_tests

    def compute_cognitive_age(self, tests_258, tests_274, tests_278):
        feature_names = cognitive_tests.gen_names_258() + cognitive_tests.gen_names_274() + cognitive_tests.gen_names_278()
        
        df_model_features = self.all_info['df_model_features']
        selected_features = df_model_features['selected_features']
        model = self.all_info['model']

        cur_tests = self.prepare_data(tests_258, tests_274, tests_278)
        
        cur_tests = cur_tests[selected_features]
        xp_mean = df_model_features.mean_feature.values
        xp_sd = df_model_features.sd_feature.values

        xp = (cur_tests - xp_mean) / xp_sd
        cognitive_age = model.predict(xp.reshape(1, -1)).item()
        return cognitive_age
