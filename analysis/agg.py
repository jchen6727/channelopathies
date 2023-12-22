import utils

from changes I have changed this
dataFolder = '../data/'
batchLabel = 'batch_2023-12-13'   # v52_batch3'

params, data = utils.readBatchData(dataFolder, batchLabel, loadAll=False, saveAll=True, vars=[('simData','V_soma')], maxCombs=None) 