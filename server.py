# Import packages
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    text_to_french = translator.englishToFrench(textToTranslate)
    return f"<p style='color:red;'>Your translation to French -->>  {text_to_french} </p>"


@app.route("/frenchToEnglish")
def frenchToEnglish():
   textToTranslate = request.args.get('textToTranslate')
   text_to_english = translator.frenchToEnglish(textToTranslate)
   return f"<p style='color:red;'>Votre traduction en anglais -->>  {text_to_english} </p>"


@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50000)
