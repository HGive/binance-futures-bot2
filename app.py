import os
from dotenv import load_dotenv
import ccxt
import pandas as pd
import logging
from pytz import timezone
from datetime import datetime
import time
import comm
from module_rsi import calc_rsi
# from module_ema import calc_ema

#로깅 설정
def timetz(*args):
    return datetime.now(tz).timetuple()
tz = timezone('Asia/Seoul') # UTC, Asia/Shanghai, Europe/Berlin
logging.Formatter.converter = timetz
logging.basicConfig(
    filename='bot2.log',
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
# logging.info('Timezone: ' + str(tz))


#바이낸스 객체 생성
load_dotenv() 
api_key = os.environ['BINANCE_API_KEY']
api_secret = os.environ['BINANCE_API_SECRET']
exchange = ccxt.binance(config = {
    'apiKey' : api_key,
    'secret' : api_secret,
    'enableRateLimit' : True,
    'options' : {
        'defaultType' : 'future'
    }
})

#타겟 심볼
symbol = 'CHR/USDT:USDT'

#가격 소숫점 자릿수 제한 설정
exchange.load_markets()
price_precision = exchange.markets[symbol]['precision']['price']
amount_precision = exchange.markets[symbol]['precision']['amount']
# min_cost = exchange.markets[symbol]['limits']['cost']['min']
pending_buy_order_id = None
pending_tp_order_id = None
interval = 20   # interval 초마다 반복
leverage = 10
init_delay_count = 0
buy_count = 0
timeframe = '5m'

#코드 시작하면 먼저 주문 모두 취소
exchange.cancel_all_orders(symbol=symbol)
#해당 타겟의 레버리지 설정
exchange.set_leverage(leverage, symbol)
#해당 타겟 모드 격리로 설정
exchange.set_margin_mode('isolated', symbol)

logging.info("***************   Bot has started!! ***************")

def main() :

    while True:
        print()
        


if __name__ == "__main__":
    main()