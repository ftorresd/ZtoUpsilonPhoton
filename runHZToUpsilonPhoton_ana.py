#!/usr/bin/env python

import os
import fileinput
import sys
from ROOT import *
# from array import array
from multiprocessing import Pool 

mcORdata = sys.argv[1]
sampleName = sys.argv[2]
shapeSystMask = sys.argv[3]


gROOT.SetBatch(True) # set ROOT to batch mode, this suppresses printing canvases
gSystem.AddIncludePath("-Iexternal");
gSystem.SetBuildDir("tmpdir", kTRUE);
gStyle.SetOptStat(0);
gROOT.ProcessLine(".L plugins/getFilesList.C+"); 
gROOT.ProcessLine(".L plugins/makeMuonsRands.C+"); 




filesData_MuOnia = [
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016B.txt", "Run2016B"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016C.txt", "Run2016C"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016D.txt", "Run2016D"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016E.txt", "Run2016E"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016F.txt", "Run2016F"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016G.txt", "Run2016G"],
	["filesLists/filesListsOniaTriggers/fromEOS/MuOnia_Run2016H.txt", "Run2016H"],
	]


filesMC_MuOnia = [
	["filesLists/filesListsOniaTriggers/fromEOS/MC_HToJPsiGamma.txt", "HToJPsiGamma", "puWeight/pu_HToJPsiGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_HToUpsilon1SGamma.txt", "HToUpsilon1SGamma", "puWeight/pu_HToUpsilon1SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_HToUpsilon2SGamma.txt", "HToUpsilon2SGamma", "puWeight/pu_HToUpsilon2SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_HToUpsilon3SGamma.txt", "HToUpsilon3SGamma", "puWeight/pu_HToUpsilon3SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_ZGTo2MuG_MMuMu-2To15.txt", "ZGTo2MuG_MMuMu-2To15", "puWeight/pu_ZGTo2MuG_MMuMu-2To15_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_ZToJPsiGamma.txt", "ZToJPsiGamma", "puWeight/pu_ZToJPsiGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_ZToUpsilon1SGamma.txt", "ZToUpsilon1SGamma", "puWeight/pu_ZToUpsilon1SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_ZToUpsilon2SGamma.txt", "ZToUpsilon2SGamma", "puWeight/pu_ZToUpsilon2SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_ZToUpsilon3SGamma.txt", "ZToUpsilon3SGamma", "puWeight/pu_ZToUpsilon3SGamma_MuOniaTriggers.root"],
	["filesLists/filesListsOniaTriggers/fromEOS/MC_HDalitz.txt", "HDalitz", "puWeight/pu_HDalitz_MuOniaTriggers.root"],
	]

filesData_MuonEG = [
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016B_FebReminiAOD.txt", "Run2016B"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016C_FebReminiAOD.txt", "Run2016C"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016D_FebReminiAOD.txt", "Run2016D"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016E_FebReminiAOD.txt", "Run2016E"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016F_FebReminiAOD1.txt", "Run2016F1"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016F_FebReminiAOD2.txt", "Run2016F2"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016G_SepRereco.txt", "Run2016G"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016H_PRv2.txt", "Run2016H2"],
	["filesLists/filesFromUERJPOWER/Data2016/job_MuEG_Run2016H_PRv3.txt", "Run2016H3"],
	]


filesMC_MuonEG = [
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon1SGamma.txt", "ZToUpsilon1SGamma", "puWeight/pu_ZToUpsilon1SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon2SGamma.txt", "ZToUpsilon2SGamma", "puWeight/pu_ZToUpsilon2SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon3SGamma.txt", "ZToUpsilon3SGamma", "puWeight/pu_ZToUpsilon3SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToJPsiGamma.txt", "ZToJPsiGamma", "puWeight/pu_ZToJPsiGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon1SGamma.txt", "HToUpsilon1SGamma", "puWeight/pu_HToUpsilon1SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon2SGamma.txt", "HToUpsilon2SGamma", "puWeight/pu_HToUpsilon2SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon3SGamma.txt", "HToUpsilon3SGamma", "puWeight/pu_HToUpsilon3SGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToJPsiGamma.txt", "HToJPsiGamma", "puWeight/pu_HToJPsiGamma.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HDalitz.txt", "HDalitz", "puWeight/pu_HDalitz.root"],
	["filesLists/filesFromUERJPOWER/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZGTo2MuG_MMuMu-2To15.txt", "ZGTo2MuG_MMuMu-2To15", "puWeight/pu_ZGTo2MuG_MMuMu-2To15.root"],
	]


