import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp, wasserstein_distance

# Function to compute convergence metrics
def compute_convergence(data):
    realizations = np.arange(1, len(data) + 1)
    quantiles_1 = [np.percentile(data[:i], 1) for i in realizations]
    return realizations, quantiles_1

# Functions for convergence criteria
def check_relative_change(current, previous, threshold=1e-3):
    return abs(current - previous) / abs(previous) < threshold if previous != 0 else False

def compute_bootstrap_quantile(data, quantile, n_bootstrap=1000):
    bootstraps = [np.percentile(np.random.choice(data, size=len(data), replace=True), quantile) for _ in range(n_bootstrap)]
    return np.std(bootstraps)

def check_confidence_band(quantile_std, threshold):
    return quantile_std < threshold

def check_wasserstein_distance(data1, data2, threshold=1e-3):
    return wasserstein_distance(data1, data2) < threshold

def check_kolmogorov_smirnov(data1, data2, threshold=0.05):
    ks_stat, p_value = ks_2samp(data1, data2)
    return p_value > threshold

# Function to plot convergence with confidence intervals and criteria fulfillment
def plot_convergence(realizations, quantiles_1, data):
    # Compute confidence band (99% confidence interval via bootstrapping)
    bootstrap_errors = [compute_bootstrap_quantile(data[:i], 1) for i in realizations]
    lower_bound = np.array(quantiles_1) - 2.576 * np.array(bootstrap_errors)
    upper_bound = np.array(quantiles_1) + 2.576 * np.array(bootstrap_errors)

    # Compute convergence checks for each realization
    relative_changes = [check_relative_change(quantiles_1[i], quantiles_1[i-1]) if i > 0 else False for i in range(1, len(quantiles_1))]
    bootstrap_stabilities = [check_confidence_band(compute_bootstrap_quantile(data[:i], 1), threshold=1e-2) for i in realizations]
    
    # Ensure Wasserstein Distance and KS Test lists are correctly aligned with realizations[1:]
    wasserstein_distances = [check_wasserstein_distance(data[:i-1], data[1:i]) if i > 1 else False for i in realizations[1:]]
    ks_tests = [check_kolmogorov_smirnov(data[:i-1], data[1:i]) if i > 1 else False for i in realizations[1:]]

    plt.figure(figsize=(12, 8))

    # Plot for the 1% quantile
    plt.subplot(2, 1, 1)
    plt.plot(realizations, quantiles_1, label=f'1% Quantile: {quantiles_1[-1]:.3f}', color='red')
    plt.fill_between(realizations, lower_bound, upper_bound, color='red', alpha=0.2,
                     label=f'99% Confidence Interval: [{lower_bound[-1]:.3f}, {upper_bound[-1]:.3f}]')
    plt.title('Convergence of the 1% Quantile with Confidence Band', fontsize=14)
    plt.xlabel('Number of Realizations', fontsize=14)
    plt.ylabel('1% Quantile', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid()

    # Plot convergence criteria fulfillment
    plt.subplot(2, 1, 2)
    plt.plot(realizations[1:], relative_changes, 'o-', label="Relative Change < Threshold", color='blue')
    plt.plot(realizations, bootstrap_stabilities, 's-', label="Bootstrap Stability", color='green')
    plt.plot(realizations[1:], wasserstein_distances, 'd-', label="Wasserstein Distance < Threshold", color='purple')
    plt.plot(realizations[1:], ks_tests, 'x-', label="KS Test Passed", color='orange')

    plt.title('Convergence Criteria Fulfillment', fontsize=14)
    plt.xlabel('Number of Realizations', fontsize=14)
    plt.ylabel('Fulfillment (1 = Yes, 0 = No)', fontsize=14)
    plt.ylim(-0.1, 1.1)  # Keep values within logical bounds
    plt.legend(fontsize=12)
    plt.grid()

    plt.tight_layout()
    plt.show()

# Main program
if __name__ == "__main__":
    # Load data from file
    file_path = "Daten.txt"
    try:
        data = np.loadtxt(file_path)
        if data.ndim > 1:
            raise ValueError("The file should contain a one-dimensional data series.")
    except Exception as e:
        print(f"Error reading the file: {e}")
        exit(1)

    # Analyze convergence
    realizations, quantiles_1 = compute_convergence(data)

    # Compute final convergence checks
    metrics_results = {
        "Relative Change in the 1% Quantile": check_relative_change(quantiles_1[-1], quantiles_1[-2]) if len(quantiles_1) > 1 else False,
        "Bootstrap Confidence Band": check_confidence_band(compute_bootstrap_quantile(data, 1), threshold=1e-2),
        "Wasserstein Distance": check_wasserstein_distance(data[:-1], data[1:]),
        "Kolmogorov-Smirnov Test": check_kolmogorov_smirnov(data[:-1], data[1:]),
    }

    print("Convergence Checks:")
    for metric, result in metrics_results.items():
        print(f"{metric}: {'Satisfied' if result else 'Not Satisfied'}")

    # Plot results
    plot_convergence(realizations, quantiles_1, data)
