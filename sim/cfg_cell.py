"""
cfg.py 

Simulation configuration for M1 model (using NetPyNE)

Contributors: salvadordura@gmail.com
"""

from netpyne import specs
import pickle

cfg = specs.SimConfig()  

#------------------------------------------------------------------------------
#
# SIMULATION CONFIGURATION
#
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Run parameters
#------------------------------------------------------------------------------
cfg.duration = 1*1e3
cfg.dt = 0.025
cfg.seeds = {'conn': 4321, 'stim': 1234, 'loc': 4321} 
cfg.hParams = {'celsius': 34, 'v_init': -80}  
cfg.verbose = 0
cfg.createNEURONObj = 1
cfg.createPyStruct = 1
cfg.connRandomSecFromList = False  # set to false for reproducibility 
cfg.cvode_active = False
cfg.cvode_atol = 1e-6
cfg.cache_efficient = True
cfg.printRunTime = 0.1
cfg.oneSynPerNetcon = True  # only affects conns not in subconnParams; produces identical results

cfg.includeParamsLabel = False #True # needed for modify synMech False
cfg.printPopAvgRates = [1000., 5000.]

cfg.checkErrors = False

cfg.saveInterval = 100 # define how often the data is saved, this can be used with interval run if you want to update the weights more often than you save
cfg.intervalFolder = 'interval_saving'


#------------------------------------------------------------------------------
# Recording 
#------------------------------------------------------------------------------
allpops = ['PT5B']
#['IT2','PV2','SOM2','IT4','IT5A','PV5A','SOM5A','IT5B','PT5B','PV5B','SOM5B','IT6','CT6','PV6','SOM6']

cfg.recordTraces = {'V_soma': {'sec':'soma', 'loc':0.5, 'var':'v'}}
					#'V_soma_ih': {'sec':'soma', 'loc':0.5, 'var':'gbar', 'mech':'hd', 'conds':{'pop': 'PT5B'}}}
					# 'V_apic_26': {'sec':'apic_26', 'loc':0.5, 'var':'v', 'conds':{'pop': 'PT5B'}},
					# 'V_dend_5': {'sec':'dend_5', 'loc':0.5, 'var':'v', 'conds':{'pop': 'PT5B'}}}
					#'I_AMPA_Adend2': {'sec':'Adend2', 'loc':0.5, 'synMech': 'AMPA', 'var': 'i'}}


cfg.recordStim = True
cfg.recordTime = True
cfg.recordStep = 0.025


#------------------------------------------------------------------------------
# Saving
#------------------------------------------------------------------------------
cfg.simLabel = 'v56_tune3'
cfg.saveFolder = '../data/v56_manualTune'
cfg.savePickle = True
cfg.saveJson = True
cfg.saveData = True #added
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams']#, 'net']
cfg.backupCfgFile = None #['cfg.py', 'backupcfg/'] 
cfg.gatherOnlySimData = False
cfg.saveCellSecs = True
cfg.saveCellConns = False
cfg.compactConnFormat = 0

#------------------------------------------------------------------------------
# Analysis and plotting 
#------------------------------------------------------------------------------
with open('cells/popColors.pkl', 'rb') as fileObj: popColors = pickle.load(fileObj)['popColors']

#cfg.analysis['plotRaster'] = {'include': 'PT5B','timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False, 'popRates': True, 'orderInverse': True, 'popColors': popColors, 'figSize': (12,10), 'lw': 0.3, 'markerSize':3, 'marker': '.', 'dpi': 300}

cfg.analysis['plotTraces'] = {'include': ['PT5B'], 'timeRange': [0, cfg.duration], 'oneFigPer': 'trace', 'figSize': (10,4), 'saveFig': True, 'showFig': True}
#originally 'include': []

#------------------------------------------------------------------------------
# Cells
#------------------------------------------------------------------------------
cfg.cellmod = {'PT5B': 'HH_full'}

