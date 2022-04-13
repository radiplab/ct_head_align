# Landmark-Based CT Head Alignment
This code will align a CT head by identifying the cochleas and nasal bridge. It uses a U-Net CNN so requires a GPU. 

Please cite the following article in any publications utilizing this code: TODO

## Getting Started
First, install the required libraries imported in the ct_head_align.py file. These include:
* monai
* numpy
* scipy
* SimpleITK
* torch
* skimage
* sympy

Then, in the ct_head_align_test.py file, run the test_integration_ct_head_align method as a unittest. This will align the 4 CT head studies located in the test_data folder, and output the results as an .nii.gz file to the working folder. You can compare the alignment results to the originals. 3D Slicer is a nice program for viewing .nii.gz files - you can just drag and drop them into the viewer.

## License
This code is provided under the MIT license. As stated in the license, THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
