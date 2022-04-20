from mysite.wsgi import *
from django.template.loader import get_template
from weasyprint import HTML


def printTicket():
    template = get_template("ingresos.html")
    context = {"name": "William Jair Dávila Vargas"}
    html_template = template.render(context)
    #css_url = os.path.join(settings.BASE_DIR, 'static/lib/bootstrap-4.4.1-dist/css/bootstrap.min.css')
    HTML(string=html_template).write_pdf(target="prueba.pdf", )


printTicket()


instalar la otra libreria que se veia más breve