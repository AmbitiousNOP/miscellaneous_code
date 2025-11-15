#!/usr/bin/env python
from typing import List, Any, Optional


def append_42(coll: Optional[List[Any]] = None) -> List[Any]:
    if coll is None:
        coll = []

    coll.append(42)
    return coll
