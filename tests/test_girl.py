import unittest
from unittest.mock import Mock

from testfixtures import compare
from testfixtures import OutputCapture
from testfixtures import ShouldRaise


class TestGirlName(unittest.TestCase):
    def _getTarget(self, *args, **kwargs):
        from pycure.girl import Girl
        return Girl(*args, **kwargs)

    def _callFUT(self, girl):
        return girl.name

    def test_before_transform(self):
        girl = self._getTarget(
            'ねじめじろう',
            'ネジキュア',
            'はい')
        name = self._callFUT(girl)

        compare(name, 'ねじめじろう')

    def test_after_transform(self):
        girl = self._getTarget(
            'ねじめじろう',
            'ネジキュア',
            'はい')
        girl._transformed = True
        name = self._callFUT(girl)

        compare(name, 'ネジキュア')


class TestGirlTransform(unittest.TestCase):
    def _getTarget(self, *args, **kwargs):
        from pycure.girl import Girl
        return Girl(*args, **kwargs)

    def _callFUT(self, girl, stdout):
        return girl.transform(stdout)

    def test_stdout(self):
        girl = self._getTarget(
            'ねじめじろう',
            'ネジキュア',
            'はい')
        with OutputCapture() as output:
            self._callFUT(girl, True)

        output.compare('はい')

    def test_not_stdout(self):
        girl = self._getTarget(
            'ねじめじろう',
            'ネジキュア',
            'はい')
        result = self._callFUT(girl, False)

        compare(result, 'はい')


class TestFirstGirlTransform(unittest.TestCase):
    def _getTarget(self, *args, **kwargs):
        from pycure.girl import FirstGirl
        return FirstGirl(*args, **kwargs)

    def _callFUT(self, girl, partner_name, stdout):
        return girl.transform(partner_name, stdout)

    def test_has_partner(self):
        girl1 = self._getTarget(
            'ねじめ',
            'キュアドリル',
            'はい')
        girl2 = self._getTarget(
            'じろう',
            'キュアビッツ',
            'はいじゃないが')
        girl1.partner = girl2
        girl2.partner = girl1
        girl1.transform_with = Mock()
        self._callFUT(girl1, 'じろう', False)

        compare(girl1.transform_with.call_count, 1)

    def test_no_partner(self):
        girl1 = self._getTarget(
            'ねじめ',
            'キュアドリル',
            'はい')
        girl1.transform_with = Mock()
        self._callFUT(girl1, 'じろう', False)

        compare(girl1.transform_with.call_count, 0)


class TestFirstGirlTransformWith(unittest.TestCase):
    def _getTarget(self, *args, **kwargs):
        from pycure.girl import FirstGirl
        return FirstGirl(*args, **kwargs)

    def _callFUT(self, girl, partner_name, stdout):
        return girl.transform_with(partner_name, stdout)

    def test_transform(self):
        girl1 = self._getTarget(
            'ねじめ',
            'キュアドリル',
            'はい')
        girl2 = self._getTarget(
            'じろう',
            'キュアビッツ',
            'はいじゃないが')
        girl1.partner = girl2
        girl2.partner = girl1
        result = self._callFUT(girl1, 'じろう', False)

        compare(result, 'はい')

    def test_invalid_partner(self):
        girl1 = self._getTarget(
            'ねじめ',
            'キュアドリル',
            'はい')
        girl2 = self._getTarget(
            'じろう',
            'キュアビッツ',
            'はいじゃないが')
        girl1.partner = girl2
        girl2.partner = girl1
        from pycure.girl import PartnerInvalidError
        with ShouldRaise(PartnerInvalidError):
            self._callFUT(girl1, 'しろう', False)
