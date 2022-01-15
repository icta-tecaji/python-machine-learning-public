# Del 2: Nadzorovano učenje

## Vsebina

### Uvod v nadzorovano učenje
- Classification and Regression
    - Classification
    - Regression
- Generalization, Overfitting, and Underfitting
- Relation of Model Complexity to Dataset Size

### k-Nearest Neighbors
- k-Neighbors classification
    - Analyzing KNeighborsClassifier
- k-neighbors regression
    - Analyzing KNeighborsRegressor
    - Primer: AirBnB dataset
- Parameters
- Strengths
- Weaknesses
- Conclusion

### Linear Models
- Linear models for regression
    - Linear regression
    - Ridge regression
    - Lasso
- Linear models for binary classification
- Linear models for multiclass classification
- Strengths, weaknesses, and parameters

### Naive Bayes Classifiers
- Gaussian Naive Bayes
- Example: Multinomial Naive Bayes - Classifying Text
- Parameters
- Strengths
- Weaknesses
- Usage

### Decision Trees
- Building decision trees
- Controlling complexity of decision trees
- Analyzing decision trees
- Feature importance in trees
- Decision trees for regression
- Strengths, weaknesses, and parameters

### Ensembles of Decision Trees
- Random forests
    - Building random forests
    - Analyzing random forests
    - Strengths, weaknesses, and parameters
    - Example: Random Forest for Classifying Digits
- Random Forest Regression
- Gradient boosted regression trees (gradient boosting machines)
    - Strengths, weaknesses, and parameters

### Kernelized Support Vector Machines
- Linear models and nonlinear features
- The kernel trick
- Understanding SVMs
- Tuning SVM parameters
- Preprocessing data for SVMs
- Strengths, weaknesses, and parameters 

### Uncertainty Estimates from Classifiers
- The Decision Function
- Predicting Probabilities
- Uncertainty in Multiclass Classification

## Pregled modelov
- **Nearest neighbors:** For small datasets, good as a baseline, easy to explain.
- **Linear models:** Go-to as a first algorithm to try, good for very large datasets, good for very highdimensional data.
- **Naive Bayes:** Only for classification. Even faster than linear models, good for very large datasets and high-dimensional data. Often less accurate than linear models.
- **Decision trees:** Very fast, don’t need scaling of the data, can be visualized and easily explained.
- **Random forests:** Nearly always perform better than a single decision tree, very robust and powerful. Don’t need scaling of data. Not good for very high-dimensional sparse data.
- **Gradient boosted decision trees:** Often slightly more accurate than random forests. Slower to train but faster to predict than random forests, and smaller in memory. Need more parameter tuning than random forests.
- **Support vector machines:** Powerful for medium-sized datasets of features with similar meaning. Require scaling of data, sensitive to parameters.

![alt text](https://scikit-learn.org/stable/_static/ml_map.png)
Vir: https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html


## Priporočila
- Pri delu z novimi podatki je priporočeno začeti z enostavnim modelom (npr. linearni modeli, naive Bayes, nearest neighbors classifier) ter pridobiti rezultate. Šele po boljšem razumevanju podatkov, se odločimo za gradnjo kompleksnješih modelov (npr, random forests, gradient boosted decision trees, SVMs).
