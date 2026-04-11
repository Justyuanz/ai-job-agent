#pip is package installer for python pip install  pip install PyMuPDF
import fitz

def extract_texts_from_pdf(filename:str):
	doc = fitz.open(filename) #handle open fail
	text= ''
	for page in doc: #generator in python
		text += page.get_text()
	return text.lower()

"""
int i = 0;
while (i < page_count)
{
    Page page = get_page(doc, i);
    text = text + get_text(page);
    i++;
}
Think of it like this:

library = a toolbox / whole package
module = one box inside the toolbox
object = one actual thing you created from code
method = an action that object can do

fitz comes from the PyMuPDF library. It is used to work with PDFs.
fitz.open() opens a PDF as a document object with pages and text tools. C open/fopen opens raw file data.
doc is just a variable name holding the opened PDF document.
You do not pre-init doc because you assign it immediately. You must init text because text += ... needs an existing value first.
page is one page object from the PDF. It has methods because it is an object, not just a number.
for page in doc means Python automatically gives you pages one by one from the document. PyMuPDF documents are iterable page by page.
text is a string collecting all extracted text. get_text() extracts text from one page.
"""