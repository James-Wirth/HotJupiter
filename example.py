from hjmodel import HJModel
import matplotlib.pyplot as plt

RES_PATH = '/Users/jameswirth/PycharmProjects/hotjupiter-multiprocess/data/'

if __name__ == '__main__':
    model = HJModel(res_path=RES_PATH, res_name='exp_data_new')
    model.run(time=12000, num_systems=1000000)

    # model.plot_outcomes()

    # outcome_probs = model.get_outcome_probabilities()
    # print(outcome_probs)

    # stats = model.get_statistics_for_outcome(['HJ'], 'r')
    # plt.hist(stats)
    # plt.show()
