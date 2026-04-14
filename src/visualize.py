import matplotlib.pyplot as plt

def plot_results(predictions):
    plt.hist(predictions)
    plt.title("Threat Detection Distribution")
    plt.show()