import datetime

from web_app.extensions import db
from web_app.models import *

def register_commands(app):
    @app.cli.command(name='create_db', help="Create empty database.")
    def create_db():
        db.create_all()

    @app.cli.command(name='fill_db', help='Fill up DB with sample data')
    def fill_db():
        room1 = Room(
            number = 22,
            r_type = RoomType.Economy,
            cleanups = [
                Cleanup(
                    c_type = CleanupType.Minibar,
                    to_be_completed = datetime.datetime.now()
                ),
                Cleanup(
                    c_type = CleanupType.Předúklid,
                    to_be_completed = datetime.datetime.now()
                ),
                Cleanup(
                    c_type = CleanupType.Standartní,
                    to_be_completed = datetime.datetime.now()
                ),
                Cleanup(
                    c_type = CleanupType.Kompletní,
                    to_be_completed = datetime.datetime.now()
                )
            ],
            faults = [
                Fault(
                    description = 'Chybí žárovka v koupelně.',
                    date = datetime.datetime.now(),
                ),
                Fault(
                    description = 'Rozbitá noha od postele.',
                    date = datetime.datetime.now(),
                ),
                Fault(
                    description = 'Nefunguje fén na vlasy.',
                    date = datetime.datetime.now(),
                ),
            ],
            discoveries = [
                Discovery(
                    date = datetime.datetime.now(),
                    description = "Na zemi ležel bílý ručník.",
                ),
                Discovery(
                    date = datetime.datetime.now(),
                    description = "V nočním stolku nalezen balíček kondomů.",
                ),
                Discovery(
                    date = datetime.datetime.now(),
                    description = "Ve skrini nalezena penezenka.",
                ),
            ],
        )
        room2 = Room(
            number = 33,
            r_type = RoomType.Business,
        )
        room3 = Room(
            number = 11,
            r_type = RoomType.Premium,
        )
        room4 = Room(
            number = 44,
            r_type = RoomType.Economy,
        )

        admin = User(
            name = "Admin",
            surname = "Admin",
            login = "admin",
            unhashed_password = "admin",
            isAdmin = True,
        )

        janitor = User(
            name = "Uklizecka",
            surname = "Nejaka",
            login = "janitor",
            unhashed_password = "janitor",
            isAdmin = False,
        )

        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)
        db.session.add(admin)
        db.session.add(janitor)

        db.session.commit()

