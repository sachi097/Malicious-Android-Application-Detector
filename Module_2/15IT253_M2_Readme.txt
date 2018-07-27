The second phase of the paper has been implemented in module 2.
Module 2 contains -
readmefile
sourcefile - folder that contains three python scripts
             i) sampledataext.py : this script is used to extract .smali file of testing samples.
	    ii) dataext.py : this file is used to extract .smali file of both benign and malware samples (The folder name should be changed in the script in order to get .smali file of benign and malware.)
           iii) NBrun.py : this script is the driver script that uses dataset of benign and malware samples in order to train NB and uses dataset of testing samples for testing.
screenshot - folder that contains screenshot of the output obtain by executing NBrun.py
testcases - folder containing xml files of testing samples and 143 samples were used for testing.
NBinput.csv - dataset of benign and malware.
NBinputsam.csv - dataset of testing sample.
Decision_Module.csv - output of phase one.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The module two has 90% accuracy.
out of 143 samples - benign : 85 , malware : 58
module two has classified : benign : 77 , malware : 51 , missclassied : 15
