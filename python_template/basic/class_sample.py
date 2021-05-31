#!/usr/bin/env python3
"""ClassSample
"""
import abc

import com.console

log = com.console.log
log_add_line = com.console.log_add_line

log('#============================')
log('# Classサンプル')
log('#============================')
log("＞Class---------------")


class Person(object):
    """Personクラス

    Args:
        object (object): オブジェクト
    """
    def __init__(self, first_name, last_name):
        """コンストラクタ

        Args:
            first_name (str): 名字
            last_name (str): 名前
        """
        self.first_name = first_name
        # プロパティ化するフィールドは「_」をつける
        self._last_name = last_name
        self.__original_last_name = last_name

    def say_something(self):
        """say something"""
        log('I am {}. hello'.format(self.first_name))

    def run(self):
        log('{} run'.format(self.first_name))

    @property
    def last_name(self):
        """名前取得

        Returns:
            str: 名前
        """
        return self._last_name

    @last_name.setter
    def last_name(self, new_last_name):
        """名前設定

        Args:
            new_last_name (str): 名前

        Raises:
            ValueError: 複数可名前変更した際に発生
        """
        if self.__original_last_name == self._last_name:
            self._last_name = new_last_name
        else:
            raise ValueError('苗字変更は1回まで')

    @property
    def original_last_name(self):
        """オリジナル名前取得

        Returns:
            str: オリジナル名前
        """
        return self.__original_last_name

    def __del__(self):
        """デストラクタ
        インスタンスが破棄される際に実行される
        明示的にdelされるか、処理の最後
        """
        log('good bay. {}'.format(self.first_name))



log('CLASS', 'start')
messi = Person('Messi', 'Lionel')
cameron = Person('Cameron', 'Diaz')
messi.say_something()
cameron.say_something()
# delしたタイミングででコンストラクタが呼ばれる（messi）
# delしなくても、処理が終了時にでコンストラクタが呼ばれる（diaz）
del messi
log('CLASS', 'end')
log_add_line(1)


log("＞Class extends---------------")
class SuperMan(Person):
    """スーパーマンクラス

    Args:
        Person (Person): Personクラス
    """
    def __init__(self, first_name, last_name, weapon):
        """コンストラクタ

        Args:
            first_name (str): 名字
            last_name (str): 名前
            weapon (str): 武器名
        """
        super().__init__(first_name, last_name)
        self.weapon = weapon

    def fly(self):
        """飛行"""
        log('{} fly'.format(self.first_name))

    def attack(self):
        """攻撃"""
        log('{} attack with {}'.format(self.first_name, self.weapon))

kent = SuperMan('Kent', 'Clark', 'BEAM')
kent.say_something()
kent.fly()
kent.attack()
log_add_line(1)

log("＞Class property(Private Field)---------------")
try:
    # 読み取りのみ許容する。またはある条件のみ変更を許可する場合、
    # 直接フィールドにアクセスさえるのではなく、setter, getterを利用する
    cameron._last_name
except AttributeError as ex:
    log('Exception:{}. {}'.format(type(ex), ex))
    log('last name is readonly')
log_add_line(1)

# setterを利用して変更
log('Cameron\'s last name is {}'.format(cameron.last_name))
cameron.last_name = 'Carry'
log('After Changed, Cameron\'s last name is {}'.format(cameron.last_name))
log_add_line(1)

try:
    # setterのロジックで２回目の変更はエラーとさせている
    cameron.last_name = 'Lionel'
except ValueError as error:
    log('Exception:{}. {}'.format(type(error), error))
    log_add_line(1)

try:
    # 完全にprivateなフィールドを設ける
    # フィールド戦闘を「__」とする
    log('Cameron\'s original last name is {}'.format(
        cameron.__original_last_name))
except Exception as ex:
    log('Exception:{}. {}'.format(type(ex), ex))
    log('original last name is not accessable')
    log_add_line(1)

# Errorにはならないが、Privateなフィールドへの変更はできない
cameron.__original_last_name = "Hoge"
log('Cameron\'s original last name is {}'.format(cameron.original_last_name))
log('DIRECT ACCESS', 'Cameron\'s original last name is {}'.format(
    cameron.__original_last_name))
log(''' 外からPrivateなFiledと同名のFiledに対して値を設定する事は可能。
        self.__xxxで参照する時と、instance.__xxxでアクセスする時で値が異なる状況になり、
        バグを生みやすいので設定しないこと'''
)
log_add_line()


log("＞AbstractClass---------------")
# もともとPythonでは抽象クラス、インターフェースという考え方はなかった
# 使う必要がなければ使う必要はない。
# コードスタイルではあまり利用しない方が良いとのこと。知っている程度でよい。
class AdultPerson(Person, metaclass=abc.ABCMeta):
    """抽象クラス"""

    # 継承したクラスで必ず実装する関数に対してアノテーションを設定する
    @abc.abstractmethod
    def drive(self):
        pass


class ProSoccerPlayer(AdultPerson):
    """プロサッカー選手"""
    # 必ず指定の関数を実装する
    def drive(self):
        log('{} drive SUPER CAR'.format(self.first_name))


class ProBasketPlayer(AdultPerson):
    """プロバスケットボール選手"""
    # 指定されたメソッドを実装しない
    pass


# 正常系
neymal_jr = ProSoccerPlayer('Neymal', 'Silva')
neymal_jr.drive()
# 異常系
try:
    jodan = ProBasketPlayer('Michael', 'Jodan')
except Exception as ex:
    log('抽象クラスで指定された関数を実装していない場合、エラー')
    log(ex)
log_add_line()


log("＞多重継承---------------")
class ProBaseballPlayer(Person):
    """プロ野球選手"""
    def drive(self):
        log('{} don\'t drive'.format(self.first_name))


class Jodan(ProBaseballPlayer, ProBasketPlayer):
    """マイケル・ジョーダン

    Args:
        ProBaseballPlayer (ProBaseballPlayer): プロ野球選手
        ProBasketPlayer (ProBasketPlayer): プロバスケットボール選手
    """

    def __init__(self, sponsor):
        """コンストラクタ

        Args:
            sponsor (str): スポンサー
        """
        super().__init__('Michale', 'Jodan')
        self.__sponsor = sponsor

    def drive(self):
        """運転する"""
        log('Superクラスのdrive呼び出し')
        super().drive()

    def new_release(self, model):
        """新作発表

        Args:
            model (str): 新作モデル
        """
        log('{} new release {} by {}'.format(self._last_name, model, self.__sponsor))


jodan = Jodan('Nike')
jodan.drive()
jodan.new_release('Air Jodan')
log_add_line()


log("＞クラス変数、メソッド---------------")
class ClassPerson(object):
    """クラス変数・メソッド確認用クラス

    Args:
        object (object): オブジェクト
    """
    # クラス変数
    kind = 'human'

    def __ini__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        try:
            # staticメソッドではクラス変数にアクセスできない
            # クラス変数もインスタンス変数も利用しない場合に利用可能。若干パフォーマンスが早いとか
            log('about {} {} '.format(kind, year))
        except NameError as error:
            log(error)
        log('about human {}'.format(year))


human = ClassPerson()
log('Object:KIND:field', human.kind)
log('Object:KIND:class_method', human.what_is_your_kind())
log_add_line(1)

log('CLASS:KIND:field', ClassPerson.kind)
log('CLASS:KIND:class_method', ClassPerson.what_is_your_kind())
ClassPerson.about(2021)
log_add_line()


log("＞特殊メソッド---------------")
