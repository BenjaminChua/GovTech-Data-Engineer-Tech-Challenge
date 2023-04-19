# Section 5: Machine Learning

## Instructions to run
1. Env set up using requirements.txt
  ```
  pip install -r requirements.txt
  ```
2. Run _car-price-prediction.ipynb_

## Data Preprocessing
Since the raw data was categorical and in string format, it was transformed into integers(numeric), which is readable by the ML algorithms.

The pre-processed data is then split into train-test sets with a split of 80-20.

The feature 'persons' was removed from training as the test sample given did not specify it.

## Model Selection
As the training dataset only consists 1,382 records, a machine learning model such as Random Forest would be sufficient and suitable.

## Hyperparameter Tuning
Hyperparameters of the Random Forest model was tuned using Grid Search and 10-Fold Cross Validation.

## Model Results
The model produced an average accuracy of 36% which is higher than the random benchmark of 25% (1/4).

## Test sample
Given the test sample:
- Maintenance = High 
- Number of doors = 4 
- Lug Boot Size = Big 
- Safety = High 
- Class Value = Good 

The buying price was predicted as *low*.