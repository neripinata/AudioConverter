#Source code: https://www.geeksforgeeks.org/convert-text-speech-python/

from gtts import gTTS
  
# This module is imported so that we can  
# play the converted audio 
import os 

def Convert():
    f = open("info.txt", "r")
    
    # The text that you want to convert to audio 
    mytext = f.read()
    
    # Language in which you want to convert 
    language = 'en'
    
    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("converter_audio.mp3") 

    
    # Playing the converted file 
    os.system("converter_audio.mp3") 
