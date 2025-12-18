from dataclasses import dataclass

# Hier werden die Daten gespeichert (im Arbeitsspeicher, global)
items = []


@dataclass
class Item:
    # Datenstruktur eines Eintrags
    text: str
    isCompleted: bool = False


def add(text):
    # Hier findet die "Ver-BBB-isierung" statt
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    items.append(Item(text))


def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted
