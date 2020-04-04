import PyPDF2

with open('dummy.pdf', 'rb') as file:  # add b to read binary
    print(file)

    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)    # number of pages
    print(reader.getPage(0))  # page object
    # print(reader.rotate(180)) - have to get page to rotate
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open('crooked.pdf', 'wb') as new_file:
        writer.write(new_file)
