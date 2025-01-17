class Color:
    def __init__(self, hexcode) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, rgb):
        if isinstance(rgb, str) and len(rgb) == 6:
            self.r = int(rgb[:2], 16)
            self.g = int(rgb[2:4], 16)
            self.b = int(rgb[4:6], 16)
            self._hexcode = rgb


