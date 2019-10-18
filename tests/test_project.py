import pytest
import pandas as pd
from reframe import Relation

country = Relation("country.csv")

def test_project():
    expected = Relation("tests/test_project.csv", sep="|").reset_index().drop(columns=["index"])
    observed = country.query('continent == "North America"').project(['name','region']).reset_index().drop(columns=["index"])
    assert observed.equals(expected)
