"""
    Testing dict_validator.py
"""

#import pytest
from dict_validator import match_keys, match_types, recurse_validate

class TestMatchKeys:
    """
        Test function match_keys
    """

    p = "path.to"
    schema = {
            "a": int,
            "b": int,
            "c": {
                "c1": int
        }}

    def test_equal_keys(self):
        d = {
            "a": "wrong_type",
            "b": 1,
            "c": {
                "wrong_key": "wrong_type"
            }}
        test = match_keys(d,TestMatchKeys.schema,TestMatchKeys.p)
        expect = True, None
        assert test == expect

    def test_missing_keys(self):
        d = {
            "a": "wrong_type",
            "c": {
                "wrong_key": "wrong_type"
            }}
        test = match_keys(d,TestMatchKeys.schema,TestMatchKeys.p)
        expect = False, "Missing keys: path.to.b "
        assert test == expect

    def test_extra_keys(self):
        d = {
            "a": "wrong_type",
            "b": 1,
            "c": {
                "wrong_key": "wrong_type",
                "extra_key": 1
                },
            "extra_key": 1,
            }
        test = match_keys(d,TestMatchKeys.schema,TestMatchKeys.p)
        expect = False, " Extra keys: path.to.extra_key"
        assert test == expect

    def test_missing_extra_keys(self):
        d = {
            "a": "wrong_type",
            "c": {
                "wrong": "wrong_type",
                "c_extra_key": 1
                },
            "extra_key": 1,
            }
        test = match_keys(d,TestMatchKeys.schema,TestMatchKeys.p)
        expect = False, "Missing keys: path.to.b Extra keys: path.to.extra_key"
        assert test == expect

class TestMatchTypes:
    """
        Test function match_types
    """

    path = "path.to"
    schema = {
            "a": int,
            "b": str,
            "c": {
                "d": int
            }
        }

    def test_equal_types(self):
        data = {
            "a": 100,
            "b": "test",
            "c": {
                "d": "wrong_type"
            }}
        test = match_types(
            data,
            TestMatchTypes.schema,
            TestMatchTypes.path)
        expect = True, None
        assert test == expect

    def test_wrong_type(self):
        data = {
            "a": 1,
            "b": "abc",
            "c": ""
            }
        test = match_types(
            data,
            TestMatchTypes.schema,
            TestMatchTypes.path)
        expect = False, "incorrect type path.to.c -> expected dict, found str"
        assert test == expect

class TestRecurseValidate:
    """
        Test function recurse_validate
    """

    path = "root"
    template = {
    "user_id": int,
    "name": {
        "first": str,
        "last": str
    },
    "bio": {
        "dob": {
            "year": int,
            "month": int,
            "day": int
        },
        "birthplace": {
            "country": str,
            "city": str
            }
        }
    }

    def test_equal_schema(self):
        data = {
            "user_id": 100,
            "name": {
                "first": "John",
                "last": "Cleese"
            },
            "bio": {
                "dob": {
                    "year": 1939,
                    "month": 11,
                    "day": 27
                },
                "birthplace": {
                    "country": "United Kingdom",
                    "city": "Weston-super-Mare"
                }
            }
        }
        test = recurse_validate(data, TestRecurseValidate.template, TestRecurseValidate.path)
        expect = True, None
        assert test == expect

    def test_wrong_schema_1(self):
        data = {
            "user_id": 102,
            "name": {
                "first": "Michael",
                "last": "Palin"
            },
            "bio": {
                "dob": {
                    "year": 1943,
                    "month": "May",
                    "day": 5
                },
                "birthplace": {
                    "country": "United Kingdom",
                    "city": "Sheffield"
                }
            }
        }
        test = recurse_validate(data, TestRecurseValidate.template, TestRecurseValidate.path)
        expect = False, "incorrect type root.bio.dob.month -> expected int, found str"
        assert test == expect