from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

import csv

class Command():
    identity        : str             = ""
    appart          : str             = ""
    address         : str             = ""
    postalcode      : str             = ""
    city            : str             = ""
    country         : str             = ""

    def __init__(self, identity, appart, address, postalcode, city, country):
        self.identity = identity
        self.appart = appart
        self.address = address
        self.postalcode = postalcode
        self.city = city
        self.country = country

    def generateHTML(self):
        return f'''
            <p>{self.identity}</p>
            <p>{self.appart}</p>
            <p>{self.address}</p>
            <p>{self.postalcode} - {self.city}</p>
            <p>{self.country}</p>
            <p style="page-break-before: always" ></p>
        '''


class KickstarterPDF():
    font_config = FontConfiguration()
    css = CSS(string='''
        @page { size: A4 landscape; margin: 1cm }
        @font-face {
            font-family: Lucida Console;
            src: url(assets/lucida-console.ttf);
        }
        h1 { font-family: Lucida Console }''', font_config=font_config)

    def render(self, body):
        HTML(string=body).write_pdf('addresses.pdf', stylesheets=[self.css], font_config=self.font_config)

body = ''
with open('assets/csv-sample.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        command = Command(identity=row[1],appart=row[1],address=row[3],postalcode=row[4],city=row[5],country=row[6])
        body = body + command.generateHTML()

# generate pdf
KickstarterPDF().render(body)
