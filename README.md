# LINE半垢

--必須事先安裝Python--

首先進入bot資料夾

找到run.txt和token.txt

把Your_LINE_TOKEN刪除,把你的AuthTOKEN貼上去

在當前的資料夾啟動終端

輸入這串:pip install -r requirements.txt (使用pip安裝所需要的程式)

最後輸入:python x.py 就好了

如果你想上傳到heroku

--必須事先安裝Heroku Cli--

先輸入 heroku login

cd 你的資料夾位置

git init

heroku git:remote -a 你的heroku app名稱

git add .

git commit -am "make it better"

git push heroku master

以上
