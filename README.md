# Nadaljevalni tečaj analitike podatkov v Python-u (Analitika 2)

Repozitoriji za tečaj: Nadaljevalni tečaj analitike podatkov v Python-u (Analtika 2)

## Datumi izvajanja:
- Termin 1: Ponedeljek, 5.10.2020 ob 16:15
- Termin 2: Ponedeljek, 12.10.2020 ob 16:15
- Termin 3: Ponedeljek, 19.10.2020 ob 16:15
- Termin 4: Ponedeljek, 26.10.2020 ob 16:15
- Termin 5: Ponedeljek, 2.11.2020 ob 16:15
- Termin 6: Ponedeljek, 9.11.2020 ob 16:15
- Termin 7: Ponedeljek, 16.11.2020 ob 16:15

## Ocenjevanje
- **+ 20%** (dodatne točke) - Domače vaje
- **100%** Praktičen izpit

## Vsebina

### Del 1: Ponovitev

### Del 2: Procesiranje velikih datasetov v pandas-u
- Introduction & Data
- Optimizing Dataframe Memory Footprint
    - The Internal Representation of a Dataframe
    - Dataframe Memory Footprint
        - Float Columns
        - Object Columns
        - True Memory Footprint
    - Optimizing Numeric Columns with Subtypes
        - Integer Columns
        - Float Columns
    - Converting To DateTime
    - Converting to Categorical
- Selecting Types While Reading the Data In
    - Example: MoMA dataset
- Processing Dataframes in Chunks
    - Processing Chunks
    - Counting Across Chunks
    - Batch Processing
    - Optimizing Performance
    - Counting Unique Values
- Analizing big files with Pandas and SQLite
    - Computing Primarily in SQL
    - Computing Primarily in Pandas
    - Reading in SQL Results Using Chunks
- Vaja: Primer analize velikega dataseta
- More file formats
    - Parquet
    - Avro
    - Feather
    - HDF5
    
### Del 3: Optimizacija kode za velike datasete
- CPU Bound Programs
    - Bounds vs Limitations
    - Primer optimizacije
- I/O Bound Programs
    - Profiling an I/O bound task
    - I/O Bounds
    - Blocking Tasks
    - Parallel Execution
    - Thread Blocking
    - Joining Threads
    - Locking
    - Thread Safety
- Optimizing Python Code with pandas
    - Basic Looping
    - Select columns and rows efficiently
    - Uporaba biult-in funkciji       
    - Joining on indexes is faster than joining on columns
- PRIMER: Pohitritev pandas kode
    - Naloga
    - Priprava podatkov
    - 1) Simple Looping Over Pandas Data
    - 2) Looping with .itertuples() and .iterrows()
    - 3) Pandas’ .apply()
    - 4) Selecting Data With .isin()
    - 5) Pandas’ pd.cut() function
    - 6) Using NumPy
    - Prevent Reprocessing with HDFStore
    - Povzetek
- Drugi nasveti
    - Numba
    - pandas.eval() for Efficient Operations
    
### Del 4: Strojno učenje: K-Nearest Neighbors
- Introduction to K-Nearest Neighbors
    - Problem definition
    - Introduction to the data
    - K-nearest neighbors
    - Euclidean distance
    - Calculate distance for all observations 
    - Randomizing, and sorting
    - Average price
    - Function to make predictions
- Evaluating Model Performance
    - Testing quality of predictions
    - Error Metrics
    - Mean Squared Error
    - Training another model
    - Root Mean Squared Error
    - Comparing MAE and RMSE
- Multivariate K-Nearest Neighbors
    - Removing features
    - Handling missing values
    - Normalize columns
    - Euclidean distance for multivariate case
    - Introduction to scikit-learn
    - Fitting a model and making predictions
    - Calculating MSE using Scikit-Learn
    - Using more features
    - Using all features
- Hyperparameter Optimization
    - Expanding grid search
    - Visualizing hyperparameter values
    - Varying features and hyperparameters
    - Practice the workflow
- Cross Validation
    - Holdout Validation
    - K-Fold Cross Validation
    - First iteration
    - Function for training models
    - Performing K-Fold Cross Validation Using Scikit-Learn
    - Exploring Different K Values
    - Bias-Variance Tradeoff 
- Vaja: Predicting Car Prices
    - Introduction To The Data Set
    - Data Cleaning
    - Univariate Model
    - Multivariate Model
    - Hyperparameter Tuning 
    
### Del 5: Strojno učenje: Linearna regresija
- The Linear Regression Model
    - Instance Based Learning Vs. Model Based Learning
    - Introduction To The Data
    - Simple Linear Regression
    - Least Squares
    - Using Scikit-Learn To Train And Predict
    - Making Predictions
    - Multiple Linear Regression
- Feature Selection
    - Missing Values
    - Correlating Feature Columns With Target Column
    - Correlation Matrix Heatmap
    - Train And Test Model
    - Removing Low Variance Features
    - Final Model    
- Overfitting
    - Introduction
    - Bias and Variance
    - Bias-variance tradeoff
    - Multivariate models
    - Cross validation
    - Plotting cross-validation error vs. cross-validation variance
- Processing And Transforming Features
    - Introduction
    - Categorical Features
    - Dummy Coding
    - Transforming Improper Numerical Features
    - Missing Values
    - Imputing Missing Values
- Vaja: Predicting House Sale Prices
    - Introduction
    - Feature Engineering
    - Feature Selection
    - Train And Test
    - Finding best result



## Uporabne strani
- [pandas - User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Open Machine Learning Course mlcourse.ai](https://mlcourse.ai/)
- [KDnuggets](https://www.kdnuggets.com/)
- [DEV](https://dev.to/)
- [DZone](https://dzone.com)
- [Medium](https://medium.com/)
- [Towards Data Science](https://towardsdatascience.com/)

