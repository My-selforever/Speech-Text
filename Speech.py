import PyPDF2 as pdf
import pyttsx3 as ptsx
import os

os.system('cls')

b = open("NCERT-Class-8-Geography-Syllabus.pdf","rb")

pdfReader = pdf.PdfFileReader(b)
tts = ptsx.init()


tts.setProperty('rate',145)
for i in range(0,pdfReader.numPages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    tts.say(text)
    tts.runAndWait()