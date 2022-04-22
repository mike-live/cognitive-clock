# Cognitive Clock

We introduce model of Cognitive Clock that estimates age of an individual based on the performance in the 3 cognitive tests:
1. Sensomotor test. Reversed letters
2. Sensomotor test. Arithmetic expressions
3. Campimetry test. Object disrimination in different hues.

## Cognitive tests description

The detailed description can be found in the supplementary materials of the paper.

Scheme of the campimetry test:
![campimetry](/images/campimetry_test_scheme.pdf "Campimetry")

Scheme of the sensomotor test:
![sensomotor](/images/sensomotor_test_scheme.pdf "Sensomotor")

## ApWay platform

The results of cognitive tests can be obtained on the ApWay platform:
http://platform.apway.ru/

To use the platform in the Laboratory one should create an "Expert" account, add a new participant and assign the 3 tests from the pre-selected set.
Next, participant takes part in the testing. Finally, an expert downloads results of tests and got 3 csv files.
Examples of cognitive test results are presented in the `data` folder.

## Getting Started
### Prerequisites

- Python 3.8+
- pip
- sklearn
- pandas
- numpy
- pickle
- pathlib2

### Installing

Clone repo:
```
git clone https://github.com/mike-live/cognitive-clock
```

### Run

The cognitive age is computed for cognitive test results stored in the folder `data`. The format of those files is presented in the following section (Format of csv files). 

To run the model:
```
python cognitive_clock_run.py data
```

Output for example cognitive test results:
```
Cognitive age: 25.180906058836847
```

## Format of csv files

### Sensomotor tests. Arithmetic expressions (SM1). Reversed letters (SM2)

Resulting file (See for ex. `data/SM1.csv` and `data/SM2.csv`) consists of the following columns:
\# -- the number of stimulus presentation
Stimul -- the ID of stimulus
Goal -- the goal of participant: 0 - shouldn't click, 1 -- should click
Duration -- the duration of the stimulus presentation (ms)
Interval -- the interval between two stimulus presentations (ms)
Show -- the time of stimulus appearing from the test start (ms)
Hide -- the time of stimulus disappearing from the test start (ms)
Down -- the time of mouse down from the test start (ms)
Up -- the time of mouse up from the test start (ms)
SMR -- sensorimotor reaction; difference time between Up and Show -- duration of dicision making and response time (ms)
MR -- motor reaction; difference time between Up and Down -- duration of time mouse were pressed (ms)
ERR_1 -- the number of missed correct stimuli
ERR_2 -- the number of double clicks
ERR_3 -- the number of clicks on incorrect stimuli

### Campimetry test

Resulting file (See for ex. `data/CM.csv`) consists of the following columns:
Stimul -- the ID of stimulus
H -- the starting hue of the background and object in the HSL model (0-360)
H+ -- the finishing hue of the object given by participant to recognize object (normal campimetry task)
dH+ -- the number of shades added by participant to recognize object (difference between H+ and H)
H- -- the finishing hue of the object given by participant to recognize object (inverse campimetry task)
dH- -- the number of shades until object hue matches background hue (difference between H- and H)
t+ -- the time of solving normal campimetry task
t- -- the time of solving inverse campimetry task
ERR -- the number of incorrect object recognition
ERR_LIM -- number of clicks after hue of the object is matches background hue

## Citation

Krivonosov M.I., Kondakova E.V., Polevaya S.A., Franceschi C., Ivanchenko M.V., Vedunova M.V. A new cognitive clock matching phenotypic and epigenetic ages. [Preprint.] April 22, 2022.

## Authors

* Krivonosov Mikhail -- *Model implementation, data analysis* [mike_live](https://github.com/mike_live)
* Kondakova Elena -- *Participants recruitment, study organisation*
* Polevaya Sofia -- *ApWay platform access, the cognitive tests inventor*
* Franceschi Claudio -- *Project vision*
* Ivanchenko Mikhail -- *Project vision*
* Vedunova Maria -- *Project vision*

## Acknowledgments

We acknowledge support by the grant of the Ministry of Education and Science of the Russian Federation Agreement No. 075-15-2019-871.