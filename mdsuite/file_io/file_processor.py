"""
This program and the accompanying materials are made available under the terms of the
Eclipse Public License v2.0 which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-v20.html
SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the Zincware Project.

Description: Parent class for the file readers. This file will process a file for
information and update the project SQL database. Following this, it will read the
data and dump it into the hdf5 database.
"""
import abc
from chemfiles import Trajectory
from chemfiles.frame import Frame


class FileProcessor(metaclass=abc.ABCMeta):
    """
    Parent class for processing files.
    """

    def __init__(self, file_path: str, experiment_name: str, format: str = None):
        """
        Constructor for the file processor.

        Parameters
        ----------
        file_path : str
                Path to the files.
        experiment_name : str
                Name of the experiment object. Used in the database update.
        format : str
                Format of the file if not clear from the extension.
        """
        # User input
        self.file_path = file_path
        self.experiment_name = experiment_name
        self.format = format

        # Class declared
        if self.format is None:
            try:
                self.trajectory = Trajectory(self.file_path)
            except ValueError:
                raise ValueError("Unknown file type, please specify a format.")
        else:
            try:
                self.trajectory = Trajectory(self.file_path, format=format)
            except ValueError:
                raise ValueError("File format not recognized.")

    def _update_experiment_properties(self):
        """
        Update the project SQL database with the data information.
        Returns
        -------

        """
        data = self._extract_system_properties()

    def _build_database_structure(self):
        """
        Construct a database structure given the data structure.
        Returns
        -------

        """
        pass

    @abc.abstractmethod
    def _extract_system_properties(self) -> dict:
        """
        Process the trajectory file and extract the properties.

        Returns
        -------
        data : dict
                A dictionary of data to be added the sql database.
        """
        pass

    def _deconstruct_frame(self, frame: Frame):
        """
        Deconstruct a frame into its components for loading into the database.

        Parameters
        ----------
        frame : Frame
                Atoms frame to process.

        Returns
        -------

        """
        pass

    def _read_frames(self, n_frames: int):
        """
        Read a frame from the trajectory and split it by species and properties.

        Parameters
        ----------
        n_frames : int
                number of frames to read

        Returns
        -------

        """
        for _ in range(n_frames):
            self.trajectory.read()


    def process_data(self):
        """
        Process the data and add it to the hdf5 database.

        Returns
        -------

        """
        # Instantiate database object TODO: Adjust db to check for existing db.
        # Give the db object the database structure.
        # Loop over batches, read, and updated hdf5 database.
        pass


if __name__ == '__main__':
    """
    """
    obj = Trajectory('/tikhome/stovey/work/Interatomic_Potentials_Investigation/Molten_Salts/Chlorides/NaCl/Classical_Potential/old/NaCl_Data.lammpstrj')
    data = obj.read()
    print(data.atoms[0]['x'])
