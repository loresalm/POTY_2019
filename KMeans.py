import random
import numpy as np


class KMeans:

    def parse(self, x):
        """
        parse the digits file into tuples of
        (digit label, numpy array of vector representation of digit image)
        """
        return (x[len(x)-1], x[:len(x)-1:])

    def parseALL(self, xALL):
        labell_data = []
        for i in xALL:
            labell_data.append(self.parse(i))

        return labell_data

    def init_centers(self, labelled_data, K):

        center_list = []
        sampled_center = random.sample(labelled_data, K)
        for center_i in sampled_center:
            center_list.append(center_i[1])
        return center_list


    #given datapoints and current centers, assign each datapoint
    #to its nearest center. This builds clusters.

    def build_clusters(self, labelled_data, unlabelled_centers):

        # enumerate because centers are arrays which are unhashable
        # (basically we assign each center a number (i.e. cluster center #x)
        # but this is not related to the digit the cluster is supposed to represent)
        centers_indices = range(len(unlabelled_centers))

        # initialize an empty dict for each center. The dict will contain
        # all the datapoints that are closer to that center than to any other.
        # That list is the cluster of that center.
        clusters = {c: [] for c in centers_indices}

        for (label, vector) in labelled_data:
            # for each datapoint, pick the closest center.
            smallest_distance = float("inf")
            for cj_index in centers_indices:
                cj = unlabelled_centers[cj_index]
                ##compute L2 distance

                distance = np.sqrt(((vector - cj) ** 2).sum())

                if distance < smallest_distance:
                    closest_center_index = cj_index
                    smallest_distance = distance
            # allocate that datapoint to the cluster of that center.
            clusters[closest_center_index].append((label, vector))
        return list(clusters.values())

    # compute the center of a cluster
    def mean_cluster(self, labelled_cluster):
        """
        compute the mean (i.e. the center at the middle) of a list of vectors (a cluster).
        take the sum and then divide by the size of the cluster.
        assume all datapoints in labelled_cluster are labelled.

        input: labelled_center: one cluster
        output: the mean of this cluster through all datapoints in this cluster
        """
        # element-wise sums a list of arrays. The initial value is the first date vector
        sum_of_points = labelled_cluster[0][1].copy()


        for (label, vector) in labelled_cluster[1:]:
            sum_of_points += vector

        # mean w.r.t the size of the cluster

        mean_of_points = sum_of_points * (1.0 / len(labelled_cluster))
        return mean_of_points

    # update centers
    def move_centers(self, labelled_clusters):
        """
        return a list of centers corresponding to the current clusters by computing their means.

        input: labelled_centers: a list of current clusters
        output: new_centers: a list of new centers
        """
        new_centers = []
        # compute the mean of each cluster
        for cluster in labelled_clusters:
            new_centers.append(self.mean_cluster(cluster))
        return new_centers

    def repeat_until_convergence(self, labelled_data, unlabelled_centers, labelled_clusters):
        """
        build clusters around centers, then keep moving the centers
        until the moves are no longer significant, i.e. we've found
        the best-fitting centers for the data.

        input: labelled_data: training datasets
               unlabelled_centers: initial centers
               labelled_clusters: initial clusters based on inital centers
        output:
               labelled_clusters: clusters from the last update
               unlabelled_centers: centers from the last update
        """

        previous_max_difference = 0
        while True:
            unlabelled_old_centers = unlabelled_centers
            unlabelled_centers = self.move_centers(labelled_clusters)
            labelled_clusters = self.build_clusters(labelled_data, unlabelled_centers)
            # we keep old_clusters and clusters so we can get the maximum difference
            # between center positions every time. We say the centers have converged
            # when the maximum difference between center positions is small.
            differences = []
            for old_center, new_center in zip(unlabelled_old_centers, unlabelled_centers):
                difference = np.sqrt(((old_center - new_center) ** 2).sum())
                differences.append(difference)

            max_difference = max(differences)
            difference_change = abs(
                (max_difference - previous_max_difference) / np.mean([previous_max_difference, max_difference])) * 100
            previous_max_difference = max_difference
            # difference change is nan once the list of differences is all zeroes.
            if np.isnan(difference_change):
                break
        return labelled_clusters, unlabelled_centers

    # main function for k-means clustering
    def cluster(self, labelled_data, k):
        """
        run k-means clustering on the data. It is assumed that the data is labelled.

        input: labelled_data: datapoints will be clustered.
               k: the number of clusters
        output: lists of final clusters and centers
        """
        # step 1: initialize centers randomly and set up clusters
        centers = self.init_centers(labelled_data, k)
        clusters = self.build_clusters(labelled_data, centers)
        # step 2: update centers util convergence
        final_clusters, final_centers = self.repeat_until_convergence(labelled_data, centers, clusters)
        return list(final_clusters), list(final_centers)