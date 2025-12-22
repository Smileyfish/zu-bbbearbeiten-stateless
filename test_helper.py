import pytest
import helper
import datetime

def test_download():
    # Given: I have entered a whole bunch of todos
    todos = [
        {
            "title": "Kommentieren, mit Emojis",
            "date": "2023-10-31",
            "category": "Kunst",
            "description": "Die gesamte Code-Base mit aussagekräftigen Kommentaren versehen, die nur aus Emojis bestehen",
        },
        {
            "title": "Hello World-AI",
            "date": "2023-10-01",
            "category": "Hausaufgaben",
            "description": "Eine AI trainieren, die darauf spezialisiert ist, Hello World-Programme zu generieren",
        },
    ]

    for todo in todos:
        helper.add(
            todo["title"],
            date=todo["date"],
            category=todo["category"],
            description=todo["description"],
        )

    # When: I click the download button
    data = helper.get_csv()

    # Then: I receive a file in CSV format
    assert (
        f'"{todos[0]["title"]}",31.10.2023,{todos[0]["category"]},"{todos[0]["description"]}"'
        in data
    )
    assert (
        f'{todos[1]["title"]},01.10.2023,{todos[1]["category"]},"{todos[1]["description"]}"'
        in data
    )

def test_add():
    # Given: I want to add a to-do with a date
    text = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(text, date)

    # Then: The most recently added to-do should have a date
    item = helper.items[-1]
    assert isinstance(item.date, datetime.date)
