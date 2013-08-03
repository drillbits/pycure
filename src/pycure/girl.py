# coding: utf-8
class Girl(object):
    _name = ""
    _precure_name = ""
    _transformed = False
    prologue = None

    def __init__(self, name, precure_name, prologue):
        self._name = name
        self._precure_name = precure_name
        self.prologue = prologue

    def __str__(self):
        return "{name}({precure_name})".format(
            name=self._name,
            precure_name=self._precure_name)

    @property
    def name(self):
        if self._transformed:
            return self._precure_name
        else:
            return self._name

    def transform(self, stdout=True):
        self._transformed = True
        if stdout:
            print(self.prologue)
        else:
            return self.prologue


class PartnerInvalidError(Exception):
    pass


class FirstGirl(Girl):
    partner = None

    def transform(self, partner_name=None):
        if self.partner:
            return self.transform_with(partner_name)
        else:
            return super().transform()

    def transform_with(self, partner_name):
        if partner_name == self.partner._name:
            self.partner._transformed = True
            return super().transform()
        else:
            raise PartnerInvalidError
