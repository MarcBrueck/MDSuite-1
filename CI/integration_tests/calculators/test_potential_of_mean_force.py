"""
MDSuite: A Zincwarecode package.

License
-------
This program and the accompanying materials are made available under the terms
of the Eclipse Public License v2.0 which accompanies this distribution, and is
available at https://www.eclipse.org/legal/epl-v20.html

SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the Zincwarecode Project.

Contact Information
-------------------
email: zincwarecode@gmail.com
github: https://github.com/zincware
web: https://zincwarecode.com/

Citation
--------
If you use this module please cite us with:

Summary
-------
"""
import os

import pytest
from zinchub import DataHub

import mdsuite as mds
from mdsuite.utils.testing import assertDeepAlmostEqual


@pytest.fixture(scope="session")
def traj_file(tmp_path_factory) -> str:
    """Download trajectory file into a temporary directory and keep it for all tests"""
    temporary_path = tmp_path_factory.getbasetemp()

    NaCl = DataHub(url="https://github.com/zincware/DataHub/tree/main/NaCl_gk_i_q")
    NaCl.get_file(path=temporary_path)

    return (temporary_path / NaCl.file_raw).as_posix()


@pytest.fixture(scope="session")
def true_values() -> dict:
    """Example fixture for downloading analysis results from github"""
    NaCl = DataHub(url="https://github.com/zincware/DataHub/tree/main/NaCl_gk_i_q")
    return NaCl.get_analysis(analysis="PotentialOfMeanForce.json")


def test_project(traj_file, true_values, tmp_path):
    """Test the pomf called from the project class"""
    os.chdir(tmp_path)
    project = mds.Project()
    project.add_experiment(
        "NaCl", simulation_data=traj_file, timestep=0.002, temperature=1400
    )

    computation = project.run.PotentialOfMeanForce(plot=False)

    assertDeepAlmostEqual(computation["NaCl"].data_dict, true_values, decimal=-0)


def test_experiment(traj_file, true_values, tmp_path):
    """Test the pomf called from the experiment class"""
    os.chdir(tmp_path)
    project = mds.Project()
    project.add_experiment(
        "NaCl", simulation_data=traj_file, timestep=0.002, temperature=1400
    )

    computation = project.experiments["NaCl"].run.PotentialOfMeanForce(plot=False)

    assertDeepAlmostEqual(computation.data_dict, true_values, decimal=0)
