import datetime as dt
import matplotlib.pyplot as plt
import yfinance as yf

#moving averages
ma1=30
ma2=100

start=dt.datetime.now()-dt.timedelta(days=365*3)
end=dt.datetime.now()

df=yf.download('RITES.NS',start,end)
df[f'SMA_{ma1}']=df['Close'].rolling(window=ma1).mean()
df[f'SMA_{ma2}']=df['Close'].rolling(window=ma2).mean()

df=df.iloc[ma2:]


buy_signal=[]
sell_signal=[]
trigger=0

for i in range(len(df)):
    if df[f'SMA_{ma2}'].iloc[i]>df[f'SMA_{ma1}'].iloc[i] and trigger!=1:
        buy_signal.append(df['Close'].iloc[i])
        sell_signal.append(float('nan'))
        trigger=1
    elif df[f'SMA_{ma2}'].iloc[i]<df[f'SMA_{ma1}'].iloc[i] and trigger!=-1:
        sell_signal.append(df['Close'].iloc[i])
        buy_signal.append(float('nan'))
        trigger=-1
    else:
        sell_signal.append(float('nan'))
        buy_signal.append(float('nan'))


df['Buy_Signals']=buy_signal
df['Sell_Signals']=sell_signal

plt.plot(df['Close'],label='Share Price',alpha=0.5)
plt.plot(df[f'SMA_{ma1}'],label=f'SMA_{ma1}',color='orange',linestyle='--')
plt.plot(df[f'SMA_{ma2}'],label=f'SMA_{ma2}',color='pink',linestyle='--')
plt.scatter(df.index,df['Buy_Signals'],label='BuySignal',marker='^',color='green')
plt.scatter(df.index,df['Sell_Signals'],label='SellSignal',marker='<',color='red')
plt.legend(loc='upper left')
plt.show()

