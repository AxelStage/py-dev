#!/usr/bin/env python
# coding: utf-8

# # Type hints

def greeting_dyn(name):
    return "Hello " + name

def greeting_stat(name: str) -> str:
    return "Hi " + name

greeting_dyn(1)

