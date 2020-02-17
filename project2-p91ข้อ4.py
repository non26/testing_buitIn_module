As=float(input('Enter amount invested in SPY: '))
Aq=float(input('Enter amount invested in QQQ: '))
Ae=float(input('Enter amount invested in EEM: '))
Av=float(input('Enter amount invested in VXX: '))
sum1=As+Aq+Ae+Av
Ps=(As*100)/sum1
Pq=(Aq*100)/sum1
Pe=(Ae*100)/sum1
Pv=(Av*100)/sum1
print('ETF\tPERCENTAGE'.expandtabs(5))
print('SPY{0:11.2f}%'.format(Ps))
print('QQQ{0:11.2f}%'.format(Pq))
print('EEM{0:11.2f}%'.format(Pe))
print('VXX{0:11.2f}%'.format(Pv))
