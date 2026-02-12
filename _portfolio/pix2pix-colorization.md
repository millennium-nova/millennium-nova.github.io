---
title: "Image Coloring GAN"
excerpt: "pix2pix (GAN) による画像の自動着色.<br><br>  <img src='/images/portfolio/pix2pix-colorization.png' alt='pix2pix colorization' style='width: 600px; height: auto;'> "
date: 2023-08-31
collection: portfolio
---

- 取り組んだ期間: 4ヶ月弱
- 使用技術
    - Python, PyTorch, pix2pix (GAN)
- 内容
    - image-to-image タスクで高い性能を発揮していた GAN ベースの pix2pix を用いて、白黒画像の自動着色モデルを学習した。<br> 
    - Kaggle で公開されている[風景画像のデータセット](https://www.kaggle.com/datasets/arnaud58/landscape-pictures)をグレースケール化して 4,300枚ほどのデータセットを作成し、訓練用、検証用、評価テスト用データに 8:1:1 で分割して使用した。

<img src='/images/portfolio/pix2pix-colorization.png' alt='pix2pix colorization' style='width: 600px; height: auto;'><br>
実験に使ったコードなどは [こちらのリポジトリ](https://github.com/millennium-nova/pix2pix-colorization/)にあります。<br>



