<img src = "https://user-images.githubusercontent.com/82374688/158964569-50af5ace-3843-4570-b8c0-d982ec26a029.png" width=300px>

[AIイノベーション AWARD 2022](https://www.nttpc.co.jp/innovationlab/event/ai_innovation_award_2022/)に提出したデモプログラムです。

提出テーマ:「人々の幸せ」を生むスマートシティを創ろう

## アプリ説明

「世代間を超えた支えあいで、日本に希望を取り戻す」をコンセプトとした、若者世代・働き盛り世代・シニア世代にWin-Win-Winなマッチングアプリ。
働き盛り世代が自身の親について入力した「年齢・居住地・孤独感・睡眠時間・大まかな貯金額」をAIが分析し、今後2年以内に要介護となる可能性を予測します。

「要介護見込み」と判定された場合、実際に健康状態が悪くなることを回避するために、シニア世代である親（「シニア会員」と呼びます）を定期訪問して、孤独感の軽減に努めてくれる若者（「サポーター会員」と呼びます）を選ぶことができます。

（注：費用の支払主体は、働き盛り世代（「利用者会員」と呼びます）であり、サポートを直接受けるのは、その親である「シニア会員」となります。今回のデモアプリには、契約機能や決済機能は実装しておりません。）


## 使い方

### 起動方法

サーバプログラム（app.py）を起動したうえで http://127.0.0.1:5000/ に接続。

<img src = "https://user-images.githubusercontent.com/82374688/158982175-09f8e2d6-4645-4754-bfa3-09ed30e418d0.png" width=600px>

#### 本アプリケーションはスマホ操作を想定しています。

### トップ画面

<img src = "https://user-images.githubusercontent.com/82374688/160223286-9d16771c-ec51-47b0-803e-4a68bca43f86.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/160223260-a926c80a-c5b9-4a05-ab39-becf40e6d19f.png" width=300px>

本アプリケーションの説明がメインの画面です。新規ユーザーは"今すぐ分析"ボタン、登録済みの利用会員は"ログイン"ボタンを押下し、分析画面に遷移します。

### 調査画面
<img src = "https://user-images.githubusercontent.com/82374688/160223309-6764b7d5-2d15-410e-9889-82636911a843.png" width=300px>

分析対象となるシニアユーザーの情報を入力します。空欄なく入力が完了したら、"完了！"ボタンを押下して入力を送信します。

### 分析結果画面
<img src = "https://user-images.githubusercontent.com/82374688/160536138-11c15d9e-9498-4917-95e2-9bcc425c471b.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/160536191-6591ef38-fdc7-49b8-a5ea-435cdab5c760.png" width=300px>



調査画面に入力された情報を基にAIが分析し、今後2年以内に介護が必要となる見込みの有無を判別します。「要介護見込み」と判定された場合は、その確率が表示され、新規登録を促されます。

### 新規登録・ログイン画面
<img src = "https://user-images.githubusercontent.com/82374688/160223366-0038e63c-e714-449c-a913-4a52b5eb34ce.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/160223370-e4f72dee-5ffa-4b1b-b473-9db32c4e7ef8.png" width=300px>

新規登録画面では登録したいユーザー名とパスワードを入力します。今回はどちらも文字数や使用文字の指定はございません。

ログイン画面では登録した情報を入力します。

### ユーザー画面
<img src = "https://user-images.githubusercontent.com/82374688/160223563-678c88ac-c7e0-44b2-8d5e-56ca057775f3.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/160223507-e64dc500-df54-4aae-abd1-c67fee1d8e91.png" width=300px>

マッチングをメインに行う画面です。「～現在のマッチ候補:親御様のサポートを依頼しますか？～」に表示されているサポーター会員に「依頼する！」を押下すると、「～依頼する！をした人～」にそのサポーター会員が表示されます。"解除"ボタンを押下すると、そのサポーター会員の情報はユーザー画面から削除されます。"ログアウト"ボタンを押下すると、トップ画面に遷移します。

( 注：実際の運用においては、「依頼する！」が押下されたあとに、運営側にてシニア会員とサポーター会員の双方に連絡を行い、両者の同意を得た上で、正式に担当サポーターとしてアサインすることになります。シニア会員向けは、主に電話にて連絡を行う想定ですが、サポーター会員向けの連絡は、アプリ上で自動的に行うようにすることを想定しています。)

### 管理者画面
<img src = "https://user-images.githubusercontent.com/82374688/160223593-08d85248-b710-419e-b335-c0067da848b5.png" width=300px>

デモプログラム限定の通常のボタン操作ではたどり着くことができない画面です。（http://127.0.0.1:5000/admin）　

ユーザー画面で表示されるサポーター会員を追加します。

写真は./app/static/images/peopleフォルダーのjpg方式で保存された画像名を入力します。

## データセット・データ分析
### データセット作成

本来であれば、本サービスの運営に伴い、実際のシニア会員の承諾を得たうえで収集し、蓄積すべきでデータセットですが、今回はデモアプリ用にイメージをお伝えするために、サンプルデータを作成しました。なお、サンプルデータの作成にあたっては、総務省統計局が発表しているものを含む、実際の統計データを基に、日本のシニア世代の現実の傾向を踏まえております。

データセットを作成するにあたって設定した説明変数は

`年齢,性別,過去の重病の有無,家族構成,孤独感,運動の頻度,睡眠時間,地域,大まかな貯金`

であり、

`2年後の介護の必要性`

を被説明変数（出力結果）として学習を行いました。

### データ分析

本アプリケーションでは、分析画面で入力した情報を基に、2年後の介護の必要性の予測とその確率の二つの場面で機械学習を行いました。

#### 2年後の介護の必要性
出力結果は"必要かそうでないか"の2択なので、手法はRandomForestClassifierを採用しました。データの標準化は行わずに学習を行った結果、学習精度は約86％となりました。

#### 要介護になり得る確率
"2年後の介護の必要性"と関係のある結果を求めているので、手法はRandomForestRegressionを採用しました。その確率が0.4~0.5付近で必要か否かを決定する関係性がありました。その確率に対して各ラベルの寄与率は以下のグラフのようになりました。

![image](https://user-images.githubusercontent.com/82374688/160535790-fe6ea560-6504-481a-b935-0683ef52a486.png)



## 環境
本アプリケーションはFlaskを利用しています。そのため、起動にはPythonのインストールと以下のモジュールが必要です。

`flask flask-sqlalchemy flask-bootstrap flask-login`

## 文責

* 制作チーム 鈴木総合研究所
* 所属 東京電機大学,立教大学大学院

<img src = "https://user-images.githubusercontent.com/82374688/158979845-af480279-380e-474f-8cd5-ddd19241154d.png" width=400px>

## あとがき
<img src = "https://user-images.githubusercontent.com/82374688/163708744-60e4284f-54df-4617-8f59-25bbb957831b.png" width=500px>

出場16チーム中、2位という結果となり、優秀賞を獲得できました。
詳細は[こちら](https://www.nttpc.co.jp/press/2022/04/202204211500.html)
