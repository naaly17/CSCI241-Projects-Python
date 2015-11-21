__author__ = 'nadiaaly'

class BTSMap:

 def __init__(self):
    self._root = None
    self._size = 0


class _BTSMapNode( object ):
    def __init__( self, key, data ):
        self.key = key
        self.data = data
        self.left = None
        self.right = None