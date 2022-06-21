from runtime.src import crud
from runtime.src.db.session import db_session
from runtime.src.models.item import ItemCreate, ItemUpdate
from runtime.tests.utils.utils import random_lower_string


def test_create_item():
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = crud.item.create(db_session=db_session, item_in=item_in)
    assert item.title == title
    assert item.description == description


def test_get_item():
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = crud.item.create(db_session=db_session, item_in=item_in)
    stored_item = crud.item.get(db_session=db_session, _id=item.id)
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.description == stored_item.description


def test_update_item():
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = crud.item.create(db_session=db_session, item_in=item_in)
    description2 = random_lower_string()
    item_update = ItemUpdate(description=description2)
    item2 = crud.item.update(
        db_session=db_session, item=item, item_in=item_update
    )
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.description == description2


def test_delete_item():
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = crud.item.create(db_session=db_session, item_in=item_in)
    item2 = crud.item.remove(db_session=db_session, _id=item.id)
    item3 = crud.item.get(db_session=db_session, _id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.description == description
