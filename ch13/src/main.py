from ch13.proto.mat import Matrix
from ch13.utils.mat_mul import mat_mul
import sys

if __name__ == '__main__':
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])

    print(mat_mul(a, b).data)
    print(sys.path)
