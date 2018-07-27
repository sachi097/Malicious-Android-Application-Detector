A new paper titled "Analysis Of Bayesian Classification based Appoarches for Android Malware Detection" has been completly implemented in this module.
Module 3 contains -

readmefile

sourcefiles - folder that contains seven python scripts
             i) dataextsample.py : this script is used to extract permission-based feature of testing samples.
	    ii) dataextper.py : this script is used to extract permission-based feature of both benign and malware samples (The folder name should be changed in the script in order to get .xml of benign and malware.)
           iii) dataextcode.py : this script is used to extract code-based features of both benign and malware samples (The folder name should be changed in the script in order to get .smali file of benign and malware.)
            iv) NBper.py : script uses per.csv as input and classifies the test samples on the basis of permission-based features.
             v) NBcode.py : script uses code.csv as input and classifies the test samples on the basis of code-based features.
            vi) NBmixed.py : script uses mixed.csv as input and classifies the test samples on the basis of mixed(permission and code) features.
	   vii)	driver.py : this script is the driver script that calls NBper.py NBcode.py NBmixed.py by passing commond line arguments 6,11,16,21,25 (no. features) in order to generate output csv files and plots the graph of the result.

screenshots - folder that contains screenshot of the output obtain by executing driver.py
testcases - folder containing xml files of testing samples and 262 samples were used for testing.
per.csv - permission-based feature dataset (includes both malware and benign).
code.csv - code-based feature dataset (includes both malware and benign).
mixed.csv - mixed-features dataset (includes both malware and benign).
