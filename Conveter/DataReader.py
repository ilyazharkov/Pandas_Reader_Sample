import pandas as pd
import datetime as dt
import numpy
from pandas_datareader import data


class RequestContainer:
    def __init__(self, datasource, date_from, date_to, company):
        self.datasource = datasource
        self.date_from = date_from
        self.date_to = date_to
        self.company = company


def GetFactory(args: RequestContainer):
    return ConverterFactory(args)


class ConverterFactory:
    def __init__(self, args: RequestContainer):
        self.args = args
        expected_source = [
            "yahoo",
            "iex",
            "iex-tops",
            "iex-last",
            "iex-last",
            "bankofcanada",
            "stooq",
            "iex-book",
            "enigma",
            "fred",
            "famafrench",
            "oecd",
            "eurostat",
            "nasdaq",
            "quandl",
            "moex",
            "tiingo",
            "yahoo-actions",
            "yahoo-dividends",
            "av-forex",
            "av-forex-daily",
            "av-daily",
            "av-daily-adjusted",
            "av-weekly",
            "av-weekly-adjusted",
            "av-monthly",
            "av-monthly-adjusted",
            "av-intraday",
            "econdb",
            "naver",
        ]

    def get_handler(self):
        data_source = self.args.datasource
        if data_source == "moex":
            return MoexDatasource(self.args)
        elif data_source == "yahoo":
            return YahooDatasource(self.args)
        elif data_source == "iex":
            return IexDatasource(self.args)
        elif data_source == "iex-tops":
            return IextDatasource(self.args)
        elif data_source == "iex-last":
            return IexlDatasource(self.args)
        elif data_source == "bankofcanada":
            return BocDatasource(self.args)


class BaseDatasource:
    def __init__(self, args: RequestContainer):
        self.args = args

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass

    @staticmethod
    def Create_Empty():
        index = numpy.dtype([('date', dt.datetime)])
        columns = numpy.dtype([
            ('company', str),
            ('close_price', float),
            ('open_price', float)
        ])
        empty_data = numpy.empty(0, dtype=columns)
        df = pd.DataFrame(index=index, columns=columns)
        return df

    def DoRequest(self):
        request_data = data.DataReader(self.args.company,
                                       start=self.args.date_from,
                                       end=self.args.date_to,
                                       data_source=self.args.datasource
                                       )
        return self.Convert_Data(request_data)

    def Convert_Data(self, input_data: pd.DataFrame):
        return self.Convert_Lines(input_data)


class MoexDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        # output.index = input_data.index
        output = input_data.query('BOARDID == "TQBR"', inplace=False)[['SECID', 'CLOSE', 'WAPRICE']].copy()
        output.index.rename('Date', inplace=True)
        output.rename(columns={'SECID': 'Company',
                               'CLOSE': 'Close_Price',
                               'WAPRICE': 'Open_Price'}
                      , inplace=True)
        return output


class YahooDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        output = input_data[['Open', 'Close']].copy()
        output.rename(columns={'Close': 'Close_Price',
                               'Open': 'Open_Price'}
                      , inplace=True)
        output['Company'] = self.args.company
        return output


class IexDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass


class IextDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass


class IexlDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass

class BocDatasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass
class MQL5Datasource(BaseDatasource):
    def __init__(self, args: RequestContainer):
        BaseDatasource.__init__(self, args)

    def Convert_Lines(self, input_data: pd.DataFrame):
        pass
