import pytest
from aoc2025 import day_03

def test_day_03_problem_01_case_01():
    with open("./data/03_01") as f:
        assert day_03.problem_01(f.read()) == 357

def test_day_03_problem_01():
    with open("./data/03") as f:
        assert day_03.problem_01(f.read()) == 17766

def test_day_03_problem_02_case_01():
    with open("./data/03_01") as f:
        assert day_03.problem_02(f.read()) == 3121910778619

def test_day_03_problem_02():
    with open("./data/03") as f:
        ans = day_03.problem_02(f.read())
        assert ans == 176582889354075
