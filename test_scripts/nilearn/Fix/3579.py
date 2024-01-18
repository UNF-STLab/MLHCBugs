from nilearn.datasets import fetch_language_localizer_demo_dataset
from nilearn.glm.first_level import first_level_from_bids
from nilearn.glm.second_level import non_parametric_inference

data_dir, _ = fetch_language_localizer_demo_dataset()
task_label = 'languagelocalizer'
models, models_run_imgs, models_events, models_confounds = \
    first_level_from_bids(
        data_dir, task_label,
        img_filters=[('desc', 'preproc')])
model_and_args = zip(models, models_run_imgs, models_events, models_confounds)
for m_idx, (model, imgs, events, confounds) in enumerate(model_and_args):
     model.fit(imgs, events, confounds)
     model.compute_contrast('language-string')
design_matrix = pd.DataFrame(
    [1] * len(second_level_input),
    columns=['intercept'],
)

n_perm=1000

out_dict = non_parametric_inference(
    second_level_input=models,
    design_matrix=design_matrix,
    first_level_contrast='language-string',
    model_intercept=True,
    n_perm=n_perm,  
    two_sided_test=False,
    smoothing_fwhm=8.0,
    n_jobs=1,
)