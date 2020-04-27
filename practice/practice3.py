import yfinance as yf


class NVIDIA_TradingSystem(TradingSystem):

    def absractloop(self):
        print(self.nvda.option_chain())

    def __init__(self, timeframe):
        self.ticker = 'NVDA'
        self.nvda = yf.Ticker(self.ticker)
        super().__init__('NVDA', timeframe)
        
NVIDIA_TradingSystem(10)