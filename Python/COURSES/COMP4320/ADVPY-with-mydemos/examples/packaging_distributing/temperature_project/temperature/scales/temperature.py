#!/usr/bin/env python

DEGREES = '°'    # '\u00b0'
FREEZING_PT_C = 0
FREEZING_PT_F = 32
FREEZING_PT_K = 273.15
BOILING_PT_C = 100
BOILING_PT_F = 212
BOILING_PT_K = 373.15


def c2f(temp):
    return float(temp) * 9 / 5 + 32


def c2k(temp):
    return float(temp) + 273.15


def f2c(temp):
    return (float(temp) - 32) * 5 / 9


def f2k(temp):
    return c2k(f2c(temp))


def k2c(temp):
    return float(temp) - 273.15


def k2f(temp):
    return k2c(f2c(temp))
