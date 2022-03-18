<img src = "https://user-images.githubusercontent.com/82374688/158964569-50af5ace-3843-4570-b8c0-d982ec26a029.png" width=300px>

東京電機大学x立教大学主催のコンテスト[集え！未来のAI人材たち](https://www.nttpc.co.jp/innovationlab/event/ai_innovation_award_2022/)に提出したデモプログラムです。

提出テーマ:「人々の幸せ」を生むスマートシティを創ろう

## アプリ説明

「世代間を超えた支えあいで、日本に希望を取り戻す」をコンセプトとした、若年層・中年層・シニア層にWin-Win-Winなマッチングアプリ。
入力した「年齢・お住まい・孤独感・睡眠時間・貯金額」をAIが分析し、今後3年以内に要介護となる可能性を予測します。

## 使い方

### 起動方法

サーバプログラム（app.py）を起動したうえで http://127.0.0.1:5000/ に接続。

### トップ画面

<img src = "https://user-images.githubusercontent.com/82374688/158966566-8ab6c713-9833-4fa5-870b-cff4fa8c163f.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158966704-a684a5b7-2d4c-44b6-b855-04394632e0e8.png" width=300px>

本アプリの説明がメインの画面です。新規ユーザーは"今すぐ分析"ボタン、既に会員のユーザーは"ログイン"ボタンを押下し、分析画面に遷移します。

### 分析画面
<img src = "https://user-images.githubusercontent.com/82374688/158969566-691170df-6220-4920-ab10-4f9bfb57768c.png" width=300px>

分析対象となるシニアユーザーの情報を入力します。空欄なく入力が完了したら、"完了！"ボタンを押下して入力を送信します。

### 分析結果画面
<img src = "https://user-images.githubusercontent.com/82374688/158974278-1836f681-ac02-44d6-96bd-a6dc884e5937.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158974382-7e174d20-815f-4625-bd11-a61321504ac9.png" width=300px>

分析画面の入力情報を基にAIが分析し、今後3年以内の必要性を分析します。必要だった場合はその確率が表示され、新規登録を促されます。

### 新規登録・ログイン画面
<img src = "https://user-images.githubusercontent.com/82374688/158975093-32ce2f69-a568-4955-a91a-6d27ab935fee.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158975257-fd3943d2-28a7-42c1-8b5e-f06bf03fd6b8.png" width=300px>

新規登録画面では登録したいユーザー名とパスワードを入力します。今回はどちらも文字数や使用文字の指定はございません。

ログイン画面では登録した情報を入力します。

### ユーザー画面
<img src = "https://user-images.githubusercontent.com/82374688/158976266-a3154ea2-e32b-430f-ba7e-4bea7df5a1cd.png" width=300px><img src = "https://user-images.githubusercontent.com/82374688/158976404-09077093-469d-4229-a6ed-f3c63269ebf2.png" width=300px>

マッチングをメインに行う画面です。「～現在のマッチ候補～」に表示されているサポーターに「いいかも！」をすると、「～いいかも！をした人～」にそのサポーターが表示されます。
"ログアウト"ボタンを押下すると、トップ画面に遷移します。

### 管理者画面
<img src = "https://user-images.githubusercontent.com/82374688/158977147-3f80118b-c288-4486-8ce1-bebbb1eed7ed.png" width=300px>
通常のボタン操作ではたどり着くことができない画面です。（http://127.0.0.1:5000/admin）　

ユーザー画面で表示されるサポーターを追加します。

写真は./app/static/images/peopleフォルダーのjpg方式で保存された画像名を入力します。



