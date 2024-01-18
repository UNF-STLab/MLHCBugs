from nilearn import datasets
from nilearn.reporting import get_clusters_table
import numpy as np
from nibabel import Nifti1Image, AnalyzeImage
from nilearn.image import threshold_img
motor_images = datasets.fetch_neurovault_motor_task()
stat_img = motor_images.images[0]

threshold = 3.0
table1 = get_clusters_table(stat_img, threshold, cluster_threshold=2)
table2 = get_clusters_table(stat_img, threshold, cluster_threshold=4)
print(table1)
print(table2)
def test_threshold_img_with_cluster_threshold():
    """Check that threshold_img behaves as expected with cluster_threshold
    and/or two_sided.
    """
    stat_img = motor_images.images[0]
   
    thr_img = threshold_img(stat_img, threshold=2, two_sided=False, copy=True)
    print(np.unique(thr_img.get_fdata()))
 
    thr_img = threshold_img(stat_img, threshold=2, two_sided=True, copy=True)
    print(np.unique(thr_img.get_fdata()))

    thr_img = threshold_img(
        stat_img,
        threshold=2,
        two_sided=True,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))

    thr_img = threshold_img(
        stat_img,
        threshold=0.5,
        two_sided=True,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))
    thr_img = threshold_img(
        stat_img,
        threshold=0.5,
        two_sided=False,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))

test_threshold_img_with_cluster_threshold()

# [0.         2.00077105 2.00149131 ... 7.93853569 7.93925905 7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [0.         0.50000864 0.50004089 ... 7.93853569 7.93925905 7.94134521]

# [0.         2.00077105 2.00149131 ... 7.93853569 7.93925905 7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [0.         0.50000864 0.50006717 ... 7.93853569 7.93925905 7.94134521]

#   Cluster ID     X     Y     Z  Peak Stat Cluster Size (mm3)
# 0          1  39.0 -22.0  58.0   7.941345              58347
# 1         1a  42.0 -19.0  19.0   7.941345                   
# 2         1b   6.0 -10.0  52.0   7.941345                   
# 3         1c  33.0  -7.0  -2.0   7.905312                   
# 4          2 -18.0 -52.0 -23.0   7.941345              10044
# 5         2a  -6.0 -67.0 -38.0   3.443122                   
# 6          3  -6.0 -70.0 -41.0   3.627778                 54
#    Cluster ID     X     Y     Z  Peak Stat Cluster Size (mm3)
# 0           1  39.0 -22.0  58.0   7.941345              60399
# 1          1a  42.0 -19.0  19.0   7.941345                   
# 2          1b   6.0 -10.0  52.0   7.941345                   
# 3          1c  33.0  -7.0  -2.0   7.905312                   
# 4           2 -18.0 -52.0 -23.0   7.941345              10260
# 5          2a  -6.0 -70.0 -38.0   4.260736                   
# 6           3  60.0   8.0  28.0   3.358555                108
# 7           4 -66.0 -25.0  31.0   3.338923                351
# 8           5  54.0  -1.0   7.0   3.287375                108
# 9           6 -15.0 -94.0 -11.0   3.236299                 81
# 10          7 -57.0  -1.0  40.0   3.020055                 27
# 11          8 -60.0  -4.0  40.0   3.018578                 27
# 12          9  45.0 -58.0  -2.0   3.007471                 27


# Cluster ID     X     Y     Z  Peak Stat Cluster Size (mm3)
# 0          1  39.0 -22.0  58.0   7.941345              60399
# 1         1a  42.0 -19.0  19.0   7.941345                   
# 2         1b   6.0 -10.0  52.0   7.941345                   
# 3         1c  33.0  -7.0  -2.0   7.905312                   
# 4          2 -18.0 -52.0 -23.0   7.941345              10260
# 5         2a  -6.0 -70.0 -38.0   4.260736                   
# 6          3 -66.0 -25.0  31.0   3.338923                351
#    Cluster ID     X     Y     Z  Peak Stat Cluster Size (mm3)
# 0           1  39.0 -22.0  58.0   7.941345              60399
# 1          1a  42.0 -19.0  19.0   7.941345                   
# 2          1b   6.0 -10.0  52.0   7.941345                   
# 3          1c  33.0  -7.0  -2.0   7.905312                   
# 4           2 -18.0 -52.0 -23.0   7.941345              10260
# 5          2a  -6.0 -70.0 -38.0   4.260736                   
# 6           3  60.0   8.0  28.0   3.358555                108
# 7           4 -66.0 -25.0  31.0   3.338923                351
# 8           5  54.0  -1.0   7.0   3.287375                108
# 9           6 -15.0 -94.0 -11.0   3.236299                 81
# 10          7 -57.0  -1.0  40.0   3.020055                 27