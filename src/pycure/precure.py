# coding: utf-8
from collections import OrderedDict


class PrecureDict(OrderedDict):
    def add(self, slug, title, broadcast_from, broadcast_to, now=False):
        if slug in self:
            raise KeyError
        if self.now:
            raise ValueError
        self[slug] = Series(slug, title, broadcast_from, broadcast_to, now)

    @property
    def now(self):
        for k, v in self.items():
            if v.now:
                return v
        return None

    @property
    def slugs(self):
        return [v.slug for k, v in self.items()]

    @property
    def series(self):
        return [v.__str__() for k, v in self.items()]


class Series(object):
    title = ""
    slug = ""
    broadcast_from = None
    broadcast_to = None
    now = False
    girls = []

    def __init__(self, slug, title, broadcast_from, broadcast_to, now=False):
        self.slug = slug
        self.title = title
        self.broadcast_from = broadcast_from
        self.broadcast_to = broadcast_to
        self.now = now

    def __str__(self):
        return self.title
