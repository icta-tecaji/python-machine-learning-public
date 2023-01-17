# Del 1: Uvod v strojno učenje

## Vsebina
- Teoretičen uvod v strojno učenje (v priloženem PPT) ✅
- Workflow of a machine learning project ✅
- What is machine learning? ✅
- What are machine learning models? ✅
- Why Machine Learning? ✅
- Problems Machine Learning Can Solve ✅
- scikit-learn ✅
- A First Application: Classifying Iris Species ✅
    - The data
    - Training and Testing Data
    - Look at Your Data
    - Building Your First Model: k-Nearest Neighbors
    - Making Predictions
    - Evaluating the Model
  
## Priprava okolja
### Linux (Ubuntu 20)
- Po potrebi namestimo git in Python:
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-2-public.git`
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
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-2-public.git`
- Ustvarimo virtualno okolje: `python -m venv .venv`
- Aktiviramo virtualno okolje: `.venv\Scripts\activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`

### Mac OS
- Po potrebi namestimo git in Python:
    - https://git-scm.com/download/mac
    - https://www.python.org/downloads/macos/
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-2-public.git`
- Ustvarimo virtualno okolje: `python3 -m venv .venv`
- Aktiviramo virtualno okolje: `source .venv/bin/activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`