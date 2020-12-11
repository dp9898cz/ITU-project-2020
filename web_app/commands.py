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
                    c_type = CleanupType.Preduklid,
                    to_be_completed = datetime.datetime.now()
                ),
                Cleanup(
                    c_type = CleanupType.Standartni,
                    to_be_completed = datetime.datetime.now()
                ),
                Cleanup(
                    c_type = CleanupType.Standartni,
                    to_be_completed = datetime.datetime.now()
                )
            ],
            faults = [
                Fault(
                    description = 'Chybí žárovka v koupelně.',
                ),
                Fault(
                    description = 'Rozbitá noha od postele.',
                ),
                Fault(
                    description = 'Nefunguje fén na vlasy.',
                ),
            ],
            discoveries = [
                Discovery(
                    description = "Na zemi ležel bílý ručník.",
                ),
                Discovery(
                    description = "V nočním stolku nalezen balíček kondomů.",
                ),
                Discovery(
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

        db.session.add(room1)
        db.session.add(room2)
        db.session.add(room3)
        db.session.add(room4)

        db.session.commit()

