# Machine Learning Healthcare Bug Repository.

This repository houses a tool for viewing and executing bugs from popular
ML tools and libraries.


## Getting Started

The use of this tool is straigtforward, knowledge of basic Python and Shell scripting is all the 
knowledge needed to make full use of the repository.

### Prerequisites

Listed are the requirements:
- Python 3.10 (https://www.python.org/)
- Conda v4.11.0 (https://docs.conda.io/projects/conda/en/latest/#)

### Installing

1) Download the repository:

   git clone https://github.com/UNF-STLab/MLHCBugs.git

2) Make the main script executable:

  chmod u+x MLHCBugs.py
   

Note: that these requirments are for installing this tool only.
The purpose of this repository is for bug execution and testing thus,
it will install many other repositories upon selection of particular 
bug IDs. 

## Using Target Repositories

As noted this tool will download other repositories as part of the
bug execution process. For this purpose the tool has been designed so that
no other requirements are neccisary.

The main Python script will need to first download selected repositories and 
create a virtual environment using Conda for each repository along with a local copy of
the GitHub repository in a new directory. From here any nessisary dependencies for
the project will be installed to the specific virtual environment, and its bug execution
scripts enabled. Then the script MLHCBugs_Set_ID.py can be used to execute specific bugs.

## Running the tests

To run a test the main Python script takes several arguments all of the same type, the name 
of a repository to test.

1)

  ./MLHCBugs.py breast_cancer_classifier

  This will pull the repository "breast_cancer_classifier" and then create a virtual 
  environment with its dependencies.

2) 

  ./MLHCBugs_Set_ID.py 1
  
  This script will set the repository's commit to where bug ID 1 can be found and then execute 
  it.
  

A list of the repository names an bugs can be found below.

# MLBugs

| Identifier      | Project name               | Number of bugs | Active bug ids      | Deprecated bug ids (\*) |
|-----------------|----------------------------|---------------:|---------------------|-------------------------| 
| BCC             | BCC                        |       1        | 1                   | None                    |
| MZP             | MZP                        |       2        | 2,3                 | None                    |
| RGAN            | RGAN                       |       1        | 4                   | None                    |
| nilearn         | nilearn                    |       11       | 5-15                | None                    |
| lifelines       | lifelines                  |       5        | 16-22               | None                    |
| nipype          | nipype                     |       8        | 23-28               | None                    |
| dipy            | dipy                       |       2        | 29-30               | None                    |



Bug ID description:

1) Input shape.
2) Namespace' object has no attribute 'samples_train'
3) Input shape Dimension error
4) Logic error makes an conditional irrelevant.
5) Transform should never modify object. (issue #71)
6) Open ended if elif allows for dimension error. (issue #162)
7) Variable defined twice evaded coverage. (# 2959)
8) Incorrect/unwanted data modification. (# 325)
9) Colobar code breaks when a map is fully empty (#510)
10) Python int too large to convert to C long (#658)
11) Nilearn resampling doesn't support int16, throws RuntimeError: data type not supported (#817)
12) fetch_atlas_harvard_oxford and symmetric_split (#914)
13) ConnectivityMeasure requires 3D data (#941) 
14) Decoder with ridge_regressor fails on oasis vbm example (#2360)
15) clean function modifies the input time series object if performing pass-filtering without detrending (#2475)
16) Nelson Aalen hazard off by a factor of 1/2 #186
17) Float weights in Kaplan-Meier #418
18) qth_survival_time raising ambiguous truth value error #535
19) Shape mismatch when using conditional_after with strata in CoxPHFitter #880
20) KMF fit fails with tuples #1034
21) Error when setting labels=False in plotting.add_at_risk_counts(). #1097
22) KaplanMeierFitter (interval-censored) issue #1151
23) if hash difference is found, some reported entries are bogus due to list != tuple:
24) Iterables are getting miswired #163
25) Parallel execution of nipype failing #1127
26) Problems hashing inputs derived from encoding in corner cases #1620
27) First Level Bayesian Estimation fails #1786
28) DVARS calculation is incorrect #1821
29) Inconsistent output for values_from_volume #909
30) bundles_distances_mdf asymmetric values #2310


## Versioning


## Authors


## License


## Acknowledgments

