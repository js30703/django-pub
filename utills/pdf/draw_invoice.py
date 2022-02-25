from reportlab.pdfgen import canvas 
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.platypus import TableStyle,SimpleDocTemplate,Table, Paragraph
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4, A5
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime
import os
from reportlab.lib.units import mm

from django.conf import settings
from django.core.files.base import ContentFile


 
def draw_invoice(filename,treatment,service_detail,total,payment_detail, paid_total, left_cost ):

    pdfmetrics.registerFont(
    TTFont('content', f'{settings.BASE_DIR}/utills/pdf/Muli-Light.ttf')
    )

    pdfmetrics.registerFont(
        TTFont('header', f'{settings.BASE_DIR}/utills/pdf/PlayfairDisplay-SemiBold.ttf')
    )

    class PageNumCanvas(canvas.Canvas):
    
        def __init__(self, *args, **kwargs):
            """Constructor"""
            canvas.Canvas.__init__(self, *args, **kwargs)
            self.pages = []
            
        #----------------------------------------------------------------------
        def showPage(self):
            """
            On a page break, add information to the list
            """
            self.pages.append(dict(self.__dict__))
            self._startPage()
            
        #----------------------------------------------------------------------
        def save(self):
            """
            Add the page number to each page (page x of y)
            """
            page_count = len(self.pages)
            
            for page in self.pages:
                self.__dict__.update(page)
                self.draw_page(page_count)
                canvas.Canvas.showPage(self)
                
            canvas.Canvas.save(self)
            
        #----------------------------------------------------------------------
        def draw_page(self, page_count):    
            
            image = 'logo.jpg'


            self.drawImage(f'{settings.BASE_DIR}/utills/pdf/{image}', 420, hight-75, width= 140, height=70)

            self.setFont('header', 11)
            self.drawCentredString(140, hight-38, 'Wonderfull Life With Beautiful Smile')

            self.line(30, hight-50 , 400, hight-50)



                # ###   footer
            self.line(30, 60, 560, 60)
            self.setFont('content', 8)

            self.drawString(95, 49, 'Website: www.indentalclinic.net | SIP: 503.445/36-KUG/436.6.3/IX/2016 | Email: info@indentalclinic.co.id')
            self.drawString(180, 38, 'Adress: Jalan Baratajaya 19 no 54A | Phone: 031-50115751')
            page = "%s of %s" % (self._pageNumber, page_count)
            self.drawString(290, 20, page)


    # reportoutputfilepath = os.path.join(f"{settings.BASE_DIR}/../media/invoice/{datetime.now().strftime('%Y-%m')}/{filename}.pdf")
    # reportoutputfilepath = os.path.join(f'/mnt/c/Users/js010/Desktop/utills/pdfgen/{filename}.pdf')
    
    reportoutputfilepath = os.path.join(f"{settings.BASE_DIR}/{filename}.pdf")
    width , hight = A4
    


    pdf_file = SimpleDocTemplate(
                                reportoutputfilepath,
                                pagesize=(width, hight),
                                topMargin=60
                        )
    

    elements = []
    para_styles = getSampleStyleSheet()

    para_styles.add(ParagraphStyle(
        name='title1',
        parent=para_styles['Heading1'],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20,
        spaceBefore=80,
    ))


    elements.append(Paragraph('I N V O I C E', para_styles['title1']))


    treat_table = Table(treatment, colWidths=(25*mm, 60*mm, 60*mm, 25*mm,),repeatRows=1, spaceAfter=10*mm, spaceBefore=10)
    ts_treatment = [
            ('ALIGN', (4,0), (-1,-1), 'LEFT'),
            ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
            ('FONT', (0,0), (-1,0), 'header'),
            ('LINEABOVE', (0,-1), (-1,-1), 1, colors.black),
            ('FONT', (0,-1), (-1,-1), 'content'),
            ('BACKGROUND',(1,1),(-2,-2),colors.white),
            ('TEXTCOLOR',(0,0),(1,-1),colors.black),
            ('FONTSIZE', (0,0),(-1,-1), 9), 
            ]
    treat_table.setStyle(TableStyle(ts_treatment))


    elements.append(Paragraph(f'TREATMENT INFO', para_styles['Heading4']))
    elements.append(treat_table)


# 서비스 디테일 표
    detail = Table(service_detail, colWidths=(20*mm, 100*mm, 20*mm, 30*mm),repeatRows=1)
    ts_detail = [
            ('ALIGN', (4,0), (-1,-1), 'LEFT'),
            ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
            ('FONT', (0,0), (-1,0), 'header'),
            ('LINEABOVE', (0,-1), (-1,-1), 1, colors.black),
            ('FONT', (0,-1), (-1,-1), 'header'),
            ('BACKGROUND',(1,1),(-2,-2),colors.white),
            ('TEXTCOLOR',(0,0),(1,-1),colors.black),
            ('FONTSIZE', (0,0),(-1,-1), 9), 
            ]

    detail.setStyle(TableStyle(ts_detail))
    elements.append(Paragraph('SERVICE DETAIL', para_styles['Heading4']))
    elements.append(detail)

# 토탈 가격
    para_styles.add(ParagraphStyle(
        name='total',
        parant=para_styles['Normal'],
        alignment=TA_RIGHT,
        fontName='content',
        fontSize=10,
        leading=8,
        spaceAfter= 10,
    ))
    elements.append(Paragraph(f'Total Service Cost : {total} IRD', para_styles['total']))

#결제 정보 
    payment_detail = Table(payment_detail, colWidths=(50*mm, 50*mm, 40*mm,30*mm),repeatRows=1)
    ts_payment = [
            ('ALIGN', (4,0), (-1,-1), 'LEFT'),
            ('LINEBELOW', (0,0), (-1,0), 1, colors.black),
            ('FONT', (0,0), (-1,0), 'header'),
            ('LINEABOVE', (0,-1), (-1,-1), 1, colors.black),
            ('FONT', (0,-1), (-1,-1), 'header'),
            ('BACKGROUND',(1,1),(-2,-2),colors.white),
            ('TEXTCOLOR',(0,0),(1,-1),colors.black),
            ('FONTSIZE', (0,0),(-1,-1), 9), 
            ]

    payment_detail.setStyle(TableStyle(ts_payment))
    elements.append(Paragraph('PAYMENT DETAIL', para_styles['Heading4']))
    elements.append(payment_detail)
    
    
    elements.append(Paragraph(f' Paid Total : {paid_total} IRD', para_styles['total']))
    elements.append(Paragraph(f' Left Cost : {left_cost} IRD', para_styles['total']))
    elements.append(Paragraph(f" Issued Date : {datetime.now().date().strftime('%d-%m-%Y')} ", para_styles['total']))

    # Build the PDF
    pdf_file.build(elements, canvasmaker=PageNumCanvas)
    return reportoutputfilepath