cfg.ihModel = 'migliore'  # ih model
cfg.ihGbar = 1.0  # multiplicative factor for ih gbar in PT cells
cfg.ihGbarZD = None # multiplicative factor for ih gbar in PT cells
cfg.ihGbarBasal = 1.0 # 0.1 # multiplicative factor for ih gbar in PT cells
cfg.ihlkc = 0.2 # ih leak param (used in Migliore)
cfg.ihlkcBasal = 1.0
cfg.ihlkcBelowSoma = 0.01
cfg.ihlke = -86  # ih leak param (used in Migliore)
cfg.ihSlope = 14*2

cfg.removeNa = False  # simulate TTX; set gnabar=0s
cfg.somaNa = 5
cfg.dendNa = 0.3
cfg.axonNa = 7
cfg.axonRa = 0.005

cfg.gpas = 0.5  # multiplicative factor for pas g in PT cells
cfg.epas = 0.9  # multiplicative factor for pas e in PT cells

cfg.KgbarFactor = 1.0 # multiplicative factor for K channels gbar in all E cells
cfg.makeKgbarFactorEqualToNewFactor = False

cfg.modifyMechs = {'startTime': 500, 'endTime': 1000, 'cellType':'PT', 'mech': 'hd', 'property': 'gbar', 'newFactor': 1.00, 'origFactor': 0.75}



#------------------------------------------------------------------------------
# Synapses
#------------------------------------------------------------------------------
cfg.synWeightFractionEE = [0.5, 0.5] # E->E AMPA to NMDA ratio
cfg.synWeightFractionEI = [0.5, 0.5] # E->I AMPA to NMDA ratio
cfg.synWeightFractionSOME = [0.9, 0.1] # SOM -> E GABAASlow to GABAB ratio

cfg.synsperconn = {'HH_full': 5, 'HH_reduced': 1, 'HH_simple': 1}
cfg.AMPATau2Factor = 1.0

#------------------------------------------------------------------------------
# Network 
#------------------------------------------------------------------------------
cfg.singleCellPops = True  # Create pops with 1 single cell (to debug)
cfg.weightNorm = 1  # use weight normalization
cfg.weightNormThreshold = 4.0  # weight normalization factor threshold

cfg.addConn = False #1
cfg.scale = 1 #1.0
cfg.sizeY = 1350.0
cfg.sizeX = 300.0
cfg.sizeZ = 300.0
cfg.correctBorderThreshold = 150.0

cfg.L5BrecurrentFactor = 1.0
cfg.ITinterFactor = 1.0
cfg.strengthFactor = 1.0

cfg.EEGain = 0.5
cfg.EIGain = 1.0
cfg.IEGain = 1.0
cfg.IIGain = 1.0

cfg.IEdisynapticBias = None  # increase prob of I->Ey conns if Ex->I and Ex->Ey exist 

#------------------------------------------------------------------------------
## E->I gains
cfg.EPVGain = 1.0
cfg.ESOMGain = 1.0

#------------------------------------------------------------------------------
## I->E gains
cfg.PVEGain = 1.0
cfg.SOMEGain = 1.0

#------------------------------------------------------------------------------
## I->I gains
cfg.PVSOMGain = None #0.25
cfg.SOMPVGain = None #0.25
cfg.PVPVGain = None # 0.75
cfg.SOMSOMGain = None #0.75

#------------------------------------------------------------------------------
## I->E/I layer weights (L2/3+4, L5, L6)
cfg.IEweights = [0.8, 0.8, 1.0]
cfg.IIweights = [1.2, 1.0, 1.0]

cfg.IPTGain = 1.0
cfg.IFullGain = 1.0

#cfg.IClamp1 = {'pop': ['PT5B'], 'sec': 'soma', 'loc': 0.5, 'start': 0, 'dur': 1000, 'amp': 0.50}

#IT5B

#------------------------------------------------------------------------------
# NetStim inputs
#------------------------------------------------------------------------------

 			   ## pop, sec, loc, synMech, start, interval, noise, number, weight, delay 
cfg.NetStim = {'pop': ['PT5B'], 'ynorm':[0,1.0], 'sec': 'soma', 'loc': 0.5, 'synMech': ['AMPA', 'NMDA'], 'synMechWeightFactor': [0.5, 0.5],
				'start': 700, 'interval': 1000, 'noise': 0.0, 'number': 1, 'weight': 30.0, 'delay': 1}

