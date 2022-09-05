# Import packages
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv #, find_dotenv

# find_dotenv
load_dotenv()

Api_Key = os.environ['apikey']
URL = os.environ['url']

# Connect to ibm watson translator 
def connectToWatson():
     authenticator = IAMAuthenticator(Api_Key)
     language_translator = LanguageTranslatorV3(
            version='2022-09-01',
            authenticator=authenticator
            )
     language_translator.set_service_url(URL)   # zone, region 

     return language_translator


# Translate English to French
def englishToFrench(englishText):
      translation = connectToWatson() \
             .translate(
             text = englishText,
             model_id= 'en-fr') \
             .get_result()
     
      frenchText = dict(translation)                                      # json.dumps(translation, indent= 2, ensure_ascii= False)
      
      for k, v in frenchText.items() : 
        if "translations" in k:
            return v


# Translate French to English
def frenchToEnglish(frenchText):
    translation = connectToWatson() \
          .translate(
          text = frenchText,
          model_id = 'fr-en') \
          .get_result()
    
    englishText =  dict(translation)                                                       # json.dumps(translation, indent= 2, ensure_ascii= False)
    for k, v in englishText.items() : 
        if "translations" in k:
            return v


