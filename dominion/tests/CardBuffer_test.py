import pytest
from src.engine.card_models import Card
from src.engine.card_structs import Cardbuffer
from src.engine.cards import Copper, Estate, Province


def makeBuffer(cards: list[Card]) -> Cardbuffer:
    buffer: Cardbuffer = Cardbuffer()
    buffer.cards = cards
    buffer.count = len(cards) 
    return buffer

def bufferHasCards(buffer: Cardbuffer, cards: list[Card]) -> bool:
    if buffer.count == len(cards) and buffer.cards == cards:
        return True
    return False


def testReceive() -> None:
    buffer: Cardbuffer = Cardbuffer()
    buffer.receive(Copper())
    buffer.receive(Estate())
    buffer.receive(Copper())
    buffer.receive(Province())
    assert buffer.cards == [Copper(), Estate(), Copper(), Province()]
    assert buffer.count == 4

def testRemove() -> None:
    buffer: Cardbuffer = makeBuffer([Copper(), Estate(), Copper()])
    assert not buffer.remove(Province())
    assert buffer.remove(Copper())
    assert buffer.cards == [Estate(), Copper()]
    assert buffer.count == 2

def testRemoveTop() -> None:
    buffer: Cardbuffer = Cardbuffer()
    assert buffer.removeTop() is None
    assert buffer.cards == []
    assert buffer.count == 0
    buffer = makeBuffer([Copper(), Estate(), Copper()])
    assert buffer.removeTop() == Copper()
    assert buffer.cards == [Estate(), Copper()]
    assert buffer.count == 2

def testMoveTo() -> None:
    source: Cardbuffer = makeBuffer([Copper(), Estate(), Copper()])
    target: Cardbuffer = Cardbuffer()
    assert not source.moveTo(Province(), target)
    assert source.moveTo(Copper(), target)
    assert bufferHasCards(source, [Estate(), Copper()])
    assert bufferHasCards(target, [Copper()])

def testDumpTo() -> None:
    source: Cardbuffer = makeBuffer([Copper(), Estate(), Copper()])
    target: Cardbuffer = Cardbuffer()
    source.dumpTo(target)
    assert bufferHasCards(source, [])
    assert bufferHasCards(target, [Copper(), Estate(), Copper()])

def testFilterInto() -> None:
    pass