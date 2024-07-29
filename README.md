# Text to Audio Script

A python script that converts PDFs to audio.

## A Note on Scope of this Project
In itself, converting PDFs to text appropriately is a challenging proposition. 
Here, I focus on the mechanics of extracting text from PDFs without diving into 
appropriately cleaning the resulting text, with the exception of (a very naive)
method of removing page numbers from the start of the text. In the future, it 
would be interesting to explore the approach outlined by
[Lin (2003)](https://www.researchgate.net/publication/221253782_Header_and_Footer_Extraction_by_Page-Association)
, which was implemented in python [here](https://medium.com/@hussainshahbazkhawaja/paper-implementation-header-and-footer-extraction-by-page-association-3a499b2552ae).
Or, alternatively, use DBSCAN to cluster the text to identify headers/footers outlined in [this comment](https://github.com/pymupdf/PyMuPDF/discussions/2259#discussioncomment-6669190).



