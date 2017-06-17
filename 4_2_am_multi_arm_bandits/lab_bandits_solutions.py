"Solution"

import math
import random

import numpy as np
import scipy.stats as stats


def random_choice(self):
    "Pick a bandit uniformly at random."
    return np.random.randint(0, len(self.wins)) # Return the index of the winning bandit.

def epsilon_greedy(self, epsilon=0.1):
    '''
    Pick a bandit uniformly at random epsilon percent of the time.
    Otherwise pick the bandit with the best observed proportion of winning.
    Return the index of the winning bandit.
    '''
    # test epsilon to decide
    if random.random() <= epsilon:
        # return a random choice
        return np.random.randint(0, len(self.wins))
    else:
        # return the current best choice
        return np.argmax(self.wins / (self.trials + 1))

def softmax(self, tau=0.01):
    '''
    Pick an bandit according to the Boltzman Distribution.
    Return the index of the winning bandit.
    '''

    # make sure to play each bandit at least once
    if len(self.trials.nonzero()[0]) < len(self.bandits):
        return np.random.randint(0, len(self.bandits))

    # compute the terms of the softmax function
    numerators = np.zeros(len(self.wins))
    denom = 0
    for i in xrange(len(self.wins)):
        numerators[i] = math.exp((self.wins[i] / (self.trials[i]+1.)) / tau)
        denom += numerators[i]

    # compute the "pmf" of the bandits
    last = 0
    softmax_vals = np.zeros(len(self.wins))
    for i in xrange(len(self.wins)):
        softmax_vals[i] = last + (numerators[i] / denom)
        last = softmax_vals[i]

    # pick a random number and see where it falls in the range
    r = random.random()
    for i in xrange(len(self.wins)):
        if r <= softmax_vals[i]:
            return i

def ucb1(self):
    '''
    Pick the bandit according to the UCB1 strategy.
    Return the index of the winning bandit.
    '''

    # make sure to play each bandit at least once
    if len(self.trials.nonzero()[0]) < len(self.bandits):
        return np.random.randint(0, len(self.bandits))

    # compute the UCB1 values for each bandit
    ucb1_vals = np.zeros(len(self.wins))
    for i in xrange(len(self.wins)):
        ucb1_vals[i] = (self.wins[i] / (self.trials[i]+1.)) + math.sqrt(
            2.*math.log(self.N) / self.trials[i]
        )

    # return the max
    return np.argmax(ucb1_vals)

def bayesian_bandit(self):
    '''
    Randomly sample from a beta distribution for each bandit and pick the one
    with the largest value.
    Return the index of the winning bandit.
    '''

    # make sure to play each bandit at least once
    if len(self.trials.nonzero()[0]) < len(self.bandits):
        return np.random.randint(0, len(self.bandits))

    # create a beta distribution for each bandit and draw a random sample
    samples = np.zeros(len(self.wins))
    for i in xrange(len(self.wins)):
        samples[i] = stats.beta(self.wins[i]+1, (self.trials[i]-self.wins[i]+1)).rvs(1)

    return np.argmax(samples)