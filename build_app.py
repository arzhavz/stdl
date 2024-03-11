import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
	'--name=Zeta',
    r'--icon=src\icon.ico',
	r'--noconfirm',
	r'--add-data=env\Lib\site-packages\bs4;bs4',
	r'--add-data=env\Lib\site-packages\certifi;certifi',
	r'--add-data=env\Lib\site-packages\charset_normalizer;charset_normalizer',
	r'--add-data=env\Lib\site-packages\click;click',
	r'--add-data=env\Lib\site-packages\colorama;colorama',
	r'--add-data=env\Lib\site-packages\idna;idna',
	r'--add-data=env\Lib\site-packages\markdown_it;markdown_it',
	r'--add-data=env\Lib\site-packages\mdurl;mdurl',
	r'--add-data=env\Lib\site-packages\prompt_toolkit;prompt_toolkit',
	r'--add-data=env\Lib\site-packages\pygments;pygments',
	r'--add-data=env\Lib\site-packages\requests;requests',
	r'--add-data=env\Lib\site-packages\rich;rich',
	r'--add-data=env\Lib\site-packages\soupsieve;soupsieve',
	r'--add-data=env\Lib\site-packages\typer;typer',
	r'--add-data=env\Lib\site-packages\urllib3;urllib3',
	r'--add-data=env\Lib\site-packages\wcwidth;wcwidth'
])