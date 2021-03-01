import matplotlib.pyplot as plt
import seaborn as sns


# Box plot for all the features in dataset.
def box_plot(x):
    data_dia = x.iloc[:, :5]
    data_sys = x.iloc[:, 5:10]
    data_eda = x.iloc[:, 10:15]
    data_res = x.iloc[:, 15:20]
    sns.set_theme(style="whitegrid")
    # data_res.loc[data_res['Variance'] > 200, 'Variance'] = None
    ax = sns.boxplot(data=data_res, orient="h", palette="Set2")
    plt.title('Respiration Data')
    plt.show()


# Line graph for the dataset.
def line_plot(x):
    no_pain = x.iloc[:4, :]
    pain = x.iloc[4:8, :]
    x = list(range(63440))
    data = {'No Pain': no_pain, 'Pain': pain}
    for title, dataset in data.items():
        plt.plot(x, dataset.iloc[0, 3:], color='blue', label=dataset.iat[0, 1])
        plt.plot(x, dataset.iloc[2, 3:], color='green', label=dataset.iat[2, 1])
        plt.plot(x, dataset.iloc[3, 3:], color='black', label=dataset.iat[3, 1])
        plt.legend()
        plt.title(title)
        plt.show()

    for title, dataset in data.items():
        plt.plot(x, dataset.iloc[1, 3:], color='red', label=dataset.iat[1, 1])
        plt.legend()
        plt.title(title)
        plt.show()
