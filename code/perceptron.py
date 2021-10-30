'''
'''
import numpy as np
import sklearn.datasets as skd
import matplotlib.pyplot as plt
# 定义感知机模型
class Perceptron():
    # 初始化向量机参数：学习率
    def __init__(self,l_rate=1.0):
        self.b = 0
        self.l_rate = l_rate

    # 线性计算函数
    def sign(self,x):
        return self.w.dot(x)+self.b
    # 拟合函数
    def fit(self,X,y):
        n_sample=len(y)
        self.w=np.zeros(X.shape[-1])
        is_wrong=True
        while is_wrong:
            wrong_count=0
            for i in range(n_sample):
                x=X[i]
                if (y[i]*self.sign(x))<=0:
                    self.w=self.w+self.l_rate*x*y[i]
                    self.b=self.b+self.l_rate*y[i]
                    wrong_count+=1
            if wrong_count==0:
                is_wrong=False
        return

if __name__=='__main__':
    iris=skd.load_iris()
    X=iris.data[:100,:2]
    y=iris.target[:100]
    y=np.array([1 if i==1 else -1 for i in y])

    model=Perceptron()
    model.fit(X,y)

    plt.scatter(X[:50,0],X[:50,1],label='setosa')
    plt.scatter(X[50:,0],X[50:,1],label='versicolor')

    x=np.arange(X[:,0].min(),X[:,0].max(),step=1.0)
    y=-(model.w[0]*x+model.b)/model.w[1]
    plt.plot(x,y,label='Perceptron')
    plt.legend()
    plt.show()



