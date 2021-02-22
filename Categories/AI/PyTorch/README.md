# PyTorch

Deep learning framework for fast, flexible experimentation

## Common Activation Functions

1. ReLU: Rectified Linear Unit, ReLU(x) = max(0,x)
2. logit: SoftMax, SoftMax(x) = 0 ~ 1, probability, multi-class classification eg: handwritten digits from 0~9
3. tanh
4. step

## NumPy-like functionality

1. slicing
2. indexing
3. reductions
4. linear algebra
5. vector and matrix operations

## machine learning on the cloud

1. Data Preparation
2. Model Development
3. Model Training and Evaluation - distributed manner - mixing with cloud platform and ML framework
   1. developer configuring training and hyperparameter tuning
   2. cloud platform + ML framework will perform distributed training and hyperparameter tuning
4. Deployment
5. Prediction
6. Managing Versions

## Installation & Setup

1. activate conda/python for certain shells
   - > conda init bash/powershell/zsh/cmd.exe
   - > python --version
   - > jupyter --version
   - > pip --version
2. please refer to Leo.Cognizant.Test to see how to speed up downloading and package installing for pip install & conda install
3. [install pytorch](https://pytorch.org/get-started/locally/)
   - > conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
4. install jupyter notebook and config
   - > conda install jupyter notebook
   - > jupyter-notebook --generate-config
   - > jupyter notebook password
   - > jupyter notebook --notebook-dir=/?? --no-browser --port=???? --ip=???.?.?.? --allow-root
5. > conda install graphviz
6. > pip install hiddenlayer