from fastapi import FastAPI, HTTPException

import fasttext
from fasttext import tokenize
import re
import os

app = FastAPI()

# I am using lid.176.bin, which is faster and slightly more accurate,
# there is a compressed version avaiable at https://fasttext.cc/docs/en/language-identification.html
fasttext_language_model = fasttext.load_model(os.path.join("model", "lid.176.bin"))

white_space_pattern = re.compile(r"\s")


def preprocess_text_for_language_detection(text: str):
    """
    Cleans the text as per fasttext requirements.
    The requirements can be found here: https://pypi.org/project/fasttext/
    
    :text: str: text to clean
    :returns: str: cleaned text
    """
    # fastText assumes UTF-8 encoded text
    text = str(text)
    
    # fastText is not aware of UTF-8 whitespace
    # Replace all white space with space
    text = white_space_pattern.sub(text, " ")
    
    # Tokenize text, per fastext function and rejoin
    tokens = tokenize(text)
    text = " ".join(tokens)
    n = len(tokens)
    
    # Remove white space char as it affects the model accuracy
    text = text.replace("</s>", "")
    
    return text.lower()


@app.get("/language_detect/")
def identify_languages(text: str, no_of_languages: int =1, threshold: float=0.0):

    if len(text) == 0:
        raise HTTPException(status_code=406, detail="Text field is empty")
    clean_text = preprocess_text_for_language_detection(text)
    if len(clean_text) == 0:
        raise HTTPException(status_code=406, detail="Cleaned text is empty")
    ft_output = fasttext_language_model.predict(clean_text, no_of_languages, threshold=threshold)
    # format output
    result = [(ft_output[0][i][-2:], ft_output[1][i]) for i in range(len(ft_output[0]))]
    return result