__author__ = 'Nadia Aly'
from array_2d import Array2D
from arrayadt import Array
from _arrayIterator import _ArrayIterator


class PPMImage():
#
    def __init__(self, w, h):

        self.width = w
        self.height = h
        self.flag_array = Array2D(self.height,self.width)

    def __setitem__(self, key, value):

        self.flag_array[key] = value

    def writeToFile(self,output):

        # write header - looks most like the ppm guidelines
        header = bytes("P6\n%d %d 255\n" % (self.width, self.height),'ascii')
        write_flag = open(output,mode='wb')
        write_flag.write(header)
        for i in range(self.height):
            for j in range(self.width):
                r, g, b = self.flag_array[i,j]
                r.to_bytes(1,'big')
                g.to_bytes(1,'big')
                b.to_bytes(1,'big')
                k = Array(3)
                k[0] = r
                k[1] = g
                k[2] = b
                working = bytearray(k)
                write_flag.write(working)



