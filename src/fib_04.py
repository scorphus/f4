#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of f4
# https://github.com/scorphus/f4

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2020, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def setup():
    pass


def header():
    return ""


# ---8<---
def even_fib_sum(n):
    s = 0
    a1, a2, a3 = 1, 1, 2
    while a3 <= n:
        s += a3
        a1 = a2 + a3
        a2 = a1 + a3
        a3 = a1 + a2
    return s
