from Tiles.Tile import Tile


class PathableTile(Tile):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pathable = True
        pass
