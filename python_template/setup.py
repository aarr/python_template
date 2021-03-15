from distutils.core import setup

"""パッケージ作成
python setup.py sdist
を実行することで、同フォルダにdistフォルダを作成し、パッケージを作成することが可能
"""
setup(
    name='python_template',
    version='1.0.0',
    packages=['basic', 'com', 'ext'],
    url='hoge',
    license='Free',
    author='name',
    author_email='mail',
    description='python template'
)