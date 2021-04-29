from django.shortcuts import render
from django.http import FileResponse
from .models import Certificate
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
# Create your views here.


def certificate_generator(request, id):

    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 100, "Hello world")
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF= os.

    existing_pdf = PdfFileReader(open("./certificates/certificate_template.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("./certificates/generated_certificates/destination.pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    Buffer = open("./certificates/generated_certificates/destination.pdf", "rb")
    return FileResponse(Buffer, as_attachment=False, filename='./certificates/generated_certificates/destination.pdf')


def certificate_data(certificate_id):
    certificate = Certificate.objects.get(id=certificate_id)
    user_name = certificate.user_id.first_name + \
        " " + certificate.user_id.last_name
    issuer_name = certificate.course_id.course_creator.first_name + \
        " " + certificate.course_id.course_creator.last_name
    issue_date = certificate.issue_date
    course_name = certificate.course_id.name
    return user_name, course_name, issue_date, issuer_name
