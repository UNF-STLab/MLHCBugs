import nibabel as nib
import numpy as np
import pandas as pd

from nilearn import reporting
from nilearn import datasets

motor_images = datasets.fetch_neurovault_motor_task()
stat_img = motor_images.images[0]

# Run get_clusters_table on stat_img
clusters_table, label_maps = reporting.get_clusters_table(
            stat_img, 3.6, two_sided=True, return_label_maps=True
        )
# Select negative tail
neg_clusters_table = clusters_table[clusters_table["Peak Stat"] < 0]
neg_label_maps = label_maps[1]

# Get cluster IDs and its respective coordinates from the clusters table
new_clusters_table = neg_clusters_table.apply(pd.to_numeric, errors='coerce').dropna()
cluster_ids = new_clusters_table["Cluster ID"].to_list()
coords = new_clusters_table[["X", "Y", "Z"]].to_numpy()

# Use the coordinates from the clusters table to find the Cluster ID in the label map 
ijk = nib.affines.apply_affine(np.linalg.inv(neg_label_maps.affine), coords).astype(int)
cluster_label_ids = neg_label_maps.get_fdata()[tuple(ijk.T)]

print(cluster_ids, cluster_label_ids)