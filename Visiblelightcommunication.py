#coding:utf-8
import math
import matplotlib.pyplot as plt

#ピーク光度[lm/sr]
#peekcd=30000
peekcd=30
#srステラジアン
srdeg=10
#地上からの高度[km]
distance=300
#滅光係数
alpha=0.5

#E:照度[lx]
#等級が戻り値(一般に人の目で確認できる限界が6等級までと言われている)
def LEDMagnitude(peekcd,srdeg,distance):
    #地上照射面積[km**2]
    S=lambda distance,srdeg:(distance*math.tan(srdeg*math.pi/180))**2*math.pi
    phi=lambda peekcd,S,distance:peekcd*S/(distance**2)
    LEDmagnitude=lambda E:-(math.log10(E)/math.log10(10**(2.0/5)))-14
    return LEDmagnitude(phi(peekcd,S(distance,srdeg),distance)/(S(distance,srdeg)*10**6))

ledmag=[]
dis=[] 
for i in range(300,1500):
    dis.append(i)
    ledmag.append(LEDMagnitude(peekcd,srdeg,i))


def __Airmass(atom):
    sec = lambda x:1.0/math.cos(x)
    if(atom<60.0*math.pi/180):
        return sec(atom)
    else:
        return sec(atom) - 0.0018167 * (sec(atom)-1) - 0.002875 * (sec(atom)-1)**2 - 0.0008083 * (sec(atom)-1)**3
def AtomLoss(alpha,atom):
    return alpha * __Airmass(atom)

dataled1=[]
dataled2=[]
dataled3=[]
dataled4=[]
deg=[]

led1m=LEDMagnitude(peekcd,srdeg,distance)
led2m=LEDMagnitude(peekcd*5**2,srdeg,distance)
led3m=LEDMagnitude(peekcd*10**2,srdeg,distance)
led4m=LEDMagnitude(peekcd*15**2,srdeg,distance)

for i in range(0,87):
    deg.append(i)
    dataled1.append(led1m+AtomLoss(0.5,i*math.pi/180))
    dataled2.append(led2m+AtomLoss(0.5,i*math.pi/180))
    dataled3.append(led3m+AtomLoss(0.5,i*math.pi/180))
    dataled4.append(led4m+AtomLoss(0.5,i*math.pi/180))

#plt.plot(dis,ledmag)
plt.ylim(0,11)
plt.plot(deg,dataled1,deg,dataled2,deg,dataled3,deg,dataled4)
plt.show()
#elev=20*math.pi/180
#print 4.3+1.0/(math.cos(90-elev)+0.50572*(6.07995+elev)**-1.6364)
