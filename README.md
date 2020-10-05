# Nadaljevalni tečaj analitike podatkov v Python-u (Analitika 2)

Repozitoriji za tečaj: Nadaljevalni tečaj analitike podatkov v Python-u (Analtika 2)

## Datumi izvajanja:
- Termin 1: Ponedeljek, 5.10.2020 ob 16:15


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


## Uporabne strani
- [pandas - User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Open Machine Learning Course mlcourse.ai](https://mlcourse.ai/)
- [KDnuggets](https://www.kdnuggets.com/)
- [DEV](https://dev.to/)
- [DZone](https://dzone.com)
- [Medium](https://medium.com/)
- [Towards Data Science](https://towardsdatascience.com/)

