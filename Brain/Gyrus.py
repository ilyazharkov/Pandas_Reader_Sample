import zope.interface
class IClassifyText(zope.interface.Interface):
    def ClassifyText(self, inputText):
        return "Any Text"
class GyrusBase(object):
    def __init__(self):
        self.Name = 'Base'

    def doTeaching(self):
        pass
class GyrusTextAnalizier(GyrusBase):
    zope.interface.implements(IClassifyText)
