from dice import item
from dice.utils import base


class Item(item.ItemBase):
    def run(self):
        cmdline = './pyramid'
        cmdline += ' %s' % base.escape(str(self.get('option')))
        self.res = base.run(cmdline)
