"""test_fft"""
import numpy as np
import matplotlib.pyplot as plt

# データのパラメータ
N = 1024            # サンプル数
DT = 0.01          # サンプリング間隔（サンプリング周波数は1.0/DT）
f1, f2 =10, 45    # サンプル信号の周波数（ナイキスト周波数=サンプリング周波数の1/2より大きな周波数成分を含んでいないこと）
t = np.arange(0, N*DT, DT) # 時間軸
freq = np.linspace(0, 1.0/DT, N) # 周波数軸

# サンプル信号を生成（周波数f1の正弦波+周波数f2の正弦波+ランダムノイズ）
f = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + 0.3 * np.random.randn(N)
# f = 2.0 + 0.3 * np.random.randn(N)

# 高速フーリエ変換
F = np.fft.fft(f)

# 振幅スペクトルを計算
Amp = np.abs(F)

# 振幅を元に信号に揃える（必要なければコメントにする）
#Amp = Amp / N * 2 # 交流成分はデータ数で割って2倍する
#Amp[0] = Amp[0] / 2 # 直流成分は2倍不要

# グラフ表示
fig = plt.figure(figsize=(13.66, 7.68), dpi=100)
# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.family'] = 'MS Gothic'
plt.rcParams['font.family'] = 'BIZ UDGothic'
plt.rcParams['font.size'] = 10

plt.subplot(211)
plt.plot(t, f, label=r'$f_n$')
plt.xlabel("時間", fontsize=10)
plt.ylabel("信号", fontsize=10)
plt.grid()
leg = plt.legend(loc=1, fontsize=10)
leg.get_frame().set_alpha(1)

plt.subplot(212)
plt.plot(freq[:int(N/2)+1], Amp[:int(N/2)+1], label=r'$|F_k|$') # ナイキスト周波数まで表示
plt.xlabel("周波数", fontsize=10)
plt.ylabel("振幅スペクトル", fontsize=10)
plt.grid()
leg = plt.legend(loc=1, fontsize=10)
leg.get_frame().set_alpha(1)

plt.show()

fig.savefig("test_FFT.png", bbox_inches="tight", pad_inches=0.05)
