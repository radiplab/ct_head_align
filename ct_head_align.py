import os
import shutil

from numpy import empty

def align(nii_path, output_path):
    """ Aligns a CT head by landmarks of cochleas and nasal bridge

    Parameters:
        nii_path (str): Full path to a CT head in .nii format
        output_path (str): Full path including .nii filename to output the aligned CT head
    """
    x = 5