# Copyright (c)2020 BugMaker-Project
# A Script for HashTable Searching.
class HashTable(object):
  def __init__(self, size):
    self.elem = [None for i in range(size)]
    self.count = size
  def hash(self, key):
    return key % self.count
  def insert_hash(self, key):
    address = self.hash(key)
    while self.elem[address]:
      address = (address+1) % self.count
    self.elem[address] = key
  def search_hash(self, key):
    star = address = self.hash(key)
    while self.elem[address] != key:
      address = (address + 1) % self.count
      if not self.elem[address] or address == star:
        return False
    return True