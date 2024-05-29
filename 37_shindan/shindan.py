# Ａ－１）ネコ度チェック項目リストのインポート
# CAT_CHECK_LIST（日本語）、または、CAT_CHECK_LIST_E（english）
from catcheck import CAT_CHECK_LIST_E
# Ａ－２）ネコ度チェック結果リストのインポート
# CAT_CHECK_RESULT（日本語）、または、CAT_CHECK_RESULT_E（english）
from catcheck import CAT_CHECK_RESULT_E
# Ａ－３）tkinterモジュールのインポート
import tkinter
# Ｄ－１６）ネコ度チェックの項目数
CHECK_COUNT = 7

# Ｃ－１２）ボタンクリック時の処理
def click_shindan():
    # Ｃ－１３）ターミナルに出力（デバッグ用）
    print('click_shindan')
    # Ｆ－２７）チェック数の初期値を０にする
    point = 0
    # Ｆ－２８）チェック項目の数だけ繰り返す
    for i in range(CHECK_COUNT):
        # Ｆ－２９）そのチェックボックスがチェックされていたら
        if cat_check[i].get() == True:
            # Ｆ－３０）チェック数を１増やす
            point += 1
    # Ｆ－３１）結果の文字列を削除（最初から最後までと範囲を指定）
    result_text.delete('1.0', tkinter.END)
    # Ｆ－３２）ネコ度を計算
    nekodo = int(100 * point / CHECK_COUNT)
    # Ｆ－３３）結果の文章を作成
    # ＜診断結果＞\n貴方のネコ度は  {nekodo}％です。\n
    # ＜Diagnosis results＞\n   Your cat level is {nekodo}%\n
    cat_result = '＜Diagnosis results＞\n'
    cat_result += f'Your cat level is {nekodo}%\n'
    cat_result += CAT_CHECK_RESULT_E[point]
    # Ｆ－３３）結果を表示（先頭に追加）
    result_text.insert('1.0', cat_result)

# Ａ－４）ウィンドウオブジェクトの作成
root = tkinter.Tk()
# Ａ－５）ウィンドウタイトルの設定
# 「ネコ度」診断アプリ / “Cat degree” diagnosis app
root.title('"cat degree"diagnosis app')

# Ａ－６）ウィンドウのサイズ変更をできなくする
root.resizable(False,False)
# Ｂ－８）キャンバスの作成
canvas = tkinter.Canvas(root, width=800,height=600)
# Ｂ－９）キャンバスの配置
canvas.pack()
# Ｂ－１０）画像ファイルの読み込み
back_image = tkinter.PhotoImage(file='image/cat_bg.png')
# Ｂ－１１）画像ファイルの表示
canvas.create_image(0, 0, image=back_image, anchor='nw')
# Ｃ－１４）ボタンの部品を作る
# （診断する / Diagnose、ＭＳ 明朝(Jpn) or ＭＳ ゴシック(Eng)、lightgreen）
shindan_button = tkinter.Button(root, text='Diagnose',
                                font=('ms ゴシック', 32),
                                bg='skyblue',
                                command= click_shindan)    
# Ｃ－１５）ボタンを配置する
shindan_button.place(x=400,y=480)
# Ｅ－２４）結果表示テキストボックスの部品を作る（ＭＳ ゴシック）
result_text = tkinter.Text(width=40, height=5,
                           font=('ＭＳ ゴシック', 16))
# Ｅ－２５）結果表示テキストボックスの部品を配置する
result_text.place(x=320, y=30)
# Ｅ－２６）先頭に初期メッセージを設定
# （ここに結果を表示します / Show results here.）
#result_text.insert('1.0', 'ここに結果を表示します')
result_text.insert('1.0', 'Show Result here.')
# Ｄ－１７）ネコ診断のチェック有無を入れるリスト
cat_check =  [None] * CHECK_COUNT
# Ｄ－１８）ネコ診断のチェックボタンのリスト
cat_cbtn = [None] * CHECK_COUNT

# Ｄ－１９）ネコ度チェックのチェックボックスと項目を配置
for i in range(CHECK_COUNT):
    # Ｄ－２０）ブール値オブジェクトを作成
    cat_check[i] = tkinter.BooleanVar()
    # Ｄ－２１）値に False を設定
    cat_check[i].set(False)
    # Ｄ－２２）チェックボタンの部品を作成
    # font Roman(Jpn) or Century Gothic(Eng)
    cat_cbtn[i] = tkinter.Checkbutton(root, text=CAT_CHECK_LIST_E[i],
                                      font=('century Gothic', 12),
                                      variable=cat_check[i],
                                      bg='#ddffee')
    # Ｄ－２３）チェックボタンの部品を配置
    cat_cbtn[i].place(x=400, y=160 + 40 *i)
# Ａ－７）ウィンドウの表示
root.mainloop()
