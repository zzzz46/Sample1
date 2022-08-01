a = 1  #探索開始地点の指定
b = 0.001  #誤差範囲の指定
c = 100  #試行回数の指定

import numpy as np  #NumPyライブラリ
import matplotlib.pyplot as plt  #データ可視化ライブラリ


#解きたい方程式
def func_f(x):
    return x**2.0 - 1.0


#Newton法（方程式の関数項、探索の開始点、微小量、誤差範囲、最大反復回数）
def newton(func_f, x0, eps=1e-10, error=b, max_loop=c):
    num_calc = 0  #計算回数
    print("{:3d}:  x = {:.15f}".format(num_calc, x0))

    #ずっと繰り返す
    while (True):
        #中心差分による微分値
        func_df = (func_f(x0 + eps) - func_f(x0 - eps)) / (2 * eps)
        if (abs(func_df) <= eps):  #傾きが0に近ければ止める
            print("error: abs(func_df) is too small (<=", eps, ").")
            quit()

        #次の解を計算
        x1 = x0 - func_f(x0) / func_df

        num_calc += 1  #計算回数を数える
        print("{:3d}:  x = {:.15f}".format(num_calc, x0))

        #「誤差範囲が一定値以下」または「計算回数が一定値以上」ならば終了
        if (abs(x1 - x0) <= error or max_loop <= num_calc):
            break

        #解を更新
        x0 = x1

    #最終的に得られた解
    print("x = {:.15f}".format(x0))

    return x0


#可視化（方程式の関数項、グラフ左端、グラフ右端、方程式の解）
def visualization(func_f, x_min, x_max, x_solved):
    plt.xlabel("$x$")  #x軸の名前
    plt.ylabel("$f(x)$")  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.axhline(0, color='#000000')  #f(x)=0の線

    #関数
    exact_x = np.arange(x_min, x_max, (x_max - x_min) / 500.0)
    exact_y = func_f(exact_x)

    plt.plot(exact_x, exact_y, label="$f(x)$", color='#ff0000')  #関数を折線グラフで表示
    plt.scatter(x_solved, 0.0)  #数値解を点グラフで表示
    plt.text(x_solved, 0.5, 'y=x^2.0 - 1.0')
    plt.text(x_solved,
             0.0,
             "$x$ = {:.9f}".format(x_solved),
             va='bottom',
             color='#0000ff')
    plt.show()  #グラフを表示


#メイン実行部
if (__name__ == '__main__'):
    #Newton法で非線型方程式の解を計算
    solution = newton(func_f, a)

    #結果を可視化
    visualization(func_f, solution - 1.0, solution + 1.0, solution)
