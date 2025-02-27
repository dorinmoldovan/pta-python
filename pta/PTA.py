import random
import numpy

class PTA:
    def __init__(self, objf, lb, ub, dim, PopSize, iters, eps, FT, RT, FRmin, FRmax):
        self.objf = objf
        self.lb = lb
        self.ub = ub
        self.dim = dim
        self.PopSize = PopSize
        self.iters = iters
        self.eps = eps
        self.FT = FT
        self.RT = RT
        self.FRmin = FRmin
        self.FRmax = FRmax

        if not isinstance(lb, list):
            self.lb = [lb] * dim
        if not isinstance(ub, list):
            self.ub = [ub] * dim

        self.plums = numpy.zeros((self.PopSize, self.dim))

        self.flowerScore = numpy.zeros(self.PopSize)
        self.flowerScore.fill(float("inf"))

        self.plumScore = numpy.zeros(self.PopSize)
        self.plumScore.fill(float("inf"))

        self.Ripe_pos = numpy.zeros(self.dim)
        self.Ripe_score = float("inf")

        self.Unripe_pos = numpy.zeros(self.dim)
        self.Unripe_score = float("inf")

        self.gBest = numpy.zeros(self.dim)
        self.gBestScore = float("inf")

        self.flowers = numpy.zeros((self.PopSize, self.dim))
        for i in range(dim):
            self.flowers[:, i] = numpy.random.uniform(0, 1, PopSize) * (self.ub[i] - self.lb[i]) + self.lb[i]
            self.plums[:, i] = self.flowers[:, i]

        for i in range(0, self.PopSize):
            self.flowerScore[i] = self.objf(self.flowers[i, :])
            self.plumScore[i] = self.objf(self.plums[i, :])

        minimum = self.plumScore[0]
        minIndex = 0
        for i in range(1, self.PopSize):
            if self.plumScore[i] < minimum:
                minimum = self.plumScore[i]
                minIndex = i
        if minimum < self.gBestScore:
            self.gBest = self.plums[minIndex, :].copy()
            self.gBestScore = minimum

    def iterate(self):
        for i in range(0, self.PopSize):
            fitness = self.plumScore[i]

            if fitness < self.Ripe_score:
                self.Unripe_score = self.Ripe_score
                self.Unripe_pos = self.Ripe_pos.copy()
                self.Ripe_score = fitness
                self.Ripe_pos = self.plums[i, :].copy()

            if fitness > self.Ripe_score and fitness < self.Unripe_score:
                self.Unripe_score = fitness
                self.Unripe_pos = self.plums[i, :].copy()

        for i in range(0, self.PopSize):
            rp = random.random()
            if rp >= self.FT:
                for j in range(self.dim):
                    self.flowers[i][j] = self.flowers[i][j] + random.uniform(self.FRmin, self.FRmax) * (self.plums[i][j] - self.flowers[i][j])
            elif rp >= self.RT:
                for j in range(self.dim):
                    r1 = random.random()
                    r2 = random.random()

                    self.flowers[i][j] = self.flowers[i][j] + 2 * r1 * (self.Ripe_pos[j] - self.flowers[i][j]) \
                                    + 2 * r2 * (self.Unripe_pos[j] - self.flowers[i][j])
            else:
                sigma_ripe = 1
                if self.plumScore[i] >= self.Ripe_score:
                    sigma_ripe = numpy.exp((self.Ripe_score - self.plumScore[i]) / (abs(self.plumScore[i]) + self.eps))
                for j in range(self.dim):
                    self.flowers[i][j] = self.plums[i][j] * (1 + numpy.random.normal(0, sigma_ripe))

        for i in range(0, self.PopSize):
            for j in range(self.dim):
                self.flowers[i, j] = numpy.clip(self.flowers[i, j], self.lb[j], self.ub[j])

        for i in range(0, self.PopSize):
            self.flowerScore[i] = self.objf(self.flowers[i, :])
            self.plumScore[i] = self.objf(self.plums[i, :])
            if self.flowerScore[i] < self.plumScore[i]:
                for j in range(self.dim):
                    self.plums[i][j] = self.flowers[i][j]
                self.plumScore[i] = self.flowerScore[i]

        minimum = self.plumScore[0]
        minIndex = 0
        for i in range(1, self.PopSize):
            if self.plumScore[i] < minimum:
                minimum = self.plumScore[i]
                minIndex = i
        if minimum < self.gBestScore:
            self.gBest = self.plums[minIndex, :].copy()
            self.gBestScore = minimum

        return self.gBestScore, self.Ripe_score, self.Unripe_score
