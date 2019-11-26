# Nadaljevalni tečaj analitike podatkov v Python-u (Analitika 2)

Repozitoriji za tečaj: Nadaljevalni tečaj analitike podatkov v Python-u (Analtika 2)

## Datumi izvajanja:
- Termin 1: Torek, 1.10.2019 ob 16:00
- Termin 2: Torek, 8.10.2019 ob 16:00
- Termin 3: torek, 15.10.2019 ob 16:00
- Termin 4: torek, 22.10.2019 ob 16:00
- Termin 5: torek, 29.10.2019 ob 16:00
- Termin 6: torek, 5.11.2019 ob 16:00
- Termin 7: torek, 12.11.2019 ob 16:00
- Termin 8: torek, 19.11.2019 ob 16:00
- Termin 9: torek, 26.11.2019 ob 16:00
- Termin 10: torek, 3.12.2019 ob 16:00
- Terin rezerva: torek, 10.12.2019 ob 16:00
- Izpit: 17.12.2019 (predlog, se dogovorimo)


## Ocenjevanje
- **+ 20%** (dodatne točke) - Domače vaje
- **100%** Praktičen izpit

## Vsebina

### Del 1: Pandas - Time Series
- The data
    - Getting the data
- Time series data structures
- Creating a time series DataFrame
- Time-based indexing
- Visualizing time series data
- Customizing time series plots
- Seasonality
- Frequencies
- Resampling
- Rolling windows
- Trends
- (DN) 01_Pandas_Time_Series_DN

### Del 2: Pandas - Categorical Data
- Background and Motivation
- Categorical Type in pandas
- Better performance with categoricals
- Categorical Methods
- Example: Using The Pandas Category Data Type
    - Data Preparation
    - Performance
    - Watch Outs
    - General Guidelines
- (D) Dodatek: Categorical data

### Del 3: Pandas - Data Cleaning napredno
- Working With Strings In Pandas
    - Data
    - Using Apply to Transform Strings
    - Vectorized String Methods
        - Exploring Missing Values with Vectorized String Methods
- Regular Expressions in Pandas
    - The Regular Expression Module
    - Finding Specific Words in Strings
    - Using Regular Expressions to Select Data
    - Import new dataset
    - Quantifiers
    - Character Classes
    - Raw strings
    - Extracting Substrings from a Series with Capture Groups
    - Using Flags to Modify Regex Patterns
    - Primer: Create a frequency table of the different capitalizations of SQL
    - Primer: Versions of Python
    - Primer: Extracting URL Parts
        - Using Named Capture Groups
- Working With Missing Data
    - Introduction
        - Why does missing data exist?
        - Workflow for treating missing values
    - Data
    - Detecting & Identifying Missing Data
        - Replacing hidden missing values
        - Analyzing missingness percentage
    - Visualizing Missing Data
    - Missingness Patterns
    - Handle Missing Values 
        - Dropping Rows 
        - Imputation Techniques
            - Mean & median imputation
            - Mode and constant imputation
            - Visualize imputations
        - Dropping Columns
        - Using Data From Additional Sources to Fill in Missing Values
        - Vaja: Removing all missing values from World Happiness Reports datasets
    - Missing time-series data
        - Impute with Forward-fill & Backfill 
        - Impute with interpolate method
- (D) Dodatek: Working with missing data
- (DN) 03_Pandas_Data_Cleaning_napredno

### Del 4: Delo s podatkovnimi bazami in SQL
- Introduction to Databases
- Data
- SQLite - Commands
    - Formatting Output
    - Querying the database schema
- Introduction to SQL
    - SELECT
    - Filtering Rows Using WHERE
    - Multiple Filter Criteria Using AND
    - Returning One of Several Conditions With OR
    - Grouping Operators With Parentheses
    - Ordering Results Using ORDER BY
- Work with the SQLite database using Python
    - Connecting to the Database
        - Closing the Database Connection
        - SQLite Python: Creating a New Database
    - Introduction to Cursor Objects and Running a Query
        - Shortcut for Running a Query
        - SQLite Python: Querying Data
    - Fetching a Specific Number of Results
- SQLAlchemy
    - Installation
    - SQLAlchemy version
    - Connecting
        - Database Urls
    - Execute SQL statements
- Working with databases and Pandas
    - Importing data from database
        - read_sql_table
        - read_sql_query
    - Writing a DataFrame to a SQL database
        - to_sql
        - SQL data types
    - Primer: Uvoz podatkov iz CSV dokumenta v SQL bazo
- Dodatna orodja
    - ipython-sql

### Del 5: Procesiranje velikih datasetov v pandas-u
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
- Druga zanimiva orodja
    - Dask  

### Del 6: Optimizacija kode za velike datasete
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

### Del 7: Uvod v strojno učnje - Osnove
- Uvod v strojno učenje
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
- Evaluating Model Performance
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

### Del 8: Uvod v strojno učnje - Nadaljevanje
- Instance Based Learning Vs. Model Based Learning
- Linear Regression
    - Introduction To The Data
    - Simple Linear Regression
    - Using Scikit-Learn To Train And Predict
    - Multiple Linear Regression
    - Missing Values
    - Correlating Feature Columns With Target Column
    - Correlation Matrix Heatmap
    - Train And Test Model
    - Removing Low Variance Features
    - Final Model
- Exercise: Predicting House Sale Prices
    - Introduction
    - Feature Engineering
        - Missing Values
        - Transforming Improper Numerical Features
    - Feature Selection
        - Categorical Features
        - Dummy Coding
    - Train And Test
    - Using the model
        - Testing different thresholds

### Del 9: Procesi v analitiki podatkov
- Designing Machine Learning Workflows
    - Feature engineering
    - Model selection
    - Grid search CV for model complexity
    - Categorical encodings
    - Feature transformations
    - Bringing it all together
- Exploring the Bitcoin Cryptocurrency Market
    - Bitcoin. Cryptocurrencies.
    - Full dataset, filtering, and reproducibility
    - Discard the cryptocurrencies without a market capitalization
    - How big is Bitcoin compared with the rest of the cryptocurrencies?
    - Making the plot easier to read and more informative
    - What is going on?! Volatility in cryptocurrencies
    - Well, we can already see that things are a bit crazy
    - Ok, those are... interesting. Let's check the weekly Series too.
    - How small is small?
    - Most coins are tiny
- Predicting Credit Card Approvals
    - Credit card applications
    - Inspecting the applications
    - Handling the missing values (part i)
    - Handling the missing values (part ii)
    - Handling the missing values (part iii)
    - Preprocessing the data (part i)
    - Splitting the dataset into train and test sets
    - Preprocessing the data (part ii)
    - Fitting a logistic regression model to the train set
    - Making predictions and evaluating performance
    - Grid searching and making the model perform better
    - Finding the best performing model
    
### Del 10: Spark

### Del 11: Primer izpita


## Uporabne strani
- [pandas - User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Open Machine Learning Course mlcourse.ai](https://mlcourse.ai/)
- [KDnuggets](https://www.kdnuggets.com/)
- [DEV](https://dev.to/)
- [DZone](https://dzone.com)
- [Medium](https://medium.com/)
- [Towards Data Science](https://towardsdatascience.com/)

