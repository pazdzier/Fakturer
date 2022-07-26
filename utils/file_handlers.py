"""
.. note::
    Moduł zawiera funkcje umożliwiające eksport/import danych w róźnych formatach.

"""

from datetime import datetime
import json
import re
import os
import subprocess
from json.decoder import JSONDecodeError
from sqlalchemy.orm.query import Query
from PySide6.QtWidgets import QFileDialog, QMessageBox
from utils.constants import STATIC


def save_to_json(parent, query: Query) -> None:
    """
    .. note::
        Przyjmuje queryset i zapisuje go do pliku w formacie
        *.json celem archiwizacji / backup'u
    """

    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Eksportuj do formatu JSON",
        "",
        "JavaScript Object Notation File (*.json)",
        options=options
    )
    if not filename:
        return None
    if not filename.endswith('.json'):
        filename += '.json'
    file = open(filename, 'w')
    try:
        result = json.dumps(
            [contractor.to_json() for contractor in query]
        )
    except TypeError:
        # when query is just one record
        result = json.dumps(query.to_json())
    file.write(result)
    file.close()
    QMessageBox.information(
        parent,
        "Sukces",
        f"Rekordy zostały prawidłowo wysłane do pliku:\n{filename}"
    )
    return None

def save_from_json(parent, db_model):

    filename = QFileDialog.getOpenFileName(
        parent,
        "Importuj z pliku JSON",
        "",
        "JavaScript Object Notation File (*.json)",
    )
    if filename[0]:
        try:
            file = open(filename[0], 'r')
            records = json.loads(file.read())
            for record in records:
                item = db_model(**record)
                parent.session.add(item)
            parent.session.commit()
            QMessageBox.information(
                parent,
                "Sukces",
                "Rekordy zostały poprawnie zaimportowane z pliku źródłowego"
            )
        except (TypeError, UnicodeDecodeError, JSONDecodeError):
            QMessageBox.critical(
                parent,
                "Błąd",
                "Nie udało się zaimportować rekordów, plik źródłowy jest \
nieprawidłowy lub uszkodzony"
            )

def git_history_to_json():

    result = subprocess.check_output(['git', 'log'])
    result = result.decode('utf-8')
    dates = re.findall(r'Date:\s*(.*)?\+\d*', result)
    dates = [
        str(datetime.strptime(i.strip(), '%a %b %d %H:%M:%S %Y')) for i in dates
    ]
    descriptions = list(map(str.strip, result.split('\n\n')[1::2]))
    result = json.dumps(list(zip(dates, descriptions)))
    with open(os.path.join(STATIC, 'history.json'), 'w') as file:
        file.write(result)
