import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import shutil

import mdsuite as mds # Cool name for professionalism purposes

new_case = True

if new_case:
    try:
        shutil.rmtree('Argon')
    except FileNotFoundError:
        pass



argon = mds.Experiment(analysis_name="Argon", time_step=2, temperature=70.0, units='real')

if new_case:
    argon.add_data(trajectory_file='../gk_data.lmp_traj')

argon.run_computation('GreenKuboThermalConductivity', data_range=2000, plot=True, correlation_time=3)
