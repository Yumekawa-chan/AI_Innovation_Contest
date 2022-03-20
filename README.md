<img src = "https://user-images.githubusercontent.com/82374688/158964569-50af5ace-3843-4570-b8c0-d982ec26a029.png" width=300px>

[AIイノベーション AWARD 2022](https://www.nttpc.co.jp/innovationlab/event/ai_innovation_award_2022/)に提出したデモプログラムです。

提出テーマ:「人々の幸せ」を生むスマートシティを創ろう

## アプリ説明

「世代間を超えた支えあいで、日本に希望を取り戻す」をコンセプトとした、若者世代層・働き盛り世代層・シニア世代層にWin-Win-Winなマッチングアプリ。
働き盛り世代が自身の親について入力した「年齢・居住地・孤独感・睡眠時間・大まかな貯金額」をAIが分析し、今後3年以内に要介護となる可能性を予測します。

「要介護見込み」と判定された場合、実際に健康状態が悪くなることを回避するために、シニア世代である親（「シニア会員」と呼びます）を定期訪問して、孤独感の軽減に努めてくれる若者（「サポーター会員」と呼びます）を選ぶことができます。
（注：費用の支払主体は、働き盛り世代（「利用者会員」と呼びます）であり、サポートを直接受けるのは、その親である「シニア会員」となります。今回のデモアプリには、契約機能や決済機能は実装しておりません。）


## 使い方

### 起動方法

サーバプログラム（app.py）を起動したうえで http://127.0.0.1:5000/ に接続。

<img src = "https://user-images.githubusercontent.com/82374688/158982175-09f8e2d6-4645-4754-bfa3-09ed30e418d0.png" width=600px>

#### 本アプリケーションはスマホ操作を想定しています。

### トップ画面

<img src = "https://user-images.githubusercontent.com/82374688/158966566-8ab6c713-9833-4fa5-870b-cff4fa8c163f.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158966704-a684a5b7-2d4c-44b6-b855-04394632e0e8.png" width=300px>

本アプリケーションの説明がメインの画面です。新規ユーザーは"今すぐ分析"ボタン、既に会員のユーザーは"ログイン"ボタンを押下し、分析画面に遷移します。

### 調査画面
<img src = "https://user-images.githubusercontent.com/82374688/158969566-691170df-6220-4920-ab10-4f9bfb57768c.png" width=300px>

分析対象となるシニアユーザーの情報を入力します。空欄なく入力が完了したら、"完了！"ボタンを押下して入力を送信します。

### 分析結果画面
<img src = "https://user-images.githubusercontent.com/82374688/158974278-1836f681-ac02-44d6-96bd-a6dc884e5937.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158974382-7e174d20-815f-4625-bd11-a61321504ac9.png" width=300px>

調査画面の入力情報を基にAIが分析し、今後3年以内の必要性を分析します。必要だった場合はその確率が表示され、新規登録を促されます。

### 新規登録・ログイン画面
<img src = "https://user-images.githubusercontent.com/82374688/158975093-32ce2f69-a568-4955-a91a-6d27ab935fee.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158975257-fd3943d2-28a7-42c1-8b5e-f06bf03fd6b8.png" width=300px>

新規登録画面では登録したいユーザー名とパスワードを入力します。今回はどちらも文字数や使用文字の指定はございません。

ログイン画面では登録した情報を入力します。

### ユーザー画面
<img src = "https://user-images.githubusercontent.com/82374688/158976266-a3154ea2-e32b-430f-ba7e-4bea7df5a1cd.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158976404-09077093-469d-4229-a6ed-f3c63269ebf2.png" width=300px>

マッチングをメインに行う画面です。「～現在のマッチ候補～」に表示されているサポーターに「いいかも！」をすると、「～いいかも！をした人～」にそのサポーターが表示されます。"解除"ボタンを押下すると、そのサポーターの情報はユーザー画面から削除されます。"ログアウト"ボタンを押下すると、トップ画面に遷移します。

### 管理者画面
<img src = "https://user-images.githubusercontent.com/82374688/158977147-3f80118b-c288-4486-8ce1-bebbb1eed7ed.png" width=300px>
デモプログラム限定の通常のボタン操作ではたどり着くことができない画面です。（http://127.0.0.1:5000/admin）　

ユーザー画面で表示されるサポーターを追加します。

写真は./app/static/images/peopleフォルダーのjpg方式で保存された画像名を入力します。

## データ分析
調査画面で入力した情報は機械学習の手法である「RandomForest」によって学習・テストされたdataset.csvを基に分析されています。

要介護見込み画面で表示されている確率は、datasetの独立した項目を4つ選別し、それぞれに重みを付けて計算されています。

## 環境
本アプリケーションはFlaskを利用しています。そのため、起動にはPythonのインストールと以下のモジュールが必要です。

`flask flask-sqlalchemy flask-bootstrap flask-login`

## 文責

* 制作チーム 鈴木総合研究所
* 所属 東京電機大学,立教大学大学院

<img src = "https://user-images.githubusercontent.com/82374688/158979845-af480279-380e-474f-8cd5-ddd19241154d.png" width=400px>

