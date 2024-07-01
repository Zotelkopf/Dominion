from src.engine.card_models import Card
from src.engine.card_structs import Cardbuffer, Deck
from src.engine.cards import Copper, Estate, Province
from test_utils import makeBuffer, makeDeck, bufferHasCards


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
    source: Cardbuffer = makeBuffer([Copper(), Estate(), Copper()])
    target1: Cardbuffer = Cardbuffer()
    target2: Cardbuffer = Cardbuffer()
    def f(card: Card) -> Cardbuffer:
        return target1 if isinstance(card, Copper) else target2
    source.FilterInto(f)
    assert bufferHasCards(source, [])
    assert bufferHasCards(target1, [Copper(), Copper()])
    assert bufferHasCards(target2, [Estate()])
    source = makeBuffer([Copper(), Estate(), Copper()])
    target1 = Cardbuffer()
    target2 = Cardbuffer()
    source.FilterInto(f, 2)
    assert bufferHasCards(source, [Copper()])
    assert bufferHasCards(target1, [Copper()])
    assert bufferHasCards(target2, [Estate()])

def testAddToTop() -> None:
    deck: Deck = Deck()
    deck.addToTop(Copper())
    deck.addToTop(Estate())
    deck.addToTop(Copper())
    deck.addToTop(Province())
    assert deck.cards == [Province(), Copper(), Estate(), Copper()]
    assert deck.count == 4

def testDrawTo() -> None:
    deck: Deck = Deck()
    target: Cardbuffer = Cardbuffer()
    assert not deck.drawTo(target)
    assert bufferHasCards(deck, [])
    assert bufferHasCards(target, [])
    deck = makeDeck([Copper(), Estate(), Copper()])
    assert deck.drawTo(target)
    assert bufferHasCards(deck, [Estate(), Copper()])
    assert bufferHasCards(target, [Copper()])