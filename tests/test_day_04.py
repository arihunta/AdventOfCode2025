import pytest
from aoc2025 import day_04

def test_day_04_problem_01_case_01():
    with open("./data/04_01") as f:
        assert day_04.problem_01(f.read()) == 13

def test_day_04_problem_01():
    with open("./data/04") as f:
        assert day_04.problem_01(f.read()) == 1480

def test_day_04_problem_02_case_01():
    with open("./data/04_01") as f:
        assert day_04.problem_02(f.read()) == 43

def test_day_04_problem_02():
    with open("./data/04") as f:
        ans = day_04.problem_02(f.read())
        assert ans == 8899
