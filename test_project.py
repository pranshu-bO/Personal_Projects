#this is not meant to work in the first once so don't try to
from CS50p.final_project.project import new_entry, view_report, exit_program
import os
import csv

def test_file_created():
    new_entry("2024-01-01", "test", 1.0)
    assert os.path.exists("report.csv")

def test_entry_written():
    new_entry("2024-01-01", "Coffee", 5.0)
    with open("report.csv", "r") as file:
        content = file.read()
    assert "Coffee" in content

def test_negative_amount():
    new_entry("2024-01-01", "Rent", -500)
    with open("report.csv", "r") as file:
        content = file.read()
    assert "-500" in content
