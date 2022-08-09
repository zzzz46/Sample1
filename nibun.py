a = -1  #探索範囲の指定(小)
b = 2  #探索範囲の指定（大）
c = 1e-4  #誤差範囲の指定
d = 140  #試行回数の指定

import numpy as np  #数値計算用モジュール
import matplotlib.pyplot as plt  #データ可視化用モジュール


def func_f(x):
    return x**2.0 - 1.0


def bisection(func_f, x_min, x_max, error=c, max_loop=d):
    #初期値を表示
    num_calc = 0  #計算回数
    print("{:3d}:  {:.15f} <= x <= {:.15f}".format(num_calc, x_min, x_max))
    #中間値の定理の条件を満たすか調べる
    if (0.0 < func_f(x_min) * func_f(x_max)):
        print(
            "error: Section definition is invalid (0.0 < func_f(x_min)*func_f(x_max))."
        )
        quit()

#ずっと繰り返す
    while (True):
        #新たな中間値の計算
        x_mid = (x_max + x_min) / 2.0

        #探索区間を更新
        if (0.0 < func_f(x_mid) * func_f(x_max)):  #中間と右端の値が同じの時
            x_max = x_mid  #右端を更新
        else:  #中間と左端の値が同じの時
            x_min = x_mid  #左端を更新

        #結果を表示
        num_calc += 1  #計算回数を数える
        print("{:3d}:  {:.15f} <= x <= {:.15f}".format(num_calc, x_min, x_max))

        #「誤差範囲が一定値以下」または「計算回数が一定値以上」ならば終了
        if ((x_max - x_min <= error) or max_loop <= num_calc):
            break

    #最終的に得られた解
    print("x = {:.15f}".format(x_mid))

    return x_mid


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
    plt.text(
        a,
        0.0,
        "a",
    )
    plt.text(
        b,
        0.0,
        "b",
    )
    plt.text(x_solved,
             0.0,
             "$x$ = {:.9f}".format(x_solved),
             va='bottom',
             color='#0000ff')
    plt.show()  #グラフを表示


#メイン実行部
if (__name__ == '__main__'):
    #二分法で非線型方程式の解を計算
    solution = bisection(func_f, a, b)

    #結果を可視化
    visualization(func_f, solution - 1.0, solution + 1.0, solution)