filesData_MuonEG_fromEOS = [
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD.txt", "Run2016B"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD.txt", "Run2016C"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD.txt", "Run2016D"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD.txt", "Run2016E"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1.txt", "Run2016F1"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2.txt", "Run2016F2"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco.txt", "Run2016G"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2.txt", "Run2016H2"],
	# ["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3.txt", "Run2016H3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_0.txt", "Run2016B_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_1.txt", "Run2016B_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_2.txt", "Run2016B_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_3.txt", "Run2016B_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_4.txt", "Run2016B_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_5.txt", "Run2016B_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_6.txt", "Run2016B_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_7.txt", "Run2016B_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_8.txt", "Run2016B_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016B_FebReminiAOD_9.txt", "Run2016B_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_0.txt", "Run2016C_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_1.txt", "Run2016C_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_2.txt", "Run2016C_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_3.txt", "Run2016C_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_4.txt", "Run2016C_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_5.txt", "Run2016C_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_6.txt", "Run2016C_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_7.txt", "Run2016C_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_8.txt", "Run2016C_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016C_FebReminiAOD_9.txt", "Run2016C_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_0.txt", "Run2016D_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_1.txt", "Run2016D_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_2.txt", "Run2016D_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_3.txt", "Run2016D_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_4.txt", "Run2016D_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_5.txt", "Run2016D_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_6.txt", "Run2016D_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_7.txt", "Run2016D_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_8.txt", "Run2016D_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016D_FebReminiAOD_9.txt", "Run2016D_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_0.txt", "Run2016E_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_1.txt", "Run2016E_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_2.txt", "Run2016E_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_3.txt", "Run2016E_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_4.txt", "Run2016E_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_5.txt", "Run2016E_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_6.txt", "Run2016E_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_7.txt", "Run2016E_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_8.txt", "Run2016E_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016E_FebReminiAOD_9.txt", "Run2016E_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_0.txt", "Run2016F1_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_1.txt", "Run2016F1_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_2.txt", "Run2016F1_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_3.txt", "Run2016F1_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_4.txt", "Run2016F1_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_5.txt", "Run2016F1_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_6.txt", "Run2016F1_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_7.txt", "Run2016F1_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_8.txt", "Run2016F1_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD1_9.txt", "Run2016F1_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_0.txt", "Run2016F2_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_1.txt", "Run2016F2_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_2.txt", "Run2016F2_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_3.txt", "Run2016F2_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_4.txt", "Run2016F2_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_5.txt", "Run2016F2_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_6.txt", "Run2016F2_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_7.txt", "Run2016F2_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_8.txt", "Run2016F2_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016F_FebReminiAOD2_9.txt", "Run2016F2_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_0.txt", "Run2016G_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_1.txt", "Run2016G_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_2.txt", "Run2016G_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_3.txt", "Run2016G_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_4.txt", "Run2016G_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_5.txt", "Run2016G_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_6.txt", "Run2016G_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_7.txt", "Run2016G_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_8.txt", "Run2016G_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016G_SepRereco_9.txt", "Run2016G_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_0.txt", "Run2016H2_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_1.txt", "Run2016H2_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_2.txt", "Run2016H2_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_3.txt", "Run2016H2_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_4.txt", "Run2016H2_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_5.txt", "Run2016H2_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_6.txt", "Run2016H2_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_7.txt", "Run2016H2_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_8.txt", "Run2016H2_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv2_9.txt", "Run2016H2_9"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_0.txt", "Run2016H3_0"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_1.txt", "Run2016H3_1"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_2.txt", "Run2016H3_2"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_3.txt", "Run2016H3_3"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_4.txt", "Run2016H3_4"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_5.txt", "Run2016H3_5"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_6.txt", "Run2016H3_6"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_7.txt", "Run2016H3_7"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_8.txt", "Run2016H3_8"],
	["filesLists/filesFromEOS/Data2016/job_MuEG_Run2016H_PRv3_9.txt", "Run2016H3_9"],
]

