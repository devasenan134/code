import pyqrcode
import png

link = "https://forms.office.com/Pages/ResponsePage.aspx?id=loKLa_-92EqTrYS8vzhC9XtpBE2iiSNEmiYzTt5T1sdUOE03Tk84REsxSVpQSDVGNElYOUpLQkZTUi4u"

qr = pyqrcode.create(link)
qr.svg("qrcode.svg", scale=8)
