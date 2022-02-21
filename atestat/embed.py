import glob
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Mm

doc = DocxTemplate("template.docx")

textFiles = glob.glob("*.html") + glob.glob("css/*.css") + glob.glob("js/*.js")
imageFiles = glob.glob("*res/*.png") + glob.glob("*res/*.jpg")

filesContents = []
for file in textFiles:
    contents = open(file, "r", encoding='utf8')
    filesContents.append( [file, contents.read()] )

imageContents = []
for file in imageFiles:
    contents = InlineImage(doc, image_descriptor= file, width=Mm(140) )
    imageContents.append( [file, contents] )

context = {
    'textFiles':filesContents,
    'imageFiles':imageContents
}


doc.render(context)
doc.save("atestat.docx")

# print(filesContents)