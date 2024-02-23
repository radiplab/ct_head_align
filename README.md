# Landmark-Based CT Head Alignment
This code will align a CT head by identifying the cochleas and nasal bridge and aligning them. The cochleas are aligned along the y and z axes, and the nasal bridge is aligned with the cochleas on the axial plane. The alignment is similar to registration to the orbito-meatal line or AC-PC line (about 5 degrees counter-clockwise from AC-PC), with the added benefit that skull base structures are more precisely aligned and symmetric. It uses a U-Net CNN. 

If you utilize this article in your research, please provide a citation. Publication is currently in process, so in the meantime e-mail me at jcramer10@gmail.com for more information.

Similarly, I am a physician first, and welcome your feedack on this project and the code at jcramer10@gmail.com.

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
