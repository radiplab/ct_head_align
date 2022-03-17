import configparser
import glob
import os
import shutil
import unittest

from ct_head_align import align

class CTHeadAlignTest(unittest.TestCase):
    config = configparser.ConfigParser()
    config.read('./tests/paths.ini')
    paths_config = config['paths']
    test_data_path = paths_config['test_data_path']
    test_working_path = paths_config['test_working_path']
    if os.path.exists(test_working_path):
        shutil.rmtree(test_working_path)
    os.mkdir(test_working_path)

    def test_integration_ct_head_align(self):
        """
        Test alignment of a CT head by landmarks - test data downloaded from http://headctstudy.qure.ai/dataset
        """
        test_case_paths = sorted(glob.glob(os.path.join(self.test_data_path, '*.nii.gz')))
        for test_case_path in test_case_paths:
            filename_full = os.path.basename(test_case_path)
            filename_base = filename_full.split('.')[0]
            aligned_filename = filename_base + '_aligned' + '.nii.gz'
            aligned_path = os.path.join(self.test_working_path, aligned_filename)
            align(test_case_path, aligned_path)

if __name__ == '__main__':
    unittest.main()
