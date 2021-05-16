from datetime import date
import os
import logging.config
import sys
import locale
from PySide2.QtWidgets import QApplication
from database.models import (
    session_manager,
    engine,
    mapper_registry,
)

locale.setlocale(locale.LC_ALL, "pl")

from gui.main import MainWindow


if __name__ == "__main__":

    logging.config.fileConfig(
        os.path.join(os.getcwd(), "static", "logging_config.ini"),
        defaults={"logfilename": f"{date.today()}.txt"}
    )
    app = QApplication(sys.argv)
    with session_manager(engine, mapper_registry) as session:
        w = MainWindow(session)
        w.show()
        logging.shutdown()
        sys.exit(app.exec_())
