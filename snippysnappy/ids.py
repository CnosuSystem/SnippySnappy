# Copyright Cnosu System 2026. GPLv3 license, see the LICENSE.md file.

import hashlib


def get_id(string: str, len: int) -> str:
    if len == 0:
        return hashlib.sha256(string.encode("utf-8")).hexdigest()
    else:
        return hashlib.sha256(string.encode("utf-8")).hexdigest()[:len]
