import pytest

def test_screenshot_on_test_failure(browser):
    browser.get("https://www.example.com")
    assert True
    # assert False  # This will fail and trigger a screenshot



def test_addition():
    assert 1 + 1 == 2, "Addition test failed"

def test_subtraction():
    assert 5 - 3 == 2, "Subtraction test failed"

def test_multiplication():
    assert 2 * 3 == 6, "Multiplication test failed"

def test_division():
    assert 6 / 2 == 3, "Division test failed"