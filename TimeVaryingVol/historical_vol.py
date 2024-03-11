import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_histogram_with_grouping(returns, xlab, plot_title):
    # Calculate mean and standard deviation of returns
    mu = np.mean(returns)
    sigma = np.std(returns)
    min_return, max_return = np.min(returns), np.max(returns)
    tail_distance = 3  # no. std devs beyond which it's considered tail of distribution
    num_bins = int(np.power(len(returns), 1/2))

    bins = np.linspace(mu - tail_distance*sigma, mu + tail_distance*sigma, num_bins)
    if min_return < bins[0]:
        bins = np.insert(bins, 0, min_return)
    if max_return > bins[-1]:
        bins = np.append(bins, max_return)

    # Create histogram
    counts, _, _ = plt.hist(returns, bins=bins, edgecolor='black')
    plt.xlim(mu - (tail_distance + 0.3)*sigma,
             mu + (tail_distance + 0.3)*sigma)
 
    # Add x-ticks for the first and last bins
    first_bin_label = f'x<={bins[1]:.2f}'
    last_bin_label = f'x>={bins[-2]:.2f}'
    skip_len = 5 
    other_labels = [f"{bins[i]:.2f}" for i in range(1+skip_len, len(bins) - 2 - skip_len, skip_len)]
    all_labels = [first_bin_label] + other_labels + [last_bin_label]
    plt.xticks(np.concatenate(([bins[1]], bins[1+skip_len:-2-skip_len:skip_len], [bins[-2]])),
               all_labels,
               rotation=0)

    plt.axvline(x=mu + 3 * sigma, color='red', linestyle='dashed', linewidth=2)
    plt.text(mu + 3 * sigma, max(counts), r'$3\sigma$', rotation=90, verticalalignment='top')

    plt.axvline(x=mu - 3 * sigma, color='red', linestyle='dashed', linewidth=2)
    plt.text(mu - 3 * sigma, max(counts), r'-$3\sigma$', rotation=90, verticalalignment='top')

    plt.axvline(x=mu, color='red', linestyle='dashed', linewidth=2)
    plt.text(mu, max(counts), r'mu', rotation=90, verticalalignment='top')

    # Add labels and title
    plt.xlabel(xlab)
    plt.ylabel('Frequency')
    plt.title(plot_title)

    plt.gca().xaxis.grid(True)  # Add grid for better visualization

    # Show plot
    plt.show()


df = pd.read_csv("../data/Monthly_3_FamaFrench_Factors.csv")
mkt_excess = df.iloc[:,1].values
rf = df.iloc[:,4].values

mkt_rate_of_return = mkt_excess + rf
mkt_return_relative = 1 + (mkt_rate_of_return)/100
log_returns = np.log(mkt_return_relative)

print(np.sqrt(12)*np.std(log_returns))

start_yyyymm = str(df.iloc[0,0])
end_yyyymm = str(df.iloc[-1, 0])
plot_title = f"US Stocks Monthly {start_yyyymm[-2:]}/{start_yyyymm[:-2]}-{end_yyyymm[-2:]}/{end_yyyymm[:-2]} ({len(df)} observations)"
plot_histogram_with_grouping(log_returns, "Log Returns", plot_title)
plot_histogram_with_grouping(mkt_rate_of_return, "Rate of Return (%)", plot_title)

