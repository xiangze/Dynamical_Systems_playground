import numpy as np
import math
import matplotlib.pyplot as plt

#定義域全体に対して線形補間関数マップを適用し、その結果をリストとして返す
def fmap1(f:list,eps=0.):
    return [ int((1-eps)*f[f[i]]+eps*f[i]) for i in range(len(f))]

#fmap1をn回繰り返す
def fmap(f:list,n=1,eps=0.):
    for i in range(n):
        f=fmap1(f,eps)
    return f


#plot用関数
## 複数ステップの関数グラフを重ね書き
def plots(f,eps=.3,step=100,size=(15,15),overwrite=True):
    plt.figure(figsize=size)
    ff=f
    for i in range(step):
        if(overwrite or i==step-1):
            plt.plot(ff,"o")
        ff=fmap1(ff,eps)
    plt.show()

##sample分だけ幅Nから間引いて時系列をプロットする
def sampleplot(f,N=1000,eps=0., step=1000,samplenum=20):
    ff=f
    fs=[[] for  i in range(samplenum)]
    for i in range(step):
        ff=fmap1(ff,.3)
        for j in range(samplenum):
            fs[j].append(ff[j*(N//samplenum)])
    
    plt.figure(figsize=(15,10))   
    for j in range(samplenum):
        plt.plot(fs[j])
    plt.show()
    
#初期関数
sinramdam0=lambda N:[min(N-1,i+int(300*math.sin(i/(N/20)))) for i in range(N)]

NagumoSato=lambda k,omega,N=1000:[int((k*x+omega)%N) for x in range(N)]


def emb_NagumoSato(eps=.3,k=1.2,w=0.4,N=1000):
    a=(1-w)/(1-eps)
    b=1-w
    assert(a<1)
    
    x0=int(N*b)
    x1=int(N*a)
    f00=[N*( 1-2/b*abs(x/N-b/2)) for x in range(x0)]
    f01=[N-1 for x in range(x0,x1)]
    f02=[0 for x in range(x1,N)]
    return [ min(int(x),N-1) for x in f00+f01+f02]


##行列積としての関数マップ
def matrix_fmap(f:np.array,W:np.array , eps=0.):
    =(W@f).transpose()
    

def attention(q:np.array,Wq:np.array, k:np.array, Wk,eps=0.):
    =(W@f).transpose()

    
init