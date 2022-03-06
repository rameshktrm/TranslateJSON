from googletrans import Translator, constants
from pprint import pprint
import GoogleTrans as gt
import re,os
if __name__ == '__main__':
    gt.readSourceFolder()

def readSourceFolder():
    path = "i18_en"
    files = os.listdir(path)
    for file in files:
        print('SourceFileName : ', file)
        convertString(file)

def convertString(sourceFileName):
    lines = open("i18_en/"+sourceFileName)
    for line in lines:
        print(line)
        validStringList = re.findall(': (.*)', line)
        if (len(validStringList) > 0):
            translatedString = translateString(validStringList.__getitem__(0))
            writeFile(line.replace(validStringList.__getitem__(0), translatedString),sourceFileName)
        else:
            writeFile(line,sourceFileName)

def writeFile(line, sourceFileName):
    #print("WriteFile Started...")
    destFileName = "i18_es/" + sourceFileName.replace('-en', '-es')
    file = open(destFileName, "a")
    file.write(line)
    #file.write("\n")

def translateString(translation_input):
    if translation_input.__contains__("Next"):
        return '"Próxima",'
    elif translation_input.__contains__("Mandatory"):
        return '"Obligatorio",'
    elif translation_input.__contains__("Terminator"):
        return '"Terminator",'
    elif translation_input.__contains__("None"):
        return '"Ninguna",'
    elif translation_input.__contains__("second"):
        return '"segunda",'
    else:
        translator = Translator()
        print("Translation Input == ", translation_input)
        translation = translator.translate(translation_input, dest="es")
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        return translation.text
