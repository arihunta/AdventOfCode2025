import pytest
from aoc2025 import day_02

def test_day_02_problem_01_case_01():
    with open("./data/02_01") as f:
        assert day_02.problem_01(f.read()) == 1227775554

def test_day_02_problem_01():
    with open("./data/02") as f:
        assert day_02.problem_01(f.read()) == 40055209690

def test_day_02_problem_02_case_01():
    with open("./data/02_01") as f:
        assert day_02.problem_02(f.read()) == 4174379265

def test_day_02_problem_02():
    with open("./data/02") as f:
        ans = day_02.problem_02(f.read())
        assert ans == 50857215650
