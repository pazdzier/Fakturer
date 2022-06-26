"""
..note::
    Moduł zawiera funkcje generujące fake'owe dane do db na potrzeby developmentu.

"""
from datetime import date
from random import randint, choice
from database.models import (
    session_manager,
    engine,
    mapper_registry,
    Contractor,
    User,
    Service,
)
from faker import Faker

FAKER = Faker("pl_PL")


def fake_user():
    """Tworzy w db fejkowego użytkownika"""

    with session_manager(engine, mapper_registry) as session:
        user = User(
            first_name=FAKER.first_name(),
            last_name=FAKER.last_name(),
            company_name="TACO",
            street=FAKER.street_address(),
            city=FAKER.city(),
            zip_code=FAKER.postcode(),
            nip=FAKER.nip(),
            account_number=f"{randint(10000000000000000000000000,99999999999999999999999999)}",
        )
        session.add(user)
        print(f"Użytkownik: {user.first_name} {user.last_name} został dodany")
        session.commit()


def fake_contractor(num_to_create: int):
    """Tworzy w db kontrahentów w ilości = num_to_create"""

    with session_manager(engine, mapper_registry) as session:
        for _ in range(num_to_create):
            contractor = Contractor(
                company_name=FAKER.company(),
                nip=FAKER.nip(),
                street=FAKER.street_address(),
                city=FAKER.city(),
                zip_code=FAKER.postcode(),
                default=False,
            )
            session.add(contractor)
            print(f"Dodano Kontrahenta: {contractor.company_name}")
        session.commit()


def fake_service():
    """Tworzy w db rekord usługi"""

    with session_manager(engine, mapper_registry) as session:
        service = Service(
            name=f"Świadczenie usług programistycznych zgodnie z umową z \
dnia {date.today().strftime('%d.%m.%Y')}",
            amount=2450,
            percentage=choice(['17%', '15%', '14%', '12,5%', '12%', '10%', '8,5%', '5,5%', '3%'])
        )
        session.add(service)
        print("Dodano usługę")
        session.commit()
