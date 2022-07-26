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
import os
from contextlib import ContextDecorator
from decimal import Decimal
import platform
import subprocess
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Paragraph as PH
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError
from reportlab.lib import colors

from .converters import numtoword
from .other import perc_amounts_collector, all_percs_dict
from .pdf_tools import MCLine

try:
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))
    CHOSENFONT = "Verdana"
except TTFError:
    # for LINUX compatibility, tested on Debian 10, 5.4.72-microsoft-standard-WSL2
    pdfmetrics.registerFont(TTFont("DejaVuSans", "DejaVuSans.ttf"))
    CHOSENFONT = "DejaVuSans"


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
        PH(
            f"<font size=8>{bill.user.city}, data wystawienia: {bill.created.strftime('%Y-%m-%d')}</font>",
            style_right,
        )
    )
    invoice.append(Spacer(1, 8))
    table = Table(
        [
            [
                PH("Sprzedawca:", style_left),
                PH(
                    f"Data sprzedaży: {bill.created.strftime('%B %Y').lower()}",
                    style_right,
                ),
            ]
        ],
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
    invoice.append(PH(f"Nr konta: {bill.user.account_number}", style_left))
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
                PH(f"{numtoword(round(bill.amount, 2))}", style_center),
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
    if platform.system() == 'Darwin':
        invoice_name = os.path.join(os.getcwd(), f"{invoice_name}.pdf")
        subprocess.call(['open', invoice_name])
    else:
        subprocess.Popen([f"{invoice_name}.pdf"], shell=True)


class RevenueEvidencePDF(ContextDecorator):

    STYLE_JUSTIFY = PS(name="", fontName=CHOSENFONT, fontSize=8, alignment=TA_JUSTIFY)
    STYLE_JUSTIFY_SM = PS(
        name="", fontName=CHOSENFONT, fontSize=7, alignment=TA_JUSTIFY
    )
    STYLE_HEADER = PS(name="", fontName=CHOSENFONT, fontSize=10, alignment=TA_CENTER)
    COLS_7 = [1.05 * cm, 2 * cm, 1.05 * cm, 2 * cm, 16 * cm, 2 * cm, 4 * cm]
    COLS_12 = [
        6.10 * cm,
        1.77 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.77 * cm,
        2 * cm,
        4 * cm,
    ]
    COLS_15 = [
        1.05 * cm,
        2 * cm,
        1.05 * cm,
        2 * cm,
        1.77 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.78 * cm,
        1.77 * cm,
        2 * cm,
        4 * cm,
    ]
    TABLE_STYLE = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
            ("FONT", (0, 0), (-1, -1), CHOSENFONT),
        ]
    )
    TABLE_STYLE2 = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.black),
            ("FONT", (0, 0), (-1, -1), CHOSENFONT),
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ]
    )

    def __init__(self, bills):
        self.bills = bills
        self.evidence = []

    def __enter__(self):

        self.evidence.append(PH("EWIDENCJA PRZYCHODÓW", self.STYLE_HEADER))
        self.evidence.append(Spacer(1, 25))
        self.table_header()
        self.table_subheader()

        dicts_lst = []
        dicts_lst_all = []
        total_amount = Decimal(0)
        for num, bill in enumerate(self.bills, 1):
            perc_dict = perc_amounts_collector(bill)
            dicts_lst.append(perc_dict)
            dicts_lst_all.append(perc_dict)
            created = bill.created.strftime("%Y-%m-%d")
            total_amount += bill.amount

            invoice = [
                PH(rf"#{num}", self.STYLE_JUSTIFY_SM),
                PH(rf"{created}", self.STYLE_JUSTIFY_SM),
                PH(r"", self.STYLE_JUSTIFY_SM),
                PH(rf"{bill.name}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('17%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('15%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('14%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('10%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('8,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('5,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('3%', '')}", self.STYLE_JUSTIFY_SM),
                PH(r"", self.STYLE_JUSTIFY_SM),
                PH(r"", self.STYLE_JUSTIFY_SM),
            ]

            table = Table([invoice], colWidths=self.COLS_15)
            table.setStyle(self.TABLE_STYLE2)
            self.evidence.append(table)

            if num == 7:
                page_dict = all_percs_dict(dicts_lst)
                dicts_lst = []
                self.page_summary(page_dict)
                self.evidence.append(PageBreak())
            if num % 9 == 0 and num > 9:

                self.previous_page(page_dict)

                page_dict = all_percs_dict(dicts_lst)
                dicts_lst = []
                self.page_summary(page_dict)

                self.evidence.append(PageBreak())
        if num < 9:
            perc_dict = all_percs_dict(dicts_lst)
        #        x = all_percs_dict(dicts_lst)
        #        self.page_summary(x)
        #        self.previous_page(dicts_lst_all)
        try:
            self.previous_page(page_dict)
        except UnboundLocalError:
            pass
        page_dict = all_percs_dict(dicts_lst)
        dicts_lst = []
        self.page_summary(page_dict)

        self.table_sum_all(dicts_lst_all, total_amount)

    def __exit__(self, *exc):

        doc = SimpleDocTemplate(
            f"Ewidencja przychodów.pdf",
            pagesize=landscape(A4),
            rightMargin=60,
            leftMargin=60,
            topMargin=42,
            bottomMargin=18,
        )
        doc.build(self.evidence)
        if platform.system() == 'Darwin':
            invoice_name = os.path.join(os.getcwd(), "Ewidencja przychodów.pdf")
            subprocess.call(['open', invoice_name])
        else:
            subprocess.Popen(["Ewidencja przychodów.pdf"], shell=True)
        return False

    def table_header(self):

        data = [
            [
                PH(r"<b>L.p.</b>", self.STYLE_JUSTIFY),
                PH(r"<b>Data wpisu</b>", self.STYLE_JUSTIFY),
                PH(r"<b>Data uzyskania przychodu</b>", self.STYLE_JUSTIFY),
                PH(
                    r"<b>Numer dowodu, na podstawie którego dokonano wpisu</b>",
                    self.STYLE_JUSTIFY,
                ),
                PH(
                    r"<b>Pzychody objęte ryczałtem os przychodów ewidencjonowanych według stawki</b>",
                    self.STYLE_JUSTIFY,
                ),
                PH(
                    r"<b>Ogółem przychody (5+6+7+8+9+10+11+12+13)</b>",
                    self.STYLE_JUSTIFY,
                ),
                PH(r"<b>Uwagi*</b>", self.STYLE_JUSTIFY),
            ]
        ]
        table = Table(data, colWidths=self.COLS_7)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)

    def table_subheader(self):

        data = [
            [
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"17%", self.STYLE_JUSTIFY),
                PH(r"15%", self.STYLE_JUSTIFY),
                PH(r"14%", self.STYLE_JUSTIFY),
                PH(r"12,5%", self.STYLE_JUSTIFY),
                PH(r"12%", self.STYLE_JUSTIFY),
                PH(r"10%", self.STYLE_JUSTIFY),
                PH(r"8,5%", self.STYLE_JUSTIFY),
                PH(r"5,5%", self.STYLE_JUSTIFY),
                PH(r"3%", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
            ]
        ]

        table = Table(data, colWidths=self.COLS_15)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)

    def table_sum_all(self, dicts_lst_all, total_amount):

        if not total_amount:
            total_amount = "..."
        else:
            total_amount = str(round(total_amount, 2)) + " zł"

        perc_dict = all_percs_dict(dicts_lst_all)

        data = [
            [
                PH(
                    rf"Suma przychodów od początku miesiąca {sum(perc_dict.values())}",
                    self.STYLE_JUSTIFY,
                ),
                PH(rf"{perc_dict.get('17%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('15%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('14%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('10%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('8,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('5,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('3%', '')}", self.STYLE_JUSTIFY_SM),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
            ]
        ]
        table = Table(data, colWidths=self.COLS_12)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)

    def page_summary(self, perc_dict):

        data = [
            [
                PH(r"Podsumowanie strony", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('17%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('15%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('14%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('10%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('8,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('5,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('3%', '')}", self.STYLE_JUSTIFY_SM),
                PH(r"", self.STYLE_JUSTIFY),
                PH(r"", self.STYLE_JUSTIFY),
            ]
        ]

        table = Table(data, colWidths=self.COLS_12)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)

    def previous_page(self, perc_dict):

        data = [
            [
                PH(r"Przeniesienie z poprzedniej strony", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('17%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('15%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('14%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('12%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('10%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('8,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('5,5%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"{perc_dict.get('3%', '')}", self.STYLE_JUSTIFY_SM),
                PH(rf"", self.STYLE_JUSTIFY),
                PH(rf"", self.STYLE_JUSTIFY),
            ]
        ]
        table = Table(data, colWidths=self.COLS_12)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)

    def numbers_row(self):
        data = [
            [
                PH(r"<b>1</b>", self.STYLE_JUSTIFY),
                PH(r"<b>2</b>", self.STYLE_JUSTIFY),
                PH(r"<b>3</b>", self.STYLE_JUSTIFY),
                PH(r"<b>4</b>", self.STYLE_JUSTIFY),
                PH(r"<b>5</b>", self.STYLE_JUSTIFY),
                PH(r"<b>6</b>", self.STYLE_JUSTIFY),
                PH(r"<b>7</b>", self.STYLE_JUSTIFY),
                PH(r"<b>8</b>", self.STYLE_JUSTIFY),
                PH(r"<b>9</b>", self.STYLE_JUSTIFY),
                PH(r"<b>10</b>", self.STYLE_JUSTIFY),
                PH(r"<b>11</b>", self.STYLE_JUSTIFY),
                PH(r"<b>12</b>", self.STYLE_JUSTIFY),
                PH(r"<b>13</b>", self.STYLE_JUSTIFY),
                PH(r"<b>14</b>", self.STYLE_JUSTIFY),
                PH(r"<b>15</b>", self.STYLE_JUSTIFY),
            ]
        ]

        table = Table(data, colWidths=self.COLS_15)
        table.setStyle(self.TABLE_STYLE)
        self.evidence.append(table)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
