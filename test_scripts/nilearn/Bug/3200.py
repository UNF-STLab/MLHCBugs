from nilearn import datasets
from nilearn.reporting import get_clusters_table
import numpy as np
from nibabel import Nifti1Image, AnalyzeImage
from nilearn.image import threshold_img
motor_images = datasets.fetch_neurovault_motor_task()
stat_img = motor_images.images[0]

threshold = 3.0
table1 = get_clusters_table(stat_img, threshold, cluster_threshold=10)
table2 = get_clusters_table(stat_img, threshold, cluster_threshold=0)
print(table1)
print(table2)
def test_threshold_img_with_cluster_threshold():
    """Check that threshold_img behaves as expected with cluster_threshold
    and/or two_sided.
    """
    # First we create a statistical image with specific characteristics
    # shape = (20, 20, 30)
    # affine = np.eye(4)
    # data = np.zeros(shape, dtype=int)
    # data[:2, :2, :2] = 4  # 8-voxel positive cluster
    # data[4:6, :2, :2] = -4  # 8-voxel negative cluster
    # data[8:11, 0, 0] = 5  # 3-voxel positive cluster
    # data[13:16, 0, 0] = -5  # 3-voxel positive cluster
    # data[:6, 4:10, :6] = 1  # 216-voxel positive cluster with low value
    # data[13:19, 4:10, :6] = -1  # 216-voxel negative cluster with low value
    # stat_img = Nifti1Image(data, affine, dtype=np.int16)
    stat_img = motor_images.images[0]
    # The standard approach should retain any clusters with values > 2
    thr_img = threshold_img(stat_img, threshold=2, two_sided=False, copy=True)
    print(np.unique(thr_img.get_fdata()))
    #assert np.array_equal(np.unique(thr_img.get_fdata()), np.array([0, 4, 5]))
    # With two-sided we get any clusters with |values| > 2
    thr_img = threshold_img(stat_img, threshold=2, two_sided=True, copy=True)
    print(np.unique(thr_img.get_fdata()))
    # assert np.array_equal(
    #     np.unique(thr_img.get_fdata()),
    #     np.array([-5, -4, 0, 4, 5]),
    # )
    # With a cluster threshold of 5 we get clusters with |values| > 2 and
    # cluster sizes > 5
    thr_img = threshold_img(
        stat_img,
        threshold=2,
        two_sided=True,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))
    #assert np.array_equal(np.unique(thr_img.get_fdata()), np.array([-4, 0, 4]))

    #assert np.sum(thr_img.get_fdata() == 4) == 8
    # With a cluster threshold of 5 we get clusters with |values| > 0.5 and
    # cluster sizes > 5
    thr_img = threshold_img(
        stat_img,
        threshold=0.5,
        two_sided=True,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))
    # assert np.array_equal(
    #     np.unique(thr_img.get_fdata()),
    #     np.array([-4, -1, 0, 1, 4]),
    # )
    # Now we disable two_sided again to get clusters with values > 0.5 and
    # cluster sizes > 5
    thr_img = threshold_img(
        stat_img,
        threshold=0.5,
        two_sided=False,
        cluster_threshold=5,
        copy=True,
    )
    print(np.unique(thr_img.get_fdata()))
    #assert np.array_equal(np.unique(thr_img.get_fdata()), np.array([0, 1, 4]))

# if table1 == table2:
#     print("pass")
# else:
#     print("fail")

test_threshold_img_with_cluster_threshold()

# [0.         2.00077105 2.00149131 ... 7.93853569 7.93925905 7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [-7.9414444  -7.92836809 -7.90569019 ...  7.93853569  7.93925905
#   7.94134521]
# [0.         0.50000864 0.50004089 ... 7.93853569 7.93925905 7.94134521]