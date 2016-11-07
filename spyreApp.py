# -*- coding: utf-8 -*-

from spyre import server

import pandas as pd
from urllib.request import urlopen
import json
import matplotlib.pyplot as plt

class StockExample(server.App):
    title = "Historical Stock Prices"

    inputs = [{ "type":"text",
                "key":"words",
                "label": "Enter a Stock Ticker:",
                "value":"COST",
                "action_id":"update_data"},
                { "type":"dropdown",
                "key":"span",
                "options":[{"label": "1 Month", "value":"1m"},
                           {"label": "3 Months", "value":"3m"},
                           {"label": "6 Months", "value":"6m"},
                           {"label": "1 Year", "value":"1y"},
                           {"label": "3 Years", "value":"3y"},
                           {"label": "5 Years", "value":"5y"}],
                "label": "Enter a Time Span:",
                "action_id":"update_data"}]

    controls = [{   "type" : "button",
                     "label":"get stock data",
                    "id" : "update_data"}]

    tabs = ["Plot","Table"]
                    
    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab":"Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab":"Table",
                    "sortable":"True"}]

    def getData(self, params):
        ticker = params['words']
        # make call to yahoo finance api to get historical stock data
        api_url = 'https://chartapi.finance.yahoo.com/instrument/1.0/{}/chartdata;type=quote;range=%s/json'.format(ticker) % params['span']
        result = urlopen(api_url).read()
        data = json.loads(result.replace(b'finance_charts_json_callback( ',b'')[:-1].decode('utf-8'))  # strip away the javascript and load json
        self.company_name = data['meta']['Company-Name']
        df = pd.DataFrame.from_records(data['series'])
        df['Date'] = pd.to_datetime(df['Date'],format='%Y%m%d')
        return df.drop('volume',axis=1)
    
    def getPlot(self, params):
        df = self.getData(params)
        fig = plt.figure(figsize=(16,12))
        with plt.style.context('fivethirtyeight'):
            plt.plot(df.Date, df.close, label='close') 
            plt.plot(df.Date, df.open, label='open') 
            plt.plot(df.Date, df.high, label='high') 
            plt.plot(df.Date, df.low, label='low') 
        plt.legend()
        return fig
    
app = StockExample()
app.launch()