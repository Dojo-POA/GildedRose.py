# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                LegendaryItem(item).update()
                continue

            if item.name == "Aged Brie":
                AgedItem(item).update()
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                TicketItem(item).update()
                continue


            RichItem(item).update()

class RichItem:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.decrease_quality()

        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.decrease_quality()

    def increase_quality(self, by=1):
        if self.item.quality < 50:
            self.item.quality += by

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1


class LegendaryItem(RichItem):
    def update(self):
        pass

class AgedItem(RichItem):
    def update(self):
        self.increase_quality()
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.increase_quality()

class TicketItem(RichItem):

    def update(self):
        self.increase_quality()

        if self.item.sell_in in range(6, 11):
            self.increase_quality()

        if self.item.sell_in in range(0, 6):
            self.increase_quality(by=2)

        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
