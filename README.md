# FACE MASK DETECTION SYSTEM

<h3>
    <strong> Problem description </strong>
</h3>
<p>
    Design and implement a system to detect and classify the wearing of mask in three classes:
</p>
<br>
<p align="center">
    <img src="https://drive.google.com/uc?id=1qv32VDRpnure0sSeLEDf5ugYZzYbu_y6">
</p> 
<br>

<h3>
    <strong> Dataset </strong>
</h3>
    <p>
    Dataset is available in this <a href="https://drive.google.com/drive/folders/1gJ8_0LJZj9VtRBueUF0ZXPLFhgEaiCe6?usp=sharing"><strong><i> Drive folder </i></strong></a>, this was created from others publics dataset:
    <ul>
      <li><a href="https://github.com/balajisrinivas/Face-Mask-Detection/tree/master/dataset"><strong><i> Dataset 1 </i></strong></a></li>
      <li><a href="https://github.com/cabani/MaskedFace-Net"><strong><i> Dataset 2 </i></strong></a></li>
    </ul>
</p>
<br>

<i> Developep by: </i> <br>
<p align="center">
- <strong> Jhon Hader Fernández </strong> <br>
- <strong> Diego Fernando Díaz </strong> <br>
- <strong> Oscar Geovanny Baracaldo </strong> <br>
</p>
<br>

---
---
<br>

<p align="center">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg"><br>
    <img src="https://img.shields.io/badge/Trained in-Google Colab-magenta.svg">
    <img src="https://img.shields.io/badge/On device-GPU-green.svg">
</p>

<h3>
    <strong> Virtual environment </strong>
</h3>
<p>
    We use <a href="https://colab.research.google.com/notebooks/welcome.ipynb?hl=es-419"><strong><i> Google Colab </i></strong></a> to train our model, we did it because <strong> Colab </strong> offers us GPU for free, in this way we can accelerate the model training.
</p>
<br>

<h3>
    <strong> Data balance </strong>
</h3>
<p>
    It's important know the data balance, to see the distribution of data, in this way we can't avoid possible overfitting, for example, if some class have more data than others the model will be trained for recognize that class.
</p>
<br>
<p align="center">
    <img src="https://drive.google.com/uc?id=1hDNa-MczwvL2vrJLw86pgzPeEcohyeRx">
</p> <br>

<h3>
    <strong> Model solution </strong>
</h3>
<p>
    Our base model is <a href="https://arxiv.org/pdf/1801.04381.pdf"><strong><i> MobileNetV2 </i></strong></a>, after we added layers. The following is out architure:
</p>
<p align="center">
    <img src="https://drive.google.com/uc?id=1ALPJrPRSN2MAFT9lnYl6ta7IjrogfjI2">
</p> 
<br>
<p align="center">
    <img src="https://drive.google.com/uc?id=1ynTxSdnK3veuN8KM9JviGho5br9_15VW">
</p> <br>

<h3>
    <strong> Results </strong>
</h3>
<p>
    Performance of model was:
</p>
<p align="center">
    <img src="https://drive.google.com/uc?id=1Jl9s0_CabLbZZUYJ954xfq5KcvbiSzkY">
</p> <br>
