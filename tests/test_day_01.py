import pytest
from aoc2025 import day_01

def test_day_01_problem_01_case_01():
    with open("./data/01_01") as f:
        assert day_01.problem_01(f.read()) == 3

def test_day_01_problem_01():
    with open("./data/01") as f:
        assert day_01.problem_01(f.read()) == 1168

def test_day_01_problem_02_case_01():
    with open("./data/01_01") as f:
        assert day_01.problem_02(f.read()) == 6

def test_day_01_problem_02():
    with open("./data/01") as f:
        ans = day_01.problem_02(f.read())
        assert ans == 7199
