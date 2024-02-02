"""
batch.py 

Batch simulation for Excitatory Weight Normalization
"""
import numpy as np
from netpyne import specs
from netpyne.batch import Batch


# ----------------------------------------------------------------------------------------------
# Weight Normalization Exc
# ----------------------------------------------------------------------------------------------

#pops =  ['IT2', 'IT4', 'IT5A', 'IT5B', 'PT5B', 'IT6', 'CT6', 'PV2', 'SOM2'],

if __name__ == '__main__':


    b = weightNormE(pops = ['PT5B'], secs = ['soma'], locs = [0.5],
                allSegs = False, rule = 'PT5B_full', weights= [0.1, 0.2])

    b.saveFolder = '../data/'+b.batchLabel
    b.method = 'grid'  # evol
    setRunCfg(b, 'mpi_direct')  # cores = nodes * 8
    b.run() # run batch
def weightNormE(pops = ['PT5B'], secs = None, locs = None,
                allSegs = False, rule = 'PT5B_full', weights= (0.1, 0.2)):


    # Add params
    from netParams_cell import netParams

    excludeSegs = ['axon']
    if not secs:
        secs = []
        locs = []
        for secName, sec in netParams.cellParams[rule]['secs'].items():
            if secName not in excludeSegs:
                if allSegs:
                    nseg = sec['geom']['nseg']
                    for iseg in list(range(nseg)):
                        secs.append(secName) 
                        locs.append((iseg+1)*(1.0/(nseg+1)))
                else:
                    secs.append(secName) 
                    locs.append(0.5)

    params = specs.ODict()
    params[('NetStim1', 'pop')] = pops
    params[('NetStim1', 'loc')] = locs
    params[('NetStim1', 'sec')] = secs
    params[('NetStim1', 'weight')] = weights

    groupedParams = [('NetStim1', 'sec'), ('NetStim1', 'loc')]
    b = Batch(params=params, netParamsFile='netParams_cell.py', cfgFile='cfg_cell.py', initCfg=initCfg, groupedParams=groupedParams)

    return b




# ----------------------------------------------------------------------------------------------
# Run configurations
# ----------------------------------------------------------------------------------------------
def setRunCfg(b, type='mpi_bulletin', nodes=1, coresPerNode=8):
    if type=='mpi_bulletin':
        b.runCfg = {'type': 'mpi_bulletin', 
            'script': 'init_cell.py', 
            'skip': True}

# ----------------------------------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------------------------------




if __name__ == '__main__': 


    b = weightNormE(pops = ['PT5B'], secs = ['soma'], locs = [0.5],
                allSegs = False, rule = 'PT5B_full', weights= [0.1, 0.2])

    b.saveFolder = '../data/'+b.batchLabel
    b.method = 'grid'  # evol
    setRunCfg(b, 'mpi_direct')  # cores = nodes * 8
    b.run() # run batch 