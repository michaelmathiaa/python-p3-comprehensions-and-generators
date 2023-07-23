#!/usr/bin/env python3

def return_evens(num_list):
    return [number for number in num_list if number % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]