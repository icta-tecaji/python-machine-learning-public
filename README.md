# Analitika 2: Strojno učenje v Python-u

## Zagon 
### Linux (Ubuntu 20)
- Po potrebi namestimo git in Python:
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Prenesemo repozitoriji: `git clone https://github.com/leon11s/python-analitika-2-public.git`
- Namestimo Python venv: `apt install python3.8-venv`
- Ustvarimo virtualno okolje: `python3 -m venv .venv`
- Aktiviramo virtualno okolje: `source .venv/bin/activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`
- Remote access (before running the notebook):
    - Generate the config file: `jupyter notebook --generate-config`
    - Add the following lines to the conifg:
        - `c.NotebookApp.allow_origin = '*'`
        - `c.NotebookApp.ip = '0.0.0.0'`

### Windows 10
- Po potrebi namestimo git in Python:
    - https://git-scm.com/download/win
    - https://www.python.org/downloads/windows/
- Prenesemo repozitoriji: `git clone https://github.com/leon11s/python-analitika-2-public.git`
- Ustvarimo virtualno okolje: `python -m venv .venv`
- Aktiviramo virtualno okolje: `.venv\Scripts\activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`

### Mac OS
- Po potrebi namestimo git in Python:
    - https://git-scm.com/download/mac
    - https://www.python.org/downloads/macos/
- Prenesemo repozitoriji: `git clone https://github.com/leon11s/python-analitika-2-public.git`
- Ustvarimo virtualno okolje: `python3 -m venv .venv`
- Aktiviramo virtualno okolje: `source .venv/bin/activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`

## Vsebina
### Del 1: Uvod v strojno učenje
- Why Machine Learning? 
- Problems Machine Learning Can Solve
- scikit-learn
- Essential Libraries and Tools
- A First Application: Classifying Iris Species

### Del 2: Nadzorovano učenje
- Uvod v nadzorovano učenje
- k-Nearest Neighbors
- Linear Models
- Naive Bayes Classifiers
- Decision Trees
- Ensembles of Decision Trees
- Kernelized Support Vector Machines
- Uncertainty Estimates from Classifiers



## Uporabne strani
- [Machine Learning Crash Course](https://developers.google.com/machine-learning): Google's fast-paced, practical introduction to machine learning
- [pandas - User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Open Machine Learning Course mlcourse.ai](https://mlcourse.ai/)
- [KDnuggets](https://www.kdnuggets.com/)
- [DEV](https://dev.to/)
- [DZone](https://dzone.com)
- [Medium](https://medium.com/)
- [Towards Data Science](https://towardsdatascience.com/)