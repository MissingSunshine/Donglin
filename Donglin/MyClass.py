# import math
#
#
# # 油品类
#
#
# class Oil:
#     def __init__(self, p20, v20, Tn):
#         self.p20 = p20  # 20度时油品密度
#         self.v20 = v20  # 20度时油品黏度
#         self.Tn = Tn  # 油品凝点
#
#     def get_v(self, t):  # 计算黏度
#         v = self.v20 * math.exp(0.09 * (t - 20))
#         return v
#
#     def get_p(self, t):  # 计算密度
#         p = self.p20 - (1.825 - 0.0001315 * self.p20) * (t - 20)
#         return p
#
#     def get_c(self, t):  # 计算比热容
#         d15 = self.get_p(15) / 999.099
#         c = (1 / math.sqrt(d15)) * (1.687 + 3.39 * math.pow(10, -3))
#         return c
#
#
# class Pipe:
#     """管段类"""
#
#     def __init__(self, p0, TR, G, L, D, t, K, T0):
#         self.p0 = p0  # 起点压力
#         self.TR = TR  # 起点温度
#         self.L = L  # 管长
#         self.D = D  # 管外径
#         self.G = G  # 质量流量
#         self.t = t  # 壁厚
#         self.K = K  # 总传热系数
#         self.T0 = T0  # 地温
#
#     def get_Tx(self, c, L):  # 计算管道任意一点的温度
#         a = (self.K * math.pi * self.D / 1000) / (self.G * c * 1000)
#         Tx = self.T0 + (self.TR - self.T0) * math.exp(-a * L * 1000)
#         return Tx
#
#     def get_hx(self, v, p, L):  # 计算管道任一点的摩阻
#         Q = self.G / p
#         d = (self.D - 2 * self.t) / 1000
#         Re = 4 * Q / (math.pi * d * v)
#         e = 0.0002 / d
#         Re1 = 59.5 / math.pow(e, 8 / 7)
#         Re2 = (665 - 765 * math.log10(e)) / e
#
#         B = 0
#         m = 0
#         if Re <= 2000:
#             B = 4.15
#             m = 1
#         if 2000 < Re < Re1:
#             B = 0.0246
#             m = 0.25
#         if Re1 < Re < Re2:
#             B = 0.0802
#             m = 0.123
#         if Re > Re2:
#             B = 0.0826
#             m = 0
#         hx = B * math.pow(Q, 2 - m) * math.pow(v, m) * L * 1000 / math.pow(d, 5 - m)
#         return hx
#
#     def get_paras_distribution(self, p, v, c, x_list):  # 计算沿线水头、温度、压力
#         H_x = []
#         T_X = []
#         P_X = []
#         H0 = self.P0 * 10 ** 6 / (p * 9.81)
#         for x in x_list:
#             Tx + self.get_Tx(c, x)
#             T_x.append(Tx)
#             Hx = H0 – self.get_hx(v, p, x)[0]
#             H_x.append(Hx)
#             P_x.append(p * 9.81 * Hx * 10 ** -6)
#         m = self.get_hx(v, p, x)[1]
#         return H_x, T_x, P_x, m
#
#
# # 站场类
#
#
# class Station:  # 获取泵站扬程
#
#     def __int__(self, Q_in, A, B, m):
#         self.Q = Q_in
#         self.A = A
#         self.B = B
#         self.m = m
#
#     def add_head(self):
#         H = self.A - self.B * math.pow(self.Q, 2 - self.m)
#         return H
#
#
# def sinulate(Q_init, p_init, TR1, TR2, T0, K, A, B, oil):
#     """ 计算主函数 """
#     x_list1 = []  # 管段1的里程
#     G = Oil.get_p(TR1) * Q_init
#     pipe1 = Pipe(p_init, TR1, G, 95, 610, 6, K, T0)  # 创建东营站到滨州站的管道
#     for i in range(pipe1.L):
#         x_list1.append(i)
#     Td_cpv = (pipe1.TR + pipe1.T0) / 2  # 由此温度确定原油比热、密度和黏度
#     TL = pipe1.get_Tx(oil.get_c(Td_cpv), x_list1[-1])
#     H_x, T_x, P_x, n = pipe1.get_paras_distribution(oil.get_p(Td_cpv), oil.get_v(Td_cpv), oil.get_c(Td_cpv), x_list1)
#     Q = G / oil.get_p(TR2)
#     BZ = Station(Q, A, B, m)
#     H3 = H_x[-1] + BZ.add_head()
#     p3 = oil.get_p(TR2) * 9.81 * H3 * 10 ** -6
#     x_list2 = []
#     pipe2 = Pipe(p3, TR2, G, 60.5, 610, 6, K, T0)  # 创建滨州站到临邑站的管道
#     for I in range(pipe2, L):
#         x_list2.append(i)
#     Td_cpv2 = (pipe2.TR + pipe2.T0) / 2
#     TL = pipe2.get_Tx(oil.get_c(Td_cpv2), x_list2[-1])
#     H_x1, T_x1, P_x1, m1 = pipe2.get_paras_distribution(oil.get_p(Td - cpv2), oil.get_v(Td_cpv2), oil.get_c(Td_cpv2),
#                                                         x_list2)
#
#     x_list3 = [x + x_list1[-1] for x in x_list2]
#     x_list = x_list1 + x_list3
#     H_list = H_x + H_x1
#     T_list = T_x + T_x1
#     P_list = P_x + P_x1
#     return P_x[0], P_x[-1], H_x[0], H_x[-1], T_x[-1], p3, H3, P_x1[-1], H_x1[-1], T_x1[
#         -1], x_list, H_list, T_list, P_list


import requests

res = requests.post(
    'http://127.0.0.1:8000/donglin/register',
        data={
            "email": "123456@qq.com",
            "username": "user1",
            "password": "123456",
        })

print(res.status_code)
print(res.text)