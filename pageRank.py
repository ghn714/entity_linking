from numpy import *

def graphMove(a):  # 构造转移矩阵
    b = transpose(a)  # b为a的转置矩阵
    c = zeros(a.shape, dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = a[i][j] / (b[j].sum())  # 完成初始化分配
    print(c,"\n====================================================")
    return c

def firstPr(c):  # pr值得初始化
    pr = zeros((c.shape[0], 1), dtype=float)  # 构造一个存放pr值得矩阵
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
        #print(pr,"\n===================================================")
    return pr


def pagerank(p, M, U):  # 计算pageRank值
    U_past_has_alpha = []
    U0 = array(U)
    while True:
        U = p * dot(M, U) + (1-p) * U0
        # print('Un: ', U)
        if str(U) == str(U_past_has_alpha):
            break
        U_past_has_alpha = U
    return U


if __name__ == '__main__':
    # A->B有边 则 矩阵a[1][0]>0  跟常识是是反的
    a = array([[1, 1, 1, 1, 0],
               [0, 1, 0, 1, 1],
               [0, 0, 1, 0, 1],
               [0, 0, 0, 1, 1],
               [1, 0, 0, 0, 1]], dtype=float)  # dtype指定为float
    M = graphMove(a)
    pr = firstPr(M)
    p = 0.85  # 引入浏览当前网页的概率为p,假设p=0.8
    print(pagerank(p, M, pr))  # 计算pr值