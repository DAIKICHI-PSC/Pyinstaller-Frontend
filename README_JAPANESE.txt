PyinstallerFrontEnd
Pyinstallerフロントエンド


説明：
このプログラムはpyinstallerのフロントエンドです。
GUIでpythonファイルをexeファイルに変換することができます。
  
Python環境：
Python 3.7

必要なモジュール：
PySide6
pyinstaller
  
インストール1：
PySide2がインストールされてない場合は、コンソールで以下を実行して下さい。
pip install pyside6
pyinstallerがインストールされてない場合は、コンソールで以下を実行して下さい。
pip install pyinstaller
pythonnet（エラーが発生した場合）
pip install pythonnet
  
インストール2：
ドライブにファイルを配置したら、PyinstallerFrontEnd.pyを実行します。
pyinstaller.exeのパスを設定します（例：PYTHON_FOLDER/Scripts/pyinstaller.exe）。
PyinstallerFrontEnd.pyを選択してください。
icon.icoを選択してください。
すべてのチェックボックスをチェックしてください。
EXECボタンを押して、pyファイルをexeファイルに変換します。
PyinstallerFrontEnd.pyがPyinstallerFrontEnd.exeに正常に変換されたら、distフォルダにicon.icoをコピーします。
好きな場所にPyinstallerFrontEnd.exeのショートカットファイルを作成します。