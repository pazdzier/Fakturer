from datetime import date
import os
import logging.config
import sys
import locale
import platform
from PySide6.QtWidgets import QApplication
from database.models import (
    session_manager,
    engine,
    mapper_registry,
)

if platform.system() != 'Darwin':
    # Linux: Linux
    # Mac: Darwin
    # Windows: Windows
    locale.setlocale(locale.LC_ALL, "pl_PL.utf8")

from gui.main import MainWindow


if __name__ == "__main__":
    if not os.path.isdir(os.path.join(os.getcwd(), "dev_tools", "logs")):
        os.mkdir(os.path.join(os.getcwd(), "dev_tools", "logs"))
    logging.config.fileConfig(
        os.path.join(os.getcwd(), "static", "logging_config.ini"),
        defaults={"logfilename": f"{date.today()}.txt"},
    )
    app = QApplication(sys.argv)
    with session_manager(engine, mapper_registry) as session:
        w = MainWindow(session)
        w.show()
        logging.shutdown()
        sys.exit(app.exec())
