import matplotlib.pyplot as plt
import numpy

k_b = 1.38E-16
n_h = 1.0
lambda_0 = 10E-22
t_0 = 20000
alpha = 10
beta = -0.5
temp_list = [1E7]
time_list = [5E8]


def Lambda(y_n):

    if y_n <= t_0:
        return lambda_0*((y_n/t_0)**alpha)
    else:
        return lambda_0*((y_n/t_0)**beta)


def k_1(y_n):
    return (-2/(3*k_b))*n_h*Lambda(y_n)


def k_2(delta_t, y_n):
    return (-2/(3*k_b))*n_h*Lambda(y_n+k_1(y_n)*delta_t)


def yn_plus_one(y_n, delta_t):
    return y_n+((1/2)*(k_1(y_n)+k_2(delta_t, y_n))*delta_t)

def adaptive_stop():


if __name__ == "__main__":
    y_n = temp_list[-1]
    starting_temp = 10E10
    time_list.append(starting_temp)
    delta_t = time_list[0]
    i = 1
    while y_n > 6000:
        temp_list.append(yn_plus_one(y_n, delta_t))
        y_n = temp_list[-1]
        i = i + 1
        time_list.append(delta_t*i)
    plt.plot(time_list, temp_list)
    plt.yscale('log')
    plt.show()

