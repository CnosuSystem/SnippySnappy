# Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.

# Test if the functions in ids.py actually work.

# Check get_id

from snippysnappy import get_id


def test_get_id_sting_text_len_8():
    assert get_id("text", 8) == "982d9e3e"


def test_get_id_string_text_len_full():
    assert (
        get_id("text", 0)
        == "982d9e3eb996f559e633f4d194def3761d909f5a3b647d1a851fead67c32c9d1"
    )


def test_get_id_string_empty_len_8():
    assert get_id("", 8) == "e3b0c442"


def test_get_id_string_empty_len_full():
    assert (
        get_id("", 0)
        == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    )
