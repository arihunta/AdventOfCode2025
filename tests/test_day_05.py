import pytest
from aoc2025 import day_05

def test_day_05_problem_01_case_01():
    with open("./data/05_01") as f:
        assert day_05.problem_01(f.read()) == 3

def test_day_05_problem_01():
    with open("./data/05") as f:
        assert day_05.problem_01(f.read()) == 761

def test_day_05_problem_02_case_01():
    with open("./data/05_01") as f:
        assert day_05.problem_02(f.read()) == 14

def test_day_05_problem_02():
    with open("./data/05") as f:
        ans = day_05.problem_02(f.read())
        assert ans == 345755049374932
