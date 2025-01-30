import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")
from generator import Generator
from main import SystemUnderTest

generator = Generator()
system = SystemUnderTest("1")

ints = [1,2,3]
strings = ["abc","def","ghi"]
int_x_int = generator.generate_combinations(None, ints, ints)
ints += [4,5]
int_x_int = generator.generate_combinations(int_x_int, ints, ints)
ints += [0, -1, 99, 100, -2, -100, 64000]
int_x_int = generator.generate_combinations(int_x_int, ints, ints)
int_x4 = generator.generate_combinations(None, ints, ints, ints, ints)
ints += [42, 77, 71, 9999, 1000000, -7]
int_x_int = generator.generate_combinations(int_x_int, ints, ints)
int_x4 = generator.generate_combinations(int_x4, ints, ints, ints, ints)
int_x8 = generator.generate_combinations(None, ints, ints, ints, ints, ints, ints, ints, ints)

def test_add_function(snapshot):
        for test_tuple in int_x_int:
            print(test_tuple)
            # 1-n
            assert system.add(*test_tuple) == snapshot

def test_subtract_function(snapshot):
        for test_tuple in int_x_int:
            print(test_tuple)
            assert system.sub(*test_tuple) == snapshot

def test_mean_function(snapshot):
    for test_tuple in int_x4:
        print(test_tuple)
        assert system.mean(*test_tuple) == snapshot

def test_concat_function(snapshot):
    for test_tuple in int_x8:
        print(test_tuple)
        assert system.concat(*test_tuple) == snapshot
