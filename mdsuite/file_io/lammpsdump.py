"""
This program and the accompanying materials are made available under the terms of the
Eclipse Public License v2.0 which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-v20.html
SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the Zincware Project.

Description: Class for processing the lammps trajectory file.
"""
from mdsuite.file_io.file_processor import FileProcessor


class LammpsTrajectory(FileProcessor):
    """
    Class to process LAMMPS trajectory files with .lammpstrj file endings.
    """
    def _extract_system_properties(self) -> dict:
        """
        Extract system properties from the LAMMPS file.

        Returns
        -------
        system_data : dict
                A dictionary of the data in the system.
        """