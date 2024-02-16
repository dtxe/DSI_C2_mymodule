import math
import argparse 

def hello_world():
    print("Hello, world!")
    
def calc_area_rectangle(side1_length, side2_length):
    return side1_length * side2_length

def calc_area_circle(radius):
    if not isinstance(radius, (float, int)):
        raise TypeError(f'radius is {radius} but should be a number')
    if radius < 0:
        raise ValueError(f'radius is {radius} but must be positive')
    return math.pi * radius ** 2

def calc_area_cmdinterface():
    parser = argparse.ArgumentParser()
    parser.add_argument('shape', choices = ['rectangle', 'circle'])
    parser.add_argument('dimension', nargs='+')
    args = parser.parse_args()

    if args.shape == 'circle':
        print(calc_area_circle(float(args.dimension[0])))
    elif args.shape == 'rectangle':
        print(calc_area_rectangle(
            float(args.dimension[0]), 
            float(args.dimension[1])
            ))
    else:
        raise NotImplementedError('unknown shape')
    