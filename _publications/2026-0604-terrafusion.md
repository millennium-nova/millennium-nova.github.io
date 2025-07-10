---
title: "TerraFusion: Joint Generation of Terrain Geometry and Texture Using Latent Diffusion Models"
collection: publications
category: manuscripts
authors: Kazuki Higo, Toshiki Kanai, Yuki Endo, Yoshihiro Kanamori
permalink: /publication/2025-06-04-terrafusion
excerpt: '*Virtual Reality & Intelligent Hardware (Proc. of Computer Graphics International 2025), Vol. , No. , pp. -, 2025*'
date: 2025-06-04
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
# paperurl: 'https://arxiv.org/pdf/2505.04050'
links:
  - label: "[Project]"
    url:  https://millennium-nova.github.io/terra-fusion-page/
  - label: "[Paper]"
    url:  https://arxiv.org/abs/2505.04050
  - label: "[Code]"
    url:  https://github.com/millennium-nova/terra-fusion
  - label: "[Dataset]"
    url:  https://huggingface.co/datasets/millennium-nova/
share: false
# bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
# citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
# title: "Paper Title Number 1"
# collection: publications
# category: manuscripts
# permalink: /publication/2009-10-01-paper-title-number-1
# excerpt: 'This paper is about the number 1.'
# date: 2025-01-01
# venue: 'Journal Name'
# # slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
# paperurl: 'http://academicpages.github.io/files/paper1.pdf'
# # bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
# # citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---
<img src="../images/terra-fusion/teaser.png" alt="TerraFusionのティーザ画像" width="750" height="500"><br>
3D terrain models are essential in fields such as video game development and film production. Since surface color often correlates with terrain geometry, capturing this relationship is crucial to achieving realism. However, most existing methods generate either a heightmap or a texture, without sufficiently accounting for the inherent correlation. Methods In this paper, we propose a method that jointly generates terrain heightmaps and textures using a latent diffusion model. First, we train the model in an unsupervised manner to randomly generate paired heightmaps and textures. Then, we perform supervised learning of an external adapter to enable user control via hand-drawn sketches. Results Experiments show that our approach allows intuitive terrain generation while preserving the correlation between heightmaps and textures.
<!-- これらの内容は、公開論文のリストの一部として表示されます。ユーザーが論文のリンクをクリックすると、このセクションの内容が1ページ全体として表示され、読者に論文の詳細情報を提供することができます。公開論文が単一ページとして表示される場合、上記の「citation」フィールドの内容がこのセクションの下部に小さいフォントで自動的に含まれます。 -->