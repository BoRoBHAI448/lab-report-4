import random

# Point class - ekta (x,y) coordinate store korar jonno
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None  # kon cluster e point ta ache ta rakhar jonno

# Modified KMeans class - Manhattan distance use kora hoyeche
class KMeansManhattan:
    def __init__(self, points, clusters, grid_size=30):
        self.grid_size = grid_size  # 2D Matrix er size fix korlam
        # Random 100 ta point generate korchi
        self.points = [Point(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(points)]
        # Random 10 ta cluster center generate korchi
        self.centroids = [Point(random.randint(0, grid_size-1), random.randint(0, grid_size-1)) for _ in range(clusters)]
        self.clusters = clusters
        self.run()  # main function call korchi

    # Manhattan distance function (New: Euclidean na, Manhattan use korchi)
    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    # Main logic of KMeans
    def run(self):
        while True:
            changed = False
            for p in self.points:
                min_dist = float('inf')
                closest_cluster = None
                for i, c in enumerate(self.centroids):
                    dist = self.manhattan_distance(p, c)  # Manhattan distance diye nearest cluster ber kortesi
                    if dist < min_dist:
                        min_dist = dist
                        closest_cluster = i
                if p.cluster != closest_cluster:
                    p.cluster = closest_cluster
                    changed = True

            if not changed:
                break  # jokhon kono point er cluster ar change hochhe na, loop bondho

            # Cluster center update kortesi - new centroid ber kortesi
            for i in range(self.clusters):
                cluster_points = [p for p in self.points if p.cluster == i]
                if cluster_points:
                    avg_x = sum(p.x for p in cluster_points) // len(cluster_points)
                    avg_y = sum(p.y for p in cluster_points) // len(cluster_points)
                    self.centroids[i] = Point(avg_x, avg_y)

        self.display_results()

    # New: Cluster center + members print kora, then matrix
    def display_results(self):
        # Cluster Centers Print
        print("\nCluster Centers:")
        for idx, center in enumerate(self.centroids):
            print(f"Cluster {idx + 1} center: ({center.x}, {center.y})")

        # Cluster Members Print
        print("\nCluster Members:")
        for i in range(self.clusters):
            members = [(p.x, p.y) for p in self.points if p.cluster == i]
            print(f"Cluster {i + 1} members: {members}")

        # Matrix Visualization (like previous)
        matrix = [['.' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        # Data points mark kora (0-9 digit)
        for p in self.points:
            matrix[p.y][p.x] = str((p.cluster + 1) % 10)

        # Cluster centers mark kora '*' diye
        for c in self.centroids:
            matrix[c.y][c.x] = '*'

        print("\nClustered 2D Matrix Visualization:")
        for row in matrix:
            print(' '.join(row))  # row wise matrix print kortesi

# Extra part: Data file save kora (New)
def save_data_to_file():
    with open("points_data.txt", "w") as f:
        for _ in range(100):
            x = random.randint(0, 29)
            y = random.randint(0, 29)
            f.write(f"{x},{y}\n")  # 100 ta random point file e likhchi

# Main function
if __name__ == "__main__":
    save_data_to_file()  # first points file save korchi
    KMeansManhattan(points=100, clusters=10)  # tarpor clustering start korchi
