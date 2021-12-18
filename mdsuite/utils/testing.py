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
import multiprocessing
import traceback

import numpy as np


def assertDeepAlmostEqual(expected, actual, *args, **kwargs):
    """
    Assert that two complex structures have almost equal contents.
    Compares lists, dicts and tuples recursively. Checks numeric values
    using test_case's :py:meth:`unittest.TestCase.assertAlmostEqual` and
    checks all other values with :py:meth:`unittest.TestCase.assertEqual`.
    Accepts additional positional and keyword arguments and pass those
    intact to assertAlmostEqual() (that's how you specify comparison
    precision).

    Parameters
    ----------
    decimal: int
        The desired positional precision.
        See numpy.testing.assert_array_almost_equal for keyword arguments

    References
    ----------
    https://github.com/larsbutler/oq-engine/blob/master/tests/utils/helpers.py

    """
    if isinstance(expected, (int, float, complex, np.ndarray, list)):
        np.testing.assert_array_almost_equal(expected, actual, *args, **kwargs)
    elif isinstance(expected, dict):
        assert set(expected) == set(actual)
        for key in expected:
            assertDeepAlmostEqual(expected[key], actual[key], *args, **kwargs)
    else:
        assert expected == actual


class MDSuiteProcess(multiprocessing.Process):
    """
    Process class for use in ZnVis testing.
    """

    def __init__(self, *args, **kwargs):
        """
        Multiprocessing class constructor.
        """
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        """
        Run the process and catch exceptions.
        """
        try:
            multiprocessing.Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))

    @property
    def exception(self):
        """
        Exception property to be stored by the process.
        """
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception


if __name__ == "__main__":
    dict_1 = {"a": [1, 2, 3, 4]}
    dict_2a = {"a": {"b": np.array([1, 2, 3, 4])}}
    dict_2b = {"a": {"b": [1, 2, 3, 4]}}
    dict_3a = {"a": {"c": np.array([1.10, 2.10, 3.11, 4.0])}}
    dict_3b = {"a": {"c": np.array([1.11, 2.09, 3.10, 4.0])}}

    print(assertDeepAlmostEqual(dict_3a, dict_3b, decimal=1))
    print(assertDeepAlmostEqual(dict_2a, dict_2b, decimal=1))
