"""
This program and the accompanying materials are made available under the terms of the
Eclipse Public License v2.0 which accompanies this distribution, and is available at
https://www.eclipse.org/legal/epl-v20.html

SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the MDSuite Project.

Python __init__ file
"""
import logging
import os
import sys
from .project import Project
from .experiment import Experiment
from .graph_modules import adjacency_matrix
from .utils.report_computer_characteristics import Report

__all__ = ['Project', 'Experiment', 'adjacency_matrix', 'Report']

logger = logging.getLogger("mdsuite")
logger.setLevel(logging.INFO)

# Formatter for advanced logging
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

channel = logging.StreamHandler(sys.stdout)
channel.setLevel(logging.DEBUG)
channel.setFormatter(formatter)

logger.addHandler(channel)
