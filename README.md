# Learn Machine Learning
Refer the end sections to know about how to clone the repository and some pre-requisite knowledge    

## Competition Details
Title: Lyft Motion Prediction for Autonomous Vehicles  
URL: https://www.kaggle.com/c/lyft-motion-prediction-autonomous-vehicles  


## Setup Dataset  
1. Install the kaggle API  
- $pip install kaggle  
(**Prerequisite Installations** : Python 3.0+ and Pip20+)  
- $pip list  
(You should see kaggle in the list, if above step is successful)  


2. Download the API key file from your kaggle account  
- Go to account under kaggle.com/<username>/account  
- Go to API section and _Create New API Token_
- This will download kaggle.json file in your machine  


3. Create .kaggle folder inside %USERPROFILE% and copy the kaggle.json get in above step  
$cd %USERPROFILE%/.kaggle/kaggle.json  
(The json file will have your username and the api key )

4. Add the kaggle path to the environment variable  
(You can find the path by seeing where kaggle is installed using following command)  
- $pip uninstall kaggle  
(Press no(n/N) to cancel uninstall)  
- $kaggle -v  
(reopen your terminal and check the kaggle command is available)
- $kaggle competitions list  
(This will list all the competitiona, just to reconfirm if the API is working)  

5. Run the following command to start downloading the data  
$kaggle competitions download -c lyft-motion-prediction-autonomous-vehicles  


## Learn some pre-requisite
Learn basics Python from folder named _basics-python_ which includes simple python structs worth knowing   
Learn basic Tensorflow from folder named _basics-tensorflow_ which includes know-hows about tensorflow api  


## Code Repository
1. Clone the repository as: _$git clone https://github.com/om-ganesh/learn-ml.git_  
2. Create your working branch from master  
3. After work done, make PR to merge the code to _master_ (We can't push code directly to master without review)
4. During merging, use **Squash and Merge** option to consolidate all changes
