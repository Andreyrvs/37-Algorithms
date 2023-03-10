from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(5, 4)
        encrypt_message(3, "π₯β±π·πΏπ·β±")
        encrypt_message("π₯β±π·πΏπ·β±", "π₯β±π·πΏπ·β±")
    assert encrypt_message("π₯πβ±πΏβ±π", 4) == "πβ±_πΏβ±ππ₯"
    assert encrypt_message("π₯πβ±πΏβ±π", 0) == "πβ±πΏβ±ππ₯"
    assert encrypt_message("πβ±π·πΏπ·β±", 9) == "β±π·πΏπ·β±π"
