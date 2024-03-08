# solutions.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters

def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    "*** YOUR CODE HERE ***"
    
    total_value = self.total()

    if total_value != 0:
        for key in self.keys():
            self[key] /= total_value

def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"

    random_value = random.random() # Generates a random float between 0 and 1
    cumulative_probability = 0 # Tracks cumulative probability as keys are iterated through
    for key, value in self.items():
        cumulative_probability += value # Add keys probability to the cumulative probability
        if random_value <= cumulative_probability: 
            return key   # Returns the key where the cumulative probability first becomes greater than or equal to the random value
    """
    Keys with higher weights have a greater chance of being selected.
    In the example (shell?) shown above denoted by the >>>'s, 100 000 samples are generated using 'dist'
    round(samples.count('key') * 1.0/N, 1) counts how many times 'key' appears in the samples
        Then divides it by the total number of samples, showing it to one decimal place
        The distribution 'dist' above is supposed to be normalized
    For example, if the random value is 0.6, key 'b' will be returned, as 0.2 + 0.4 = 0.6
        If random_value = 0.8, key 'c' will be returned
        'd' will never be returned.
    """
        

def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    """
    "*** YOUR CODE HERE ***"
    # Special case: ghost is in jail
    if ghostPosition == jailPosition:
        return 1.0 if noisyDistance is None else 0.0

    # Calculates True Distance
    trueDistance = util.manhattanDistance(pacmanPosition, ghostPosition)

    # Use the provided observation probability function
    if noisyDistance is not None:
        observationProbability = busters.getObservationProbability(noisyDistance, trueDistance)
        return observationProbability
    else:
        return 0.0



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    "*** YOUR CODE HERE ***"
    raiseNotDefined()
    self.beliefs.normalize()


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    "*** YOUR CODE HERE ***"
    raiseNotDefined()