import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize = (10, 6))

    plt.plot(time, voltage)
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")

    plt.xlim(min(time), max(time))
    plt.ylim(0, max_voltage)

    plt.grid(True)

    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = [time[i+1] - time[i] for i in range(len(time) - 1)]

    plt.title("Распределение периодов дискретизации измерений по времени на одно измерение")
    plt.figure(figsize = (10, 6))
    plt.hist(sampling_periods)
    plt.xlabel("Период измерений, с")
    plt.ylabel("Количество измерений, N")

    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show