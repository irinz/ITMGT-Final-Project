# Code from https://pdfminersix.readthedocs.io/en/latest/tutorial/composable.html (pdf miner documentation)
# pandiwa.pdf file courtesy of Pia Noche, https://samutsamot.com/wp-content/uploads/2014/11/mga-pandiwa-sa-ibat-ibang-panahunan1-1.pdf, https://samutsamot.com/2014/11/25/list-of-filipino-verbs-pandiwa/
# Writes a text file containing all the words in the pandiwa file. (Will add verb tenses to the spell checker)

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open('pandiwa.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
pandiwa_text_unprocessed = open("pandiwa_text_unprocessed.txt", "w")
text = (output_string.getvalue())
pandiwa_text_unprocessed.write(text)
pandiwa_text_unprocessed.close()
