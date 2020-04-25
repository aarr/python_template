#!/usr/bin/env python3
'''OMAKASE予約
・日次で動かして、店舗メニューの取得
・特定時間に予約を実施
・自動予約の為のINPUT情報登録
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Chromeのバージョンと合わせないと行けないため、最新をインストールでは動かない事がある
# ~=で前方一致的な感じとなる。
# pip3 install chromedriver-binary~=80.0.3987
import chromedriver_binary ,time ,re, sys, os, datetime, logging

# 別ディレクトリのため、パス追加
script_dir = os.path.abspath(__file__)
base_dir = os.path.join(os.path.dirname(script_dir), '..')
sys.path.append(os.path.join(base_dir, 'com'))

from performance import Performance
from console import *
import file_manager as file_operation

pf = Performance()
log('#============================')
log('# SELENIUM ')
log('#============================')
# OMAKASE情報
url = 'https://omakase.in/users/sign_in'
reserve_button_text = 'このお店を予約する'
# システム設定
day_of_week_for_display = ['月', '火', '水', '木', '金', '土', '日']
wait_seconds_for_get_shot_list = 5
# ID、PASSWORD情報管理ファイル
id_pass_config = os.path.join(base_dir, 'config', 'omakase.config')
# 予約リクエスト
target_shop_name = 'はっこく'
target_num_of_people = 2
# 優先順位をweekdayの値（0-6）に変換
priority_week_day = ['土', '日', '金', '月', '火', '水', '木']
priority_week_day_num = list(map(lambda elem : day_of_week_for_display.index(elem), priority_week_day))

# seleniumロガー設定
selenium_logger = logging.getLogger('selenium')
selenium_logger.setLevel(logging.ERROR)
driver = None

# ==========================================
# 関数定義
# ==========================================
def save_id_pass(id, passwd):
    config = {'id' : id, 'passwd' : passwd}
    file_operation.save_shelve('config', config, id_pass_config)

def get_id_pass():
    return file_operation.get_shelve('config', id_pass_config)

def get_ym_at_reservations(driver):
    '''予約画面にて予約年月情報を取得する
    Args:
        driver : selenium driver
    Returns:
        str : 年月テキスト
    '''
    ym = driver.find_element_by_css_selector('.p-reservation_customer_table_header > div')
    return ym.text if ym != None else None


def get_reservable_days_at_reservations(driver):
    '''予約画面にて予約可能日付を取得する
    Args:
        driver : selenium driver
    Returns:
        list : 予約可能日リスト
    '''
    return driver.find_elements_by_css_selector(
        '.p-reservation_customer_table a:not([class*="disabled"])')


def get_next_month_link_at_reservations(driver):
    '''予約画面にて翌月リンクを取得します
    Args:
        driver : selenium driver
    Returns:
        dict : 翌月リンクオブジェクト。リンクが無効の場合Noneを返却
    '''
    links =  driver.find_elements_by_css_selector(
            '.p-reservation_customer_table_header > a:not([style="visibility: hidden;"])')
    return links[1] if len(links) == 2 else None

def to_ym_dict(ym_str):
    '''年月文字列を年と月の値に分離し、オブジェクトで返却する
    OMAKASE用のフォーマットを考慮
    '''
    return to_ym_dict_from_format(ym_str, '(.*)年(.*)月')


def to_ym_dict_from_format(ym_str, ym_format):
    '''年月文字列を年と月の値に分離し、オブジェクトで返却する
    Args:
        ym_str(str) : 年月文字列
        ym_format(str) : 年月フォーマット（例：「(.*)年（.*)月」）
    Returns:
        dict : 年月値オブジェクト（ {year : year_val, month : month_val}）
    '''
    regex_ym = re.compile(ym_format)
    match_ym = regex_ym.search(ym_str)
    year = match_ym.group(1)
    month = match_ym.group(2)
    return {'year' : year, 'month' : month}


# TODO 再起処理にしない方がよい
# 再起処理にした場合の変数の設定具合を確認
# クロージャ的なものがあるのか確認
def reserve(driver, is_target_next_month=False):
    ''' 予約実行
    予約可能な日にちがある迄、予約可能な月を総確認する
    '''
    pf.mark('reserve:start')
    try:
        # 翌月を処理する場合、遷移
        if is_target_next_month:
            link_next_month = get_next_month_link_at_reservations(driver)
            if link_next_month != None:
                # click & 月移動リンクが押下できるようになるまでwati
                link_next_month.click()
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-reservation_customer_table_header > a')))
            else:
                log('最終月まで処理完了')
                return True
        
        # 予約
        target_ym = get_ym_at_reservations(driver)
        ym_dict = to_ym_dict(target_ym)
        year = ym_dict['year']
        month = ym_dict['month']
        log('予約年月', '{0}/{1}'.format(year, month))

        # 予約可能日付一覧取得
        reservable_days = get_reservable_days_at_reservations(driver) 
        count_reservable_day = len(reservable_days)
        # 予約可能な日付なし
        if count_reservable_day == 0:
            # 翌月へ遷移
            log('{0}/{1} 予約可能枠なし'.format(year, month))
            return False 
        else:
            # 曜日／時間判定 
            log('{0}/{1} 予約可能枠[{2}]'.format(year, month, count_reservable_day)) 
            reservables = {} 
            for reservable_day in reservable_days:
                str_day = reservable_day.text
                date = datetime.date(int(year), int(month), int(str_day))
                week_day = date.weekday()
                #log('{0}/{1}/{2} {3}'.format(year, month, str_day, day_of_week[week_day]))
                list_by_weed_day = reservables.get(week_day, [])
                list_by_weed_day.append({'day' : str_day, 'elem' : reservable_day})
                reservables[week_day] = list_by_weed_day

            for priority in priority_week_day_num:
                target_days = reservables.get(priority, None)
                # 指定の優先度が存在しなければ、次の優先度を確認
                if target_days == None:
                    continue
                log('曜日別({0})'.format(day_of_week_for_display[priority]), target_days)

                for target_day in target_days:
                    # 日にちclick & オプション選択が可能になるまでwait
                    target_day['elem'].click()
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.p-rsv_c_select_item ul div.checkbox label')))
                    # 予約画面に遷移できた場合、予約実行
                    # 予約画面で遷移できなかった場合、別プロセスを立ち上げて他の日付を検索 
                    # その際に、予約中の日付を対象外とする
                    reservable_times = driver.find_elements_by_css_selector('.p-rsv_c_select_item ul div.checkbox label')
                    for reservable_time in reservable_times:
                        reservable_time.click()

                        options = driver.find_elements_by_css_selector('.ui.fluid.dropdown.selection')
                        # 人数選択
                        selector_num_of_people  = options[0]
                        selector_num_of_people.click()
                        optinos_num_of_people = driver.find_elements_by_css_selector('.menu.transition.visible>div>span')
                        for option_num_of_people in optinos_num_of_people:
                            if int(option_num_of_people.text) == target_num_of_people:
                                option_num_of_people.click()

                        # 時間選択
                        selector_time = options[1]
                        selector_time.click()
                        optinos_times = driver.find_elements_by_css_selector('.menu.transition.visible>div>span') 
                        for optino_time in optinos_times:
                            # 18時以降
                            if int(optino_time.text[0:2]) >= 18:
                                # 予約確定ボタン押下
                                button_go_to_reservation = driver.find_element_by_css_selector('.p-rsv-detail .primary.button')
                                button_go_to_reservation.click()
                                # TODO ここで予約までするか
                                return True
                            else:
                                continue
            return False
        log('予約可能日付', {day_of_week_for_display[num_day_of_week] : list(map(lambda elem : elem['day'], info)) for num_day_of_week, info in reservables.items()})
    finally:
        pf.mark('reserve:end')
        pf.mesure('reserve', 'reserve:start', 'reserve:end')

# ==========================================
# メイン処理
# ==========================================
try:
    # 最初に実効時にID、PASSWDをファイルに保存
    # 2度目に実効する際には何も必要ない。
    # ログイン情報を変えたい場合、引数ありで再実行
    if len(sys.argv) == 3:
        args = sys.argv
        # args[0]はスクリプトファイル名
        save_id_pass(args[1], args[2])
    elif os.path.isfile(id_pass_config) == False:
        log('ERROR', '１度は引数（アドレス、パスワード）を指定して実効してください')
        sys.exit()


    # driver設定
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # ログイン画面機動
    pf.mark('get:start')
    driver.get(url)
    pf.mark('get:end')
    pf.mesure('get', 'get:start', 'get:end')
    # ログイン入力
    pf.mark('login_input:start')
    config = get_id_pass()
    elem_input_id = driver.find_element_by_id('user_email')
    elem_input_id.send_keys(config['id'])
    elem_input_pass = driver.find_element_by_id('user_password')
    elem_input_pass.send_keys(config['passwd'])
    elem_checkbox = driver.find_element_by_id('user_remember_me')
    elem_checkbox.click()
    elem_btn_login = driver.find_element_by_name('commit')
    pf.mark('login_input:end')
    pf.mesure('login_input', 'login_input:start', 'login_input:end')

    pf.mark('login:start')
    elem_btn_login.click()
    pf.mark('login:end')
    pf.mesure('login', 'login:start', 'login:end')

    # お店一覧への繊維
    pf.mark('go_list:start')
    elem_link_search_shop = driver.find_element_by_link_text('お店を探す')
    elem_link_search_shop.click()
    pf.mark('go_list:end')
    pf.mesure('go_list', 'go_list:start', 'go_list:end')

    # 店ページ遷移
    # 全店舗情報が読み込まれるまで時間が掛かる為、waitする
    # driver.implicitly_wait(10)だけだと、
    # 一部の店舗が読み込まれたタイミングで処理が実行され店舗が見つからないことがある。
    time.sleep(wait_seconds_for_get_shot_list)
    pf.mark('detail:start')
    links = driver.find_elements_by_css_selector('.c-restaurant_item_detail > h4')
    is_exists_detail_page = False 
    # 全ページ（全店舗）のメニュー一覧を取得＆DB保存
    for link in links:
        shop_name = link.text
        log('SHOP', shop_name)
        if link.text == target_shop_name:
            is_exists_detail_page = True
            link.click()
            break
    pf.mark('detail:end')
    pf.mesure('detail', 'detail:start', 'detail:end')
    if is_exists_detail_page == False:
        log('店舗詳細ページ不在：{0}'.format(target_shop_name))
        sys.exit()


    # 詳細ページ
    # menu保持。そのうちどこかに保存
    pf.mark('detail:start')
    menus = driver.find_elements_by_css_selector('.p-r_course_upper > h3')
    for menu in menus:
        log('MENU', menu.text)

    # 予約ページ繊維
    buttons = driver.find_elements_by_tag_name('a')
    is_exists_reserve_page = False
    for button in buttons:
        if button.text == reserve_button_text:
            is_exists_reserve_page = True
            button.click()
            break
    pf.mark('detail:end')
    if is_exists_reserve_page == False:
        log('店舗予約ページ不在：{0}'.format(shop_name))
        sys.exit()

    # 予約
    is_target_next_month = False
    research_max_month_count = 5
    research_count = 0
    while research_count < research_max_month_count:
        is_finished = reserve(driver, is_target_next_month)
        if is_finished == True:
            break;
        is_target_next_month = True
        research_count = research_count + 1

finally:
    # パフォーマンス測定情報出力
    log(pf.get_simple_entries())
    #driver.quit()
