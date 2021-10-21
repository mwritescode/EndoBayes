![Pgmpy](https://img.shields.io/badge/pgmpy-blue?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAQlBMVEUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAEhIAEREAEBAADw8AFRUTJi%2F%2F%2F%2F8e1%2BJgAAAAFXRSTlMAAQIDBAUGBwgJCgsMDQ4ODxARGBvLk5n3AAABJElEQVR42tzUB26FMBAEUHrvMPc%2Faoq1iF00i1Gi%2BicV7Ofun3xcQNMApVRo0VNCosvvpA8vHWI97%2BUfJH0m672DXCp5ZDZzDH%2BvSqt0%2BT657YMnxW8aeQL4TvLFKH2hTKiJ3yzhtS%2BQOet9pC6BerjgKu8pqdRhgolvMJwLoXZ1wMZMbZo285FG%2FBQAlkB0xwsWn9Qoflts8Jv6VTf3cYkRkjEMYPcJQAyAgpAWEk46LYTMmHBmonOxIjzr4hjZwsoj8YPpImfriBAVddvSRzJqwjsh3VTVTWQvLr33yFMCvT4hXNgssImLXj4qclm%2BLtZ%2BktmjXCzIgdiWsNfDowB9%2FQeSPhK8JalP4gNbyfstPhed1l3khhMea77HQBpgYhjaAAAoyENG1fAVVgAAAABJRU5ErkJggg%3D%3D)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)

# EndoBayes <img width="40" alt="lungs icon" src="https://github.com/mwritescode/endobayes/blob/main/figures/endo_ribbon.png">
Endometriosis is a condition where tissue similar to the lining of the uterus is found elsewhere in the body. This causes a chronic inflammatory reaction that may result in the formation of scar tissue within the pelvis and other parts if the body. According to World Health Organization (WHO), about 10% of women of reproductive age are affected by endometriosis, which currently means around 190 million people. However, the general public still has got limited awareness of this condition, which is also, due to its variable and broad symptoms, very much under-diagnosed.

This work explores the possibility of making use of new computational models - in particular, bayesian belief networks - to aid medical specialists in diagnosing Endometriosis and to spread awareness thoughout the community. A small bayesian network, including common risk factors, symptoms and comorbidities for the condition of interest, is shown, followed by an analysis of the network structure an a couple of different example diagnosis. The implementation makes use of the pgmpy library, which provides a pure python implementation for bayesian networks while focusing on modularity and extensibility.

### Dataset
All the data used in this work was collected last year by Shani Cohen, a computer science student at Ariel University (Israel) who was kind enough to let me access and use it. She collected information regarding the occourrence of 50 common Endometriosis symptoms/comorbidities in both healthy people and in individuals affected by the interested condition. Her dataset was originally intended for a deep learning project aiming to diagnose Endometriosis, which can be found [here](https://github.com/shani-co/-Deeplearning-Endo).

### Network
The final proposed network is depicted in the following image and it has been analyzed in terms of independences, markov blankets and active trails. <br>
<center> <img alt="Final Proposed Network" src="https://github.com/mwritescode/endobayes/blob/main/figures/final_network.png"> </center>

After the analysis, the network has been used to solve two simple case studies, namely:
* Finding the probability that a patient has Endometriosis, kowing that they have feel pain during intercourse, are bloated and have a family history of endometriosis, but they do not have neither IBS nor painful periods. This was solved through exact inference using Variable Elimination
* Finding how likely it is for a patient to also have IBS when they have Endometriosis and suffer from nausea, bloating and ovarian cysts. This was solved through approximate inference, using Gibbs Sampling.

### Reproducing the results
The whole code can be found in the [EndoBayes](https://github.com/mwritescode/endobayes/blob/main/src/EndoBayes.ipynb) notebook and can be easily reproduced by cloning the repository and running this code.
