# ポジティブ変換アプリ

下記を学ぶためにアプリを生成する。
1. 生成AI
2. Langchain
3. Azure Web Apps
4. GitHub Action

# 実行方法

1. ルートディレクトリに.envファイルの作成する。
2. .envファイルの中に下記を入力する。 ※ 下記は環境変数でも問題ない。
   1. OPENAI_API_KEY : 自分のOpen AIのキーを入力する。
   2. AOAI_MODEL : 利用したいモデル名を入力する。(Ex: gpt-3.5-turbo)
3. 仮想環境を作成し、必要なライブラリを導入するために、下記を入力する。
```bash
python -m venv .venv # pythonは 3.12 とする。
source .venv/bin/activate # Windowsの場合は　.venv/Scripts/activate となる。
pip install -r requirements.txt # このアプリ実行のための必要なライブラリがインストールされる。
```
4. 下記でアプリを起動する。
```bash
chainlit run src/main.py
```
