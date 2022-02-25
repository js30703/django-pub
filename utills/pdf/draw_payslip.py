import os
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import TableStyle, SimpleDocTemplate, Table, Paragraph
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4, A5
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from django.conf import settings


def draw_payslip(filename, pay_title, pay_detail, total):
    pdfmetrics.registerFont(
        TTFont('content', f'{settings.BASE_DIR}/utills/pdf/Muli-Light.ttf')
    )

    pdfmetrics.registerFont(
        TTFont(
            'header', f'{settings.BASE_DIR}/utills/pdf/PlayfairDisplay-SemiBold.ttf')
    )

    class PageNumCanvas(canvas.Canvas):

        def __init__(self, *args, **kwargs):
            """Constructor"""
            canvas.Canvas.__init__(self, *args, **kwargs)
            self.pages = []

        # ----------------------------------------------------------------------
        def showPage(self):
            """
            On a page break, add information to the list
            """
            self.pages.append(dict(self.__dict__))
            self._startPage()

        # ----------------------------------------------------------------------
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

        # ----------------------------------------------------------------------
        def draw_page(self, page_count):
            # header
            image = 'logo.jpg'
            self.drawImage(
                f'{settings.BASE_DIR}/utills/pdf/{image}', 420, 765, width=140, height=70)
            self.setFont('header', 8)
            self.drawCentredString(
                110, 765+40, 'Wonderfull Life With Beautiful Smile')
            self.line(30, 765+30, 400, 765+30)

            # footer
            self.line(30, 60, 560, 60)
            self.setFont('content', 8)
            self.drawString(
                95, 49, 'Website: www.indentalclinic.net | SIP: 503.445/36-KUG/436.6.3/IX/2016 | Email: info@indentalclinic.co.id')
            self.drawString(
                180, 38, 'Adress: Jalan Baratajaya 19 no 54A | Phone: 031-50115751')
            page = "%s of %s" % (self._pageNumber, page_count)
            self.drawString(290, 20, page)

    reportoutputfilepath = os.path.join(f"{settings.BASE_DIR}/{filename}.pdf")

    pdf_file = SimpleDocTemplate(
        reportoutputfilepath,
        pagesize=A4,
        topMargin=70
    )

    elements = []
    para_styles = getSampleStyleSheet()

    para_styles.add(ParagraphStyle(
        name='title1',
        parent=para_styles['Heading1'],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20,
    ))
    elements.append(Paragraph('P A Y S L I P', para_styles['title1']))

    treat_table = Table(pay_title, colWidths=(
        25*mm, 60*mm, 25*mm, 60*mm,), repeatRows=1, spaceAfter=10*mm)
    ts_treatment = [
        ('ALIGN', (4, 0), (-1, -1), 'LEFT'),
        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
        ('FONT', (0, 0), (-1, 0), 'header'),
        ('LINEABOVE', (0, -1), (-1, -1), 1, colors.black),
        ('FONT', (0, -1), (-1, -1), 'content'),
        ('BACKGROUND', (1, 1), (-2, -2), colors.white),
        ('TEXTCOLOR', (0, 0), (1, -1), colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]
    treat_table.setStyle(TableStyle(ts_treatment))
    elements.append(Paragraph('INFO', para_styles['Heading4']))
    elements.append(treat_table)

    detail = Table(pay_detail, colWidths=(
        15*mm, 20*mm, 80*mm, 10*mm, 20*mm, 30*mm), repeatRows=1)
    ts_detail = [
        ('ALIGN', (4, 0), (-1, -1), 'LEFT'),
        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.black),
        ('FONT', (0, 0), (-1, 0), 'header'),
        ('LINEABOVE', (0, -1), (-1, -1), 1, colors.black),
        ('FONT', (0, -1), (-1, -1), 'header'),
        ('BACKGROUND', (1, 1), (-2, -2), colors.white),
        ('TEXTCOLOR', (0, 0), (1, -1), colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]

    detail.setStyle(TableStyle(ts_detail))
    elements.append(Paragraph('PAYSLIP DETAIL', para_styles['Heading4']))
    elements.append(detail)

    para_styles.add(ParagraphStyle(
        name='total',
        alignment=TA_RIGHT,
        fontName='content',
        fontSize=10,
        leading=8,
        spaceAfter=10,
    ))
    elements.append(
        Paragraph(f'Total Price : {total[0]} IRD ', para_styles['total']))
    elements.append(
        Paragraph(f'Total Comission : {total[1]} IRD', para_styles['total']))

    # Build the PDF
    pdf_file.build(elements, canvasmaker=PageNumCanvas)

    return reportoutputfilepath


def dummy_data():

    filename = 'payslip_test.pdf'

    uuid = 'asdfa-asdfa'

    pay_title = [
        ['ID', 'NAME', 'type', 'DATE'],
        [uuid, 'docter1 ghahahahah lonong', 'Doctor', '2021-05-01 ~ 2021-05-31']

    ]

    pay_detail = [
        ['DATE', 'TM ID', 'PRODUCT', 'EA',
            'PRICE', 'COMISSION'],  # product List
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        ['06/01', 'asdfa', 'TestSercive_of_1_inden invoice',
            '1', '1,000,000', '500,000'], [
            '',
            '',
            'jujun',
            '',
            '',
            '',
        ],
        [],
    ]

    total_pr = '1, 260, 000'
    total_com = '1, 260, 000'

    total = [total_pr, total_com]
    draw_payslip(filename, pay_title, pay_detail, total)


if __name__ == 'main':
    from utills.pdf.draw_payslip import dummy_data
    dummy_data()
