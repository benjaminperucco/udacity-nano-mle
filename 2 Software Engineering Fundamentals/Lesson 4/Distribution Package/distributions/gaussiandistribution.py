import math
import matplotlib.pyplot as plt
from .generaldistribution import Distribution

class Gaussian(Distribution):
    """
    Generic distributions class for calculating and visualizing a probability
    distributions.

    Attributes:
        mean (float): Representing the mean value of the distributions
        stdev (float): Representing the standard deviation of the distributions
        data_list (list of floats): A list of floats extracted from the
        datafile
    """
    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        """
        Function to calculate the mean of the data set.

        Args:
            self (class Gaussian): Reference to itself

        Returns:
            float: Mean of the data set
        """
        avg = 1.0 * sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample=True):
        """
        Function to calculate the standard deviation of the data set.

        Args:
            self (class Gaussian): Reference to itself
            sample (bool): Whether the data represents a sample or population

        Returns:
            float: Standard deviation of the data set
        """
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean
        sigma = 0

        for d in self.data:
            sigma += (d - mean) ** 2

        sigma = math.sqrt(sigma / n)
        self.stdev = sigma
        return self.stdev

    def read_data_file(self, file_name, sample=True):
        """
        Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data
        attribute. After reading in the file, the mean and standard deviation
        are calculated

        Args:
            self (class Gaussian): Reference to itself
            file_name (str): Name of a file to read from
            sample (bol): Whether the data represents a sample or population

        Returns:
            None
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()

        file.close()
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """
        Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            self (class Gaussian): Reference to itself

        Returns:
            None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distributions.

        Args:
            self (class Gaussian): Reference to itself
            x (float): point for calculating the probability density function

        Returns:
            float: probability density function output
        """
        mu = self.mean
        sigma = self.stdev

        pdf = 1.0 / (sigma * math.sqrt(2 * math.pi)) \
              * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
        return pdf

    def plot_histogram_pdf(self, n_spaces=50):
        """
        Function to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            self (class Gaussian): Reference to itself
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
        """
        min_range = min(self.data)
        max_range = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed histogram of data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title(
            'Normal distributions for\n'
            + 'sample mean and sample standard deviation'
        )

        axes[0].set_ylabel('Density')
        plt.show()
        return x, y

    def __add__(self, other):
        """Function to add together two Gaussian distributions

        Args:
            self (class Gaussian): Reference to itself
            other (class Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distributions

        """
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result

    def __repr__(self):
        """
        Function to output the characteristics of the Gaussian instance

        Args:
            self (class Gaussian): Reference to itself

        Returns:
            string: characteristics of the Gaussian
        """
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)
