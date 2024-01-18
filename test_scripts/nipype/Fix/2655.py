from nipype.interfaces.freesurfer import ReconAll
print({'Expected': False, 'Calculated': ReconAll().version is None})