filesMC_MuonEG_fromEOS_OLD = [
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon1SGamma.txt", "ZToUpsilon1SGamma", "puWeight/pu_ZToUpsilon1SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon2SGamma.txt", "ZToUpsilon2SGamma", "puWeight/pu_ZToUpsilon2SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToUpsilon3SGamma.txt", "ZToUpsilon3SGamma", "puWeight/pu_ZToUpsilon3SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZToJPsiGamma.txt", "ZToJPsiGamma", "puWeight/pu_ZToJPsiGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon1SGamma.txt", "HToUpsilon1SGamma", "puWeight/pu_HToUpsilon1SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon2SGamma.txt", "HToUpsilon2SGamma", "puWeight/pu_HToUpsilon2SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToUpsilon3SGamma.txt", "HToUpsilon3SGamma", "puWeight/pu_HToUpsilon3SGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HToJPsiGamma.txt", "HToJPsiGamma", "puWeight/pu_HToJPsiGamma.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/HDalitz.txt", "HDalitz", "puWeight/pu_HDalitz.root"],
	["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning/ZGTo2MuG_MMuMu-2To15.txt", "ZGTo2MuG_MMuMu-2To15", "puWeight/pu_ZGTo2MuG_MMuMu-2To15.root"],
	]

filesMC_MuonEG_fromEOS = [
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ttH_HToUps3SG_NLO.txt", "ttH_HToUps3SG_NLO", "puWeight/pu_ttH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ttH_HToUps2SG_NLO.txt", "ttH_HToUps2SG_NLO", "puWeight/pu_ttH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ttH_HToUps1SG_NLO.txt", "ttH_HToUps1SG_NLO", "puWeight/pu_ttH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ggH_HToUps3SG_NLO.txt", "ggH_HToUps3SG_NLO", "puWeight/pu_ggH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ggH_HToUps2SG_NLO.txt", "ggH_HToUps2SG_NLO", "puWeight/pu_ggH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ggH_HToUps1SG_NLO.txt", "ggH_HToUps1SG_NLO", "puWeight/pu_ggH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZToUpsilon3SGamma_NLO.txt", "ZToUpsilon3SGamma_NLO", "puWeight/pu_ZToUpsilon3SGamma_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZToUpsilon2SGamma_NLO.txt", "ZToUpsilon2SGamma_NLO", "puWeight/pu_ZToUpsilon2SGamma_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZToUpsilon1SGamma_NLO.txt", "ZToUpsilon1SGamma_NLO", "puWeight/pu_ZToUpsilon1SGamma_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZH_HToUps3SG_NLO.txt", "ZH_HToUps3SG_NLO", "puWeight/pu_ZH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZH_HToUps2SG_NLO.txt", "ZH_HToUps2SG_NLO", "puWeight/pu_ZH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZH_HToUps1SG_NLO.txt", "ZH_HToUps1SG_NLO", "puWeight/pu_ZH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/ZGTo2MuG_MMuMu-2To15.txt", "ZGTo2MuG_MMuMu-2To15", "puWeight/pu_ZGTo2MuG_MMuMu-2To15.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WpH_HToUps3SG_NLO.txt", "WpH_HToUps3SG_NLO", "puWeight/pu_WpH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WpH_HToUps2SG_NLO.txt", "WpH_HToUps2SG_NLO", "puWeight/pu_WpH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WpH_HToUps1SG_NLO.txt", "WpH_HToUps1SG_NLO", "puWeight/pu_WpH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WmH_HToUps3SG_NLO.txt", "WmH_HToUps3SG_NLO", "puWeight/pu_WmH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WmH_HToUps2SG_NLO.txt", "WmH_HToUps2SG_NLO", "puWeight/pu_WmH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/WmH_HToUps1SG_NLO.txt", "WmH_HToUps1SG_NLO", "puWeight/pu_WmH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/VBFH_HToUps3SG_NLO.txt", "VBFH_HToUps3SG_NLO", "puWeight/pu_VBFH_HToUps3SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/VBFH_HToUps2SG_NLO.txt", "VBFH_HToUps2SG_NLO", "puWeight/pu_VBFH_HToUps2SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/VBFH_HToUps1SG_NLO.txt", "VBFH_HToUps1SG_NLO", "puWeight/pu_VBFH_HToUps1SG_NLO.root"],
						["filesLists/filesFromEOS/HZtoUpsilonPlusPhotonSamples2016_withGhostCleanning_NLO/HDalitzNLO.txt", "HDalitzNLO", "puWeight/pu_HDalitzNLO.root"],
					]



