# Web-Image-Processing

Djangoの勉強のために作成したプロジェクトです。

## 概要

今は物体検出を行うことができます。

検出モデルとしてはFaster R-CNNを使用しており、学習済みモデルを利用しています。

![od](./images/od.png)

上記のような手順を踏むと、選んだ画像から物体を検出します。

![od_result](./images/od_result.png)

## 環境設定

FAIRのdetectron2を利用しています。

pipでのインストール方法は[公式ドキュメント](https://detectron2.readthedocs.io/en/latest/tutorials/install.html)を参照してください。

実装時はCPUのみを使用しています。

## To Do

* ページデザイン
* 他の画像処理機能など
  * main.pyにはテスト時に使用していたグレースケール処理も含まれています
  * 一般的な画像処理、cutmixなどのdata augmentationもボタン1つで実行できるように拡張する予定

