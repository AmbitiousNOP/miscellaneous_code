#!/usr/bin/env python
from __future__ import annotations


class First:
    def process(self, item: Second) -> str:
        pass


class Second:
    def create(self, data: First) -> str:
        pass

