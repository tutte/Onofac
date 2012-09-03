#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa con la ilusión de poder descargarme automaticamente las facturas de ono.

import mechanize, urllib2
from urllib import urlopen, urlencode 

# Variables
user = 'email'
password = 'password en texto plano'
output_file = 'factura_ono.pdf'

web = "https://www.ono.es/clientes/registro/login/"
pagina_facturas = "https://www.ono.es/clientes/facturacion/facturas-emitidas/"
login_web = "https://www.ono.es/clientes/registro/login/entrar/"
fichero = "https://www.ono.es/delegate/factYpagos-portlets/FYPDelegateServlet/?action=factDetail&numServicio=0&numFactura=0&tipo=Factura&formato=2"

br = mechanize.Browser()
br.open(web)

data = {
	'user_username': user,
	'user_password': password,
	'idClientehidden': '',
	'answer': ''
}

response1 = urllib2.Request(login_web, urlencode(data))

br.open(response1)
br.open(pagina_facturas)
html_facturas = br.response().read()

br.open(fichero)
pdf_factura = open(output_file, 'w')
pdf_factura.write(br.response().read())
pdf_factura.close()
