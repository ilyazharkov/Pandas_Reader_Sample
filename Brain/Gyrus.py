import zope.interface
from enum import Enum


class EMention(Enum):
    Positive = 1
    Negative = 0


class EGyrusTypes(Enum):
    TextAnalyzer = 1
    PricePredict = 2
    CandlePredict = 3


class IClassifyText(zope.interface.Interface):
    def ClassifyText(self, inputText):
        return "Any Text"


class GyrusBase(object):
    def __init__(self):
        self.Name = 'Base'

    def doTeaching(self):
        pass


class GyrusTextAnalyzer(GyrusBase):
    zope.interface.implements(IClassifyText)

    def __init__(self):
        GyrusBase.__init__(self)
        self.Name = 'TextSimple'
    def doTeaching(self):
        pass
    def ClassifyText(self, inputText):
        if inputText != "":
            return EMention.Positive
        else:
            return EMention.Negative


class GyrusFactory(object):
    def __init__(self):
        self.objects = []
        self.objects.append(GyrusTextAnalyzer())

    def GetInstnaces(self, if_gyrus_type: EGyrusTypes):
        result = []
        for obj in self.objects:
            if if_gyrus_type == EGyrusTypes.TextAnalyzer:
                if IClassifyText.implementBy(obj):
                    result.append(obj)
        return result
