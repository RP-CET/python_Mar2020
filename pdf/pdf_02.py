import fpdf

#create a new pdf
document = fpdf.FPDF()

#define font and color for title and add the first page
document.set_font("Times","B", 14)
document.set_text_color(19,83,173)
document.add_page()

#add a image
document.image("rp_logo.png", x=10, y=8, w=23)
document.set_y(30); 

#write the title of the document
document.cell(0,5,"PDF Test Document")
document.ln()

#write a long paragraph
document.set_font("Times", "", 11)
document.set_text_color(0)
document.multi_cell(0,5, "This is an example of a long paragraph. " * 10)
document.ln()

#write another long paragrahp
document.multi_cell(0,5, "Another long paragraph. \
Lorem ipsum dolor sit amet, consectetur adipiscing elit." * 40)

#add another image
document.image("rp_logo.png", w=23)

#save the document
document.output("pdf_report.pdf")