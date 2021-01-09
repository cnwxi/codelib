# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots()
# text = ax.text(0.5, 0.5, 'event', ha='center', va='center', fontdict={'size': 20})
#
# click = False
#
#
# def call_back1(event):
#     global click
#     info = '1'
#     text.set_text(info)
#     fig.canvas.draw_idle()
#     click = True
#
#
# def call_back(event):
#     if click:
#         info = '0'
#         text.set_text(info)
#         fig.canvas.draw_idle()
#
#
# def call_back2(event):
#     global click
#     info = '2'
#     text.set_text(info)
#     fig.canvas.draw_idle()
#     click = False
#
#
# def get_w(event):
#     if event.key == 'w':
#         print('w')
#
#
# fig.canvas.mpl_connect('button_press_event', call_back1)
# fig.canvas.mpl_connect('button_release_event', call_back2)
# fig.canvas.mpl_connect('motion_notify_event', call_back)
# fig.canvas.mpl_connect('key_press_event', get_w)
#
# plt.show()
#
# import numpy as np
#
# a = np.array([[1, 0, 0], [0, 0.5, 0], [0, 0, 1]])
# b = [2, 1, 1]
# aa = np.dot(b, a)
# # aa.dtype = 'int'
# print(aa)

# x0 = 20
# y0 = 0
# t = np.array([[np.cos(np.pi / 2), np.sin(np.pi / 2), 0],
#               [-np.sin(np.pi / 2), np.cos(np.pi / 2), 0],
#               [x0 * (1 - np.cos(np.pi / 2)) + y0 * np.sin(np.pi / 2),
#                y0 * (1 - np.cos(np.pi / 2)) + x0 * np.sin(np.pi / 2), 1]])
#
# a = np.array([20, 20, 1])
# print('len1', (a[0] - x0) ** 2 + (a[1] - y0) ** 2)
# # a = np.dot(a, t)[:2]
# # print('len2', (a[0] - x0) ** 2 + (a[1] - y0) ** 2)
# a[0] = x0 + (a[0] - x0) * np.cos(np.pi / 2) - (a[1] - y0) * np.sin(np.pi / 2)
# a[1] = y0 + (a[0] - x0) * np.sin(np.pi / 2) + (a[1] - y0) * np.cos(np.pi / 2)
# print('len3', (a[0] - x0) ** 2 + (a[1] - y0) ** 2)
# print(a.astype('int32'))
import numpy as np
import math

a = np.array([20, 20, 1])
x0, y0 = 20, 0
cos = math.cos(math.pi / 2)
sin = math.sin(math.pi / 2)

tmpx = x0 + (a[0] - x0) * cos - (a[1] - y0) * sin
tmpy = y0 + (a[0] - x0) * sin + (a[1] - y0) * cos
print(tmpx, int(tmpy))

t = np.array([[cos, sin, 0],
              [-sin, cos, 0],
              [x0 * (1 - cos) + y0 * sin, y0 * (1 - cos) - x0 * sin, 1]])

tmpp = a.dot(t)
tmpp = tmpp.astype('int32')
print(tmpp)
