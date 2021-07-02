# -*- coding: utf-8 -*-
# pylint: disable=W1309
"""
.. note::

    https://www.reportlab.com/docs/reportlab-userguide.pdf

.. note::

    Czcionka Verdana to czcionka własnościowa (Microsoft). Odpowiednikiem dla LINUX
    jest DejaVuSans. Jesli Chcesz się upewnić, czy czcionka DejaVuSans jets dostępna
    to komenda: fc-list | grep "DejaVu Sans"

"""
import subprocess
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus import Paragraph as PH
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError
from reportlab.lib import colors
from .converters import numtoword
from .pdf_tools import MCLine

try:
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))
    CHOSENFONT = "Verdana"
except TTFError:
    # for LINUX compatibility, tested on Debian 10, 5.4.72-microsoft-standard-WSL2
    pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
    CHOSENFONT = 'DejaVuSans'

def create_invoice_pdf(invoice_name: str, bill):
    """Funkcja tworzy fakturę"""

    style_right = PS(name="", fontName=CHOSENFONT, fontSize=8, alignment=TA_RIGHT)
    style_left = PS(name="", fontName=CHOSENFONT, fontSize=8, alignment=TA_LEFT)
    style_justify = PS(name="", fontName=CHOSENFONT, fontSize=8, alignment=TA_JUSTIFY)
    style_center = PS(name="", fontName=CHOSENFONT, fontSize=8, alignment=TA_CENTER)
    style5 = PS(name="", fontName=CHOSENFONT, fontSize=6, alignment=TA_LEFT)
    style6 = PS(name="", fontName=CHOSENFONT, fontSize=6, alignment=TA_RIGHT)

    invoice = list()
    invoice.append(
        PH(f"<font size=8>{bill.user.city}, data wystawienia: {bill.created.strftime('%Y-%m-%d')}</font>", style_right)
    )
    invoice.append(Spacer(1, 8))
    table = Table(
        [[PH("Sprzedawca:", style_left), PH(f"Data sprzedaży: {bill.created.strftime('%B %Y').lower()}", style_right)]],
        colWidths=[8.4 * cm, 8.4 * cm],
    )
    invoice.append(table)
    invoice.append(MCLine(465))
    invoice.append(
        PH(
            f"<font size=14>{bill.user.first_name} {bill.user.last_name} \
{bill.user.company_name}</font>",
            style_left,
        )
    )
    invoice.append(Spacer(1, 16))
    invoice.append(
        PH(
            f"Adres: {bill.user.street} {bill.user.zip_code} {bill.user.city}",
            style_left,
        )
    )
    invoice.append(PH(f"NIP: {bill.user.nip}", style_left))
    invoice.append(
        PH(f"Nr konta: {bill.user.account_number}", style_left)
    )
    invoice.append(Spacer(1, 16))
    invoice.append(PH("Nabywca:", style_left))
    invoice.append(Spacer(1, 2))
    invoice.append(MCLine(465))
    invoice.append(
        PH(f"<font size=14>{bill.contractor.company_name}</font>", style_left)
    )
    invoice.append(Spacer(1, 16))
    invoice.append(
        PH(
            f"Adres: {bill.contractor.street}, {bill.contractor.zip_code} \
{bill.contractor.city}",
            style_left,
        )
    )
    invoice.append(PH(f"NIP: {bill.contractor.nip}", style_left))
    invoice.append(Spacer(1, 25))
    table = Table(
        [[PH(f"{bill.name}", style_center)]],
        colWidths=[16.36 * cm],
        rowHeights=[0.8 * cm],
    )
    table.setStyle(
        TableStyle(
            [
                (
                    "BOX",
                    (
                        0,
                        0,
                    ),
                    (-1, -1),
                    0.25,
                    colors.black,
                ),
                ("FONT", (0, 0), (-1, -1), CHOSENFONT),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("BACKGROUND", (0, 0), (-1, -1), "#f2f2f2"),
            ]
        )
    )
    invoice.append(table)
    invoice.append(Spacer(1, 25))
    data = [
        [
            PH(r"<b>L.p.</b>", style_justify),
            PH(r"<b>Nazwa towaru/usługi</b>", style_justify),
            PH(r"<b>ilość</b>", style_justify),
            PH(r"<b>j.m</b>", style_justify),
            PH(r"<b>Cena jednostkowa [zł,gr]</b>", style_justify),
            PH(r"<b>Wartość [zł,gr]</b>", style_justify),
        ]
    ]
    for i in bill.services:
        data += (
            [
                PH("1", style_justify),
                PH(
                    f"{i.service.name}",
                    style_justify,
                ),
                PH(f"{i.volume}", style_justify),
                PH(f"{i.measure}", style_justify),
                PH(f"{round(i.partial_amount, 2)}" + " zł", style_justify),
                PH(f"{round(i.full_amount, 2)}" + " zł", style_justify),
            ],
        )

    data += [
        [
            "",
            "",
            "",
            "",
            PH("Razem:", style_justify),
            PH(f"{round(bill.amount, 2)}" + " zł", style_justify),
        ],
    ]
    table = Table(
        data, colWidths=[1.05 * cm, 7.30 * cm, 1.5 * cm, 1.5 * cm, 2.5 * cm, 2.5 * cm]
    )
    table.setStyle(
        TableStyle(
            [
                ("INNERGRID", (0, 0), (-1, -2), 0.25, colors.black),
                ("BOX", (0, 0), (-1, -2), 0.25, colors.black),
                ("INNERGRID", (-1, -2), (-1, -1), 0.25, colors.black),
                ("BOX", (-1, -2), (-1, -1), 0.25, colors.black),
                ("FONT", (0, 0), (-1, -1), CHOSENFONT),
            ]
        )
    )
    invoice.append(table)
    invoice.append(Spacer(1, 25))
    PH(f"słownie: {{ }}", style_center)
    table = Table(
        [
            [
                f"Należność ogółem: {round(bill.amount, 2)} zł",
                f"{numtoword(round(bill.amount, 2))}",
            ]
        ],
        colWidths=[6 * cm, 10.35 * cm],
        rowHeights=[1 * cm],
    )
    table.setStyle(
        TableStyle(
            [
                (
                    "BOX",
                    (
                        0,
                        0,
                    ),
                    (-1, -1),
                    0.25,
                    colors.black,
                ),
                ("FONT", (0, 0), (-1, -1), CHOSENFONT),
                ("FONTSIZE", (0, 0), (-1, -1), 8),
                ("BACKGROUND", (0, 0), (-1, -1), "#f2f2f2"),
            ]
        )
    )
    invoice.append(table)
    invoice.append(Spacer(1, 10))
    invoice.append(PH("Płatność: przelew", style_left))
    invoice.append(PH(f"Termin zapłaty do: {bill.payment_date}", style_left))
    invoice.append(Spacer(1, 32))
    data = [
        [
            PH("_" * 45, style5),
            PH("_" * 49, style6),
        ],
        [
            PH("podpis osoby upoważnionej do odbioru Rachunku", style5),
            PH("podpis osoby upoważnionej do wystawienia Rachunku", style6),
        ],
    ]
    invoice.append(Table(data, colWidths=[8.4 * cm, 8.4 * cm]))

    doc = SimpleDocTemplate(
        f"{invoice_name}.pdf",
        pagesize=A4,
        rightMargin=60,
        leftMargin=60,
        topMargin=42,
        bottomMargin=18,
    )
    doc.build(invoice)
    subprocess.Popen([f"{invoice_name}.pdf"], shell=True)
