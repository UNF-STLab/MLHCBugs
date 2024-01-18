import numpy as np
import scipy.special as sps
from numpy.testing import (run_module_suite,
                           assert_,
                           assert_equal,
                           assert_raises,
                           assert_array_almost_equal)
from dipy.denoise.localpca import (mppca, genpca, _pca_classifier)
#values = localpca(np.array([[1, 1, 1,1], [3, 3, 3,3]]), 0.02, mask=None, patch_radius=2, pca_method='eig', tau_factor=2.3, out_dtype=None)
def localpca(arr, sigma, mask=None, patch_radius=2, pca_method='eig', tau_factor=2.3, out_dtype=None):
    r""" Performs local PCA denoising according to Manjon et al. [1]_.

    Parameters
    ----------
    arr : 4D array
        Array of data to be denoised. The dimensions are (X, Y, Z, N), where N
        are the diffusion gradient directions.
    sigma : float or 3D array
        Standard deviation of the noise estimated from the data.
    mask : 3D boolean array (optional)
        A mask with voxels that are true inside the brain and false outside of
        it. The function denoises within the true part and returns zeros
        outside of those voxels.
    patch_radius : int or 1D array (optional)
        The radius of the local patch to be taken around each voxel (in
        voxels). Default: 2 (denoise in blocks of 5x5x5 voxels).
    pca_method : 'eig' or 'svd' (optional)
        Use either eigenvalue decomposition (eig) or singular value
        decomposition (svd) for principal component analysis. The default
        method is 'eig' which is faster. However, occasionally 'svd' might be
        more accurate.
    tau_factor : float (optional)
        Thresholding of PCA eigenvalues is done by nulling out eigenvalues that
        are smaller than:

        .. math ::

                \tau = (\tau_{factor} \sigma)^2

        \tau_{factor} can be change to adjust the relationship between the
        noise standard deviation and the threshold \tau. If \tau_{factor} is
        set to None, it will be automatically calculated using the
        Marcenko-Pastur distribution [2]_.
        Default: 2.3 (according to [1]_)
    out_dtype : str or dtype (optional)
        The dtype for the output array. Default: output has the same dtype as
        the input.

    Returns
    -------
    denoised_arr : 4D array
        This is the denoised array of the same size as that of the input data,
        clipped to non-negative values

    References
    ----------
    .. [1] Manjon JV, Coupe P, Concha L, Buades A, Collins DL (2013)
           Diffusion Weighted Image Denoising Using Overcomplete Local
           PCA. PLoS ONE 8(9): e73021.
           https://doi.org/10.1371/journal.pone.0073021
    .. [2] Veraart J, Novikov DS, Christiaens D, Ades-aron B, Sijbers,
           Fieremans E, 2016. Denoising of Diffusion MRI using random matrix
           theory. Neuroimage 142:394-406.
           doi: 10.1016/j.neuroimage.2016.08.016
    """
    return tau_factor, genpca(arr, sigma=sigma, mask=mask, patch_radius=patch_radius,
                  pca_method=pca_method, tau_factor=tau_factor,
                  return_sigma=False, out_dtype=out_dtype)


S0 = 100 * np.ones((20, 20, 20, 20), dtype='f8')
S1 = 100 * np.ones((10, 10, 10, 10), dtype='f8')
tau_factor1,genpca1 = localpca(S0, sigma=np.ones((20, 20, 20)))
tau_factor2,genpca2 = localpca(S1, sigma=np.ones((10, 10, 10)))
if assert_equal(tau_factor1,tau_factor2) == None:
    print("tau_factor value is hardcoded")
else:
    print("tau_factor value takes hardcoded")