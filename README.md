# fasttext_language_detection
Api for language detection


## Introduction

[Fasttext](https://fasttext.cc/blog/2017/10/02/blog-post.html) has awesome tool for language detection which is blazing fast.
This repository creates a local API using [FastAPI](https://fastapi.tiangolo.com/).

## Installation

* Install [python>=3.6](https://www.python.org/), pip

* Clone repository
In a terminal type - 
```bash
git clone https://github.com/hrushikesh-dhumal/fasttext_language_detection.git
```

* Change into repository
```bash
cd fasttext_language_detection
```

* Start virtual env
These command is for windows
```bash
python -m venv env
env\Scripts\activate.bat
```
It is different for other systems

* Install required packages
```bash
pip install -R requirements.txt
```

* Create a model folder and copy the model from [here](https://fasttext.cc/docs/en/language-identification.html)

* Start the server by
```bash
uvicorn main:app --reload
```

* Stop the server by pressing `Control + C` on windows


## Ouput
Open your browser at http://127.0.0.1:8000/language_detect?text=how are you?


## Author
Hrushikesh.Dhumal