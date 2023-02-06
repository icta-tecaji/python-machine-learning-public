# Del 2: Nadzorovano učenje

## Vsebina

### Uvod v nadzorovano učenje
- Classification and Regression ✅
    - Classification ✅
    - Regression ✅
- Generalization, Overfitting, and Underfitting ✅
- Relation of Model Complexity to Dataset Size ✅

### Linear models for regression
- Jupyter Widgets ✅
- Linear regression theory ✅
- Linear regression with sklearn ✅
- Multiple linear regression ✅
- Strengths and weaknesses ✅

### Feature scaling
- What is Feature Scaling? ✅
- When to scale your data? ✅
- When scaling your data is not necessary? ✅
- Different types of features scaling ✅
    - Normalization ✅
    - Standardization ✅
    - Robust Scalar ✅
    - Scaling to unit length ✅
- Applying Scaling Transformations ✅
- Scaling Training and Test Data the Same Way ✅
- The Effect of Preprocessing on Supervised Learning ✅
- Tips ✅

### Regularization
- Overfitting and Underfitting ✅
    - What is Overfitting? ✅
    - What is Underfitting? ✅
- Bias And Variance ✅
    - Errors in Machine Learning ✅
    - What is Bias? ✅
    - What is Variance? ✅
- Bias-Variance Tradeoff ✅
- Regularization ✅
    - Ridge Regression ✅
    - Lasso Regression ✅
    - Elastic Net Regression ✅
- Strengths, weaknesses, and parameters ✅

### Polynomial regression
- Why Polynomial Regression? ✅
- What is Polynomial Regression? ✅
- Polynomial Regression with sklearn ✅
- Disadvantages of polynomial regression ✅

### Linear models for classification
- Intro to classification ✅
- Logistic Regression ✅
- Regularization for Logistic Regression ✅
- Uncertainty Estimates from Classifiers ✅
    - The Decision Function ✅
    - Predicting Probabilities ✅
- Binary Logistic Regression in Scikit-learn ✅
- Linear models for multiclass classification ✅
- Uncertainty in Multiclass Classification ✅
- Multinomial Logistic Regression in Scikit-learn ✅

### Example: North American pumpkin prices
- Visualize and clean data in preparation for ML ✅
- Build a regression model using Scikit-learn ✅
- Logistic regression to predict categories ✅

### k-Nearest Neighbors
- k-Neighbors classification ✅
    - Analyzing KNeighborsClassifier ✅
- k-neighbors regression ✅
    - Analyzing KNeighborsRegressor ✅
    - Primer: AirBnB dataset ✅
- Parameters ✅
- Strengths ✅
- Weaknesses ✅
- Conclusion ✅

### Naive Bayes Classifiers
- Gaussian Naive Bayes ✅
- Example: Multinomial Naive Bayes - Classifying Text ✅
- Parameters ✅
- Strengths ✅
- Weaknesses ✅
- Usage ✅

### Kernelized Support Vector Machines
- Linear models and nonlinear features ✅
- The kernel trick ✅
- Understanding SVMs ✅
- Tuning SVM parameters ✅
- Preprocessing data for SVMs ✅
- Strengths, weaknesses, and parameters ✅

### Decision Trees
- Building decision trees ✅
- Measuring purity ✅
- Build a decision tree model using Scikit-learn ✅
- Controlling complexity of decision trees ✅
- Analyzing decision trees ✅
- Feature importance in trees ✅
- Using one-hot encoding of categorical features ✅
- Continuous valued features ✅
- Example: Heart dataset ✅
- Decision trees for regression ✅
- Strengths, weaknesses, and parameters ✅

### Vaja: Phone prices

## Pregled modelov
- **Nearest neighbors:** For small datasets, good as a baseline, easy to explain.
- **Linear models:** Go-to as a first algorithm to try, good for very large datasets, good for very highdimensional data.
- **Naive Bayes:** Only for classification. Even faster than linear models, good for very large datasets and high-dimensional data. Often less accurate than linear models.
- **Decision trees:** Very fast, don’t need scaling of the data, can be visualized and easily explained.
- **Gradient boosted decision trees:** Often slightly more accurate than random forests. Slower to train but faster to predict than random forests, and smaller in memory. Need more parameter tuning than random forests.
- **Support vector machines:** Powerful for medium-sized datasets of features with similar meaning. Require scaling of data, sensitive to parameters.

![alt text](https://scikit-learn.org/stable/_static/ml_map.png)
Vir: https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html


## Priporočila
- Pri delu z novimi podatki je priporočeno začeti z enostavnim modelom (npr. linearni modeli, naive Bayes, nearest neighbors classifier) ter pridobiti rezultate. Šele po boljšem razumevanju podatkov, se odločimo za gradnjo kompleksnješih modelov (npr, random forests, gradient boosted decision trees, SVMs).
