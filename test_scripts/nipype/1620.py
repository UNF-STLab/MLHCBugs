import simplejson as json
from nipype.interfaces.ants import Registration
from nipype.testing import (assert_equal, assert_not_equal, assert_raises,
                            assert_true, assert_false, with_setup, package_check,
                            skipif, example_data)

def assert_all_true(ref_dict, tst_dict):
    for key, value in list(ref_dict.items()):
        if tst_dict[key] != value:
            return False
    return True

settings = example_data(example_data('smri_ants_registration_settings.json'))
with open(settings) as setf:
    data_dict = json.load(setf)
tsthash = Registration(from_file=settings)
yield assert_all_true, data_dict, tsthash.inputs.get_traitsfree()

