"""Tests of the Vector class"""

from vectors import Vector


def test_init():
    """Test the x and y properties after initialization."""
    v = Vector(1, 2)
    assert v.dx == 1
    assert v.dy == 2


def test_from_two_points():
    """Test the x and y properties after initialization with the from_two_points constructor."""


def test_negation():
    """Test taking the negative of a vector (-v) works and gives the right result."""


def test_addition():
    """Test that adding two vectors works and gives the right result."""


def test_subtraction():
    """Test that subtracting two vectors works and gives the right result."""


def test_multiplication_by_scalar():
    """Test that multiplying a vector by a scalar number works and gives the right result."""


def test_dot_product():
    """Test the dot_product of two vectors."""


def test_magnitude_product():
    """Test the magnitude of a vector."""
