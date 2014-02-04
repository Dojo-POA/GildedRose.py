# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item, by=1):
        if item.quality < 50:
            item.quality += by

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                self.increase_quality(item)
                item.sell_in -= 1
                if item.sell_in < 0:
                    self.increase_quality(item)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increase_quality(item)

                if item.sell_in in range(6, 11):
                    self.increase_quality(item)

                if item.sell_in in range(0, 6):
                    self.increase_quality(item, by=2)

                item.sell_in -= 1

                if item.sell_in < 0:
                    item.quality = 0

                continue


            self.decrease_quality(item)

            item.sell_in -= 1

            if item.sell_in < 0:
                self.decrease_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
