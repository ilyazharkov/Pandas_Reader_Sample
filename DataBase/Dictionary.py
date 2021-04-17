from enum import Enum
class enLanguage(Enum):
    English = 'EN'
    Russian = 'RU'
    All     = '**'
class enWordType(Enum):
    Noun = 'N'
    All  = 'A'
class WordDictionary:
    def __init__(self, language: enLanguage = enLanguage.All):
        self.language = language
    def words_query(self, wType: enWordType = enWordType.All):
        