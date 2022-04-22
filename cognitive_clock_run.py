from cognitive_clock import cognitive_clock
from pathlib2 import Path
import pandas as pd

if __name__ == "__main__":
    import sys
    work_dir = Path(sys.argv[1])
    separator = ';'
    T258_name = 'CM.csv'
    T274_name = 'SM1.csv'
    T278_name = 'SM2.csv'

    calculator = cognitive_clock()
    
    tests_258 = pd.read_csv(work_dir / T258_name, sep=separator)
    tests_274 = pd.read_csv(work_dir / T274_name, sep=separator)
    tests_278 = pd.read_csv(work_dir / T278_name, sep=separator)

    cognitive_age = calculator.compute_cognitive_age(tests_258, tests_274, tests_278)
    
    print('Cognitive age:', cognitive_age)

