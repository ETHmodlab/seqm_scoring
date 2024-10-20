
# Combining de novo molecular design with semiempirical protein–ligand binding free energy calculation

[![python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=yellow)](https://www.python.org)
[![pytorch](https://img.shields.io/badge/PyTorch-1.13.1-EE4C2C.svg?style=flat&logo=pytorch)](https://pytorch.org)
[![RDKit badge](https://img.shields.io/badge/Powered%20by-RDKit-3838ff.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAFVBMVEXc3NwUFP8UPP9kZP+MjP+0tP////9ZXZotAAAAAXRSTlMAQObYZgAAAAFiS0dEBmFmuH0AAAAHdElNRQfmAwsPGi+MyC9RAAAAQElEQVQI12NgQABGQUEBMENISUkRLKBsbGwEEhIyBgJFsICLC0iIUdnExcUZwnANQWfApKCK4doRBsKtQFgKAQC5Ww1JEHSEkAAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMi0wMy0xMVQxNToyNjo0NyswMDowMDzr2J4AAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjItMDMtMTFUMTU6MjY6NDcrMDA6MDBNtmAiAAAAAElFTkSuQmCC)](https://www.rdkit.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![DOI](https://img.shields.io/badge/DOI-10.1038/s41557--023--01360--5-green)]()

![](imgs/docking_dg_calculation.png)

This repository contains a reference implementation to preprocess the data, as well as to train and apply the de novo design models introduced in Combining de novo molecular design with semiempirical protein–ligand binding free energy calculation by Michael Iff, Kenneth Atz, Clemens Isert, Irene Pachon Angona, Leandro Cotos, Mattis Hilleke, Jan A. Hiss, and Gisbert Schneider(2024).


## 1. Environment
Create and activate the dragonfly environment. 

```
conda env create -f xtb_environment.yml
conda activate xtb_env
```


## 2. Running the Script

Once the environment is set up, you can run the Python script with the necessary arguments. Use the following command structure:

To preprocess the binding site for a given protein stored as a PDB file and its ligand as an SDF file in the `input/` directory, use the following commands:

```
cd seqm_scoring
python calculation.py -folder <path_to_your_xyz_files> -method <gfnff|gfn2> -system <receptor|ligand|combined> -charge <charge_value>
```

```
python calculation.py -folder M01/ -method gfnff -system combined -charge 0
```

This will execule the following xtb command:
```
xtb --gfnff M01/M01_combined.xyz --hess --gbsa water  > M01/M01_combined_gfnff.txt
```

The resulkts are then stored here:
```
M01_combined_gfnff.txt
```

## 3. License
The software was developed at ETH Zurich and is licensed under the MIT license, as described in `LICENSE`.

## 4. Citation
```
@article{iff2024combining,
  title={Combining de novo molecular design with semiempirical protein–ligand binding free energy calculation},
  author={Iff, Michael and Atz, Kenneth and Isert, Clemens and Pachon Angona, Irene and Cotos, Leandro and Hilleke, Mattis and Hiss, Jan A. and Schneider, Gisbert},
  year={2024},
  journal={},
  publisher={},
  volume={},
  number={}
}
```


