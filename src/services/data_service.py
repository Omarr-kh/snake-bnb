from typing import List

from data.cages import Cage
from data.owners import Owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()

    return owner


def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects(email=email).first()
    return owner


def register_cage(active_account: Owner,
                  name: str, allow_dangerous: bool,
                  has_toys: bool, carpeted: bool,
                  meters: float,
                  price: float) -> Cage:
    cage = Cage()

    cage.name = name
    cage.allow_dangerous_snakes = allow_dangerous
    cage.has_toys = has_toys
    cage.square_meters = meters
    cage.is_carpetd = carpeted
    cage.price = price

    cage.save()

    account = find_account_by_email(active_account.email)
    account.cage_ids.append(cage.id)
    account.save()

    return cage


def find_cages_for_user(account: Owner) -> List[Cage]:
    query = Cage.objects(id__in=account.cage_ids)
    cages = list(query)
    return cages