# clean up
os.system("rm -rf outputFiles/*")
os.system("rm -rf data/muonsRands/muonsRands_R*.root")





for line in fileinput.input("ana_ZtoUpsilonPhoton.C", inplace = 1):
	print line.replace("//#define IS_MC 1", "#define IS_MC 1"),


gROOT.ProcessLine(".L ana_ZtoUpsilonPhoton.C+");

def doMakeMuonsRands(filesList):
	listVec = vector('string')()
	with open(filesList[0], 'r') as listOfFiles:
		for l in listOfFiles:
			listVec.push_back(l.rstrip())
	makeMuonsRands(listVec, filesList[1]);

def runAnaMC(file):
	ana_ZtoUpsilonPhoton(getFilesList(file[0]), -1, file[1], True, file[2], shapeSystMask);



# # make random numbers for muon Rocherter Corrections
# poolRand = Pool(10) 
# resultsRand = poolRand.map(doMakeMuonsRands, filesMC_MuonEG)
# # resultsRand = poolRand.map(doMakeMuonsRands, filesMC_MuOnia)
# poolRand.close() 
# poolRand.join()
# # map(doMakeMuonsRands, filesMC_MuonEG)

# # run de analysis
# poolAna = Pool(10) 
# resultsAna = poolAna.map(runAnaMC, filesMC_MuonEG)
# # resultsAna = poolAna.map(runAnaMC, filesMC_MuOnia)
# poolAna.close() 
# poolAna.join()
# # map(runAnaMC, filesMC_MuonEG)


if (mcORdata == "MC"):
	# print "\n"*50
	# print "making Rocherter random number..."
	# doMakeMuonsRands(filter(lambda x: x[1] == sampleName, filesMC_MuonEG_fromEOS)[0])
	print "\n"*15
	print "running over events..."
	runAnaMC(filter(lambda x: x[1] == sampleName, filesMC_MuonEG_fromEOS)[0])

gROOT.ProcessLine(".U ana_ZtoUpsilonPhoton.C"); 


for line in fileinput.input("ana_ZtoUpsilonPhoton.C", inplace = 1):
	print line.replace("#define IS_MC 1", "//#define IS_MC 1"),

gROOT.ProcessLine(".L ana_ZtoUpsilonPhoton.C+");


def runAnaData(file):
	ana_ZtoUpsilonPhoton(getFilesList(file[0]), -1, file[1]);


# # make random numbers for muon Rocherter Corrections
# poolRandData = Pool(9) 
# resultsRandData = poolRandData.map(doMakeMuonsRands, filesData_MuonEG)
# poolRandData.close() 
# poolRandData.join()
# # map(doMakeMuonsRands, filesData_MuonEG)

# pool = Pool(9) 
# results = pool.map(runAnaData, filesData_MuonEG)
# pool.close() 
# pool.join()
# # map(runAnaData, filesData_MuonEG)

if (mcORdata == "Data"):
	print "\n"*15
	print "generating Rocherter random number..."
	doMakeMuonsRands(filter(lambda x: x[1] == sampleName, filesData_MuonEG_fromEOS)[0])
	print "\n"*15
	print "running over events..."
	runAnaData(filter(lambda x: x[1] == sampleName, filesData_MuonEG_fromEOS)[0])


for line in fileinput.input("ana_ZtoUpsilonPhoton.C", inplace = 1):
	print line.replace("//#define IS_MC 1", "#define IS_MC 1"),


