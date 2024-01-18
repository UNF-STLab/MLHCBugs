from __future__ import unicode_literals
from ..model import EstimateModel

def test_EstimateModel_inputs():
    input_map = dict(estimation_method=dict(field='method',
    mandatory=True,
    ),
    flags=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    paths=dict(),
    spm_mat_file=dict(copyfile=True,
    field='spmmat',
    mandatory=True,
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    write_residuals=dict(field='write_residuals',
    ),
    )
    inputs = EstimateModel.input_spec()


def test_EstimateModel_outputs():
    output_map = dict(ARcoef=dict(),
    Cbetas=dict(),
    RPVimage=dict(),
    SDbetas=dict(),
    SDerror=dict(),
    beta_images=dict(),
    labels=dict(),
    mask_image=dict(),
    residual_image=dict(),
    residual_images=dict(),
    spm_mat_file=dict(),
    )
    outputs = EstimateModel.output_spec()
    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value