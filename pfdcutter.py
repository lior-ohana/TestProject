from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split, pageNumber, cm_from_top, cm_from_bottom, cm_from_right, cm_from_left):
    pdf = PdfFileReader(path)
    point = 28.346456693
    pdf_writer = PdfFileWriter()
    # for pageN in range(pdf.getNumPages()):

    page = pdf.getPage(pageNumber)

    lr = page.cropBox.getLowerRight()
    uf = page.cropBox.getUpperLeft()
    ur = page.cropBox.getUpperRight()

    page.cropBox.setLowerLeft((cm_from_left*point, cm_from_bottom*point))
    page.cropBox.setUpperRight((ur[0] - cm_from_top*point, ur[1] - cm_from_right*point))
    page.cropBox.setLowerRight((lr[0] - cm_from_right*point, cm_from_bottom*point))
    page.cropBox.setUpperLeft((cm_from_left*point, uf[1] - cm_from_top*point))

    pdf_writer.addPage(pdf.getPage(pageNumber))
    output = f'{name_of_split}{pageNumber}.jpg'
    output_pdf = open(output, 'wb')
    pdf_writer.write(output_pdf)
    output_pdf.close()
