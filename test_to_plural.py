import pytest
from to_plural import to_plural

## test helper method
def check_map(plural_map):
    for singular, plural in plural_map.items():
        assert to_plural(singular) == plural


def test_endswith_m():
    plural_map = {
        'புத்தகம்' : 'புத்தகங்கள்',
        'மரம்'   : 'மரங்கள்'
    }
    check_map(plural_map)


def test_endswith_l():
    plural_map = {
        'கல்'  :  'கற்கள்',
        'சொல்'  :  'சொல்கள்',
        'பாடல்' :  'பாடல்கள்'
    }
    check_map(plural_map)


def test_endswith_nedil():
    plural_map = {
        'பூ'   :  'பூக்கள்',
        'பூங்கா' :  'பூங்காக்கள்'
    }
    check_map(plural_map)



def test_default():
    plural_map = {
        'வண்டி' :  'வண்டிகள்'
    }
    check_map(plural_map)


def test_exceptions():
    plural_map = {
        'அது'  :  'அவை ',
        'நீ'   :  'நீங்கள்'
    }
    check_map(plural_map)
