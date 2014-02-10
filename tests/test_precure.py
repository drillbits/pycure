import unittest
from datetime import date

from testfixtures import compare
from testfixtures import Comparison as C
from testfixtures import ShouldRaise


class TestPrecureDictAdd(unittest.TestCase):
    def _getTarget(self):
        from pycure.precure import PrecureDict
        return PrecureDict()

    def _callFUT(self, dct, *args, **kwargs):
        return dct.add(*args, **kwargs)

    def test_add(self):
        dct = self._getTarget()
        self._callFUT(dct, "test", "テスキュア", date(2014, 5, 23), None, True)

        from pycure.precure import Series
        compare(C(
            Series,
            strict=False,
            slug="test",
            title="テスキュア",
            broadcast_from=date(2014, 5, 23),
            broadcast_to=None,
            now=True), dct["test"])

    def test_duplicated_slug(self):
        dct = self._getTarget()
        dct["test"] = "spam"
        with ShouldRaise(KeyError):
            self._callFUT(dct, "test", "テスキュア", date(2014, 5, 23), None,
                          True)

    def test_duplicated_now(self):
        dct = self._getTarget()
        from pycure.precure import Series
        dct["now"] = Series("now", "ナウキュア", date(2014, 5, 23), None, True)
        with ShouldRaise(ValueError):
            self._callFUT(dct, "test", "テスキュア", date(2014, 5, 23), None,
                          True)


class TestPrecureDictNow(unittest.TestCase):
    def _getTarget(self):
        from pycure.precure import PrecureDict
        return PrecureDict()

    def _callFUT(self, dct):
        return dct.now

    def test_now(self):
        dct = self._getTarget()
        from pycure.precure import Series
        dct["test"] = Series("test", "テスキュア", date(2014, 5, 23), None,
                             True)
        now = self._callFUT(dct)

        from pycure.precure import Series
        compare(C(
            Series,
            strict=False,
            slug="test",
            title="テスキュア",
            broadcast_from=date(2014, 5, 23),
            broadcast_to=None,
            now=True), now)

    def test_no_now(self):
        dct = self._getTarget()
        from pycure.precure import Series
        dct["test"] = Series("test", "テスキュア", date(2014, 5, 23), None,
                             False)
        now = self._callFUT(dct)

        compare(now, None)


class TestPrecureDictSlugs(unittest.TestCase):
    def _getTarget(self):
        from pycure.precure import PrecureDict
        return PrecureDict()

    def _callFUT(self, dct):
        return dct.slugs

    def test_slugs(self):
        dct = self._getTarget()
        from pycure.precure import Series
        dct["spam"] = Series("spam", "スパキュア",
                             date(2013, 5, 23), date(2014, 5, 16))
        dct["ham"] = Series("ham", "ハムキュア",
                            date(2014, 5, 23), None, True)
        slugs = self._callFUT(dct)

        compare(slugs, ["spam", "ham"])


class TestPrecureDictSeries(unittest.TestCase):
    def _getTarget(self):
        from pycure.precure import PrecureDict
        return PrecureDict()

    def _callFUT(self, dct):
        return dct.series

    def test_series(self):
        dct = self._getTarget()
        from pycure.precure import Series
        dct["spam"] = Series("spam", "スパキュア",
                             date(2013, 5, 23), date(2014, 5, 16))
        dct["ham"] = Series("ham", "ハムキュア",
                            date(2014, 5, 23), None, True)
        series = self._callFUT(dct)

        compare(series, ["スパキュア", "ハムキュア"])
