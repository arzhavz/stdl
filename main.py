import os
import typer

from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import (
	button_dialog,
	message_dialog,
	input_dialog,
	radiolist_dialog
)

from typing_extensions import Annotated

from lib.connector import Database
from lib.loading import LoadingMonitor
from lib.messages import Messages
from lib.theme import Themes

from plugin import Anime


class Applications:
	def __init__(self):
		self.db = Database()
		self.theme = Themes.loads(self.db.read(self.db.id)["user"]["theme"])
	
	def _anime_info(self):
		result = radiolist_dialog(
			title=Messages.title,
			text="Silahkan pilih website penyedia anime yang tersedia.",
			style=self.theme,
			values=[
				("kusonime", "Kusonime"),
				("otakudesu", "Otakudesu"),
				("samehada", "Samehadaku")
			]
		).run()
		if result == None:
			Applications().run_program()
		if result == "kusonime":
			Anime.Kusonime().run_program()
		elif result == "otakudesu":
			Anime.Otakudesu().run_program()
		elif result == "samehada":
			Anime.Samehadaku().run_program()

	def _settings(self):
		result = button_dialog(
			title=Messages.title,
			text="SIlahkan pilih preferensi yang ingin kamu ubah.",
			style=self.theme,
			buttons=[("Nama", "name"), ("Tema", "theme"), ("Batalkan", "cancel")]
		).run()
		if result == "cancel":
			Applications().run_program()
		elif result == "name":
			uid = self.db.id
			data = self.db.read(uid)
			username = data["user"]["name"]
			new_name = input_dialog(
				title=Messages.title,
				text=HTML(f"Namamu sekarang adalah <ansiyellow>{username}</ansiyellow>. Mohon masukkan nama baru kamu di bawah."),
				style=self.theme
			).run()
			if new_name == None or new_name == "":
				message_dialog(
					title=Messages.title,
					text=HTML(f"Operasi dibatalkan oleh user."),
					style=self.theme
				).run()
				Applications()._settings()
			else:
				message_dialog(
					title=Messages.title,
					text=HTML(f"Sukses mengganti nama menjadi <ansiyellow>{new_name}</ansiyellow>."),
					style=self.theme
				).run()
				self.db.update(uid, {"name": new_name})
				Applications()._settings()
		elif result == "theme":
			uid = self.db.id
			data = self.db.read(uid)
			usertheme = data["user"]["theme"]
			new_theme = radiolist_dialog(
				title=Messages.title,
				text=HTML(f"Tema yang kamu gunakan sekarang adalah <ansiyellow>{usertheme}</ansiyellow>. Mohon pilih tema baru kamu di bawah."),
				style=self.theme,
				values=[
					("Dark Default", "Dark Default"),
					("Dark Green", "Dark Green"),
					("Dark Electric Blue", "Dark Electric Blue"),
					("Dark Pink", "Dark Pink"),
					("Dark Yellow", "Dark Yellow"),
					("Dusk", "Dusk")
				]
			).run()
			if new_theme == None:
				message_dialog(
					title=Messages.title,
					text=HTML(f"Operasi dibatalkan oleh user."),
					style=self.theme
				).run()
				Applications()._settings()
			else:
				message_dialog(
					title=Messages.title,
					text=HTML(f"Sukses mengganti nama menjadi <ansiyellow>{new_theme}</ansiyellow>."),
					style=self.theme
				).run()
				self.db.update(uid, {"theme": new_theme})
				Applications()._settings()
				
	def run_program(self, loading: bool = False):
		try:
			uid = self.db.id
			data = self.db.read(uid)
			username = data["user"]["name"]
			if loading == True: 
				LoadingMonitor(username).start_monitoring()
			result = radiolist_dialog(
				title=Messages.title,
				text=HTML(f"Selamat datang <ansiyellow>{username}</ansiyellow>! Silahkan pilih menu yang tersedia di bawah."),
				style=self.theme,
				values=[
					("animedl", "Anime Info"),
					("settings", "Settings"),
					("donate", HTML(f"<ansimagenta>Donate</ansimagenta>"))
				]
			).run()
			if result == "settings":
				Applications()._settings()
			elif result == "animedl":
				Applications()._anime_info()
			elif result == "donate":
				os.system("start https://saweria.co/arzhavz")
				message_dialog(
					title=Messages.title,
					text=HTML(f"Arigatou nee!"),
					style=self.theme
				).run()
			else:
				message_dialog(
					title=Messages.title,
					text=HTML(f"Sayonara <ansiyellow>{username}</ansiyellow>!"),
					style=self.theme
				).run()
			return True
		except Exception as e:
			message_dialog(
				title=Messages.title,
				text=HTML(f"Terjadi kesalahan: <ansired>{e}</ansired>\nKlik tombol <ansiyellow>OK</ansiyellow> di bawah untuk keluar."),
				style=self.theme
			).run()


def CLI(
	intro: Annotated[bool, typer.Option(help="Mengaktifkan GUI simulasi loading saat dinyalakan.")] = False,
	support: Annotated[bool, typer.Option(help="Membuka GUI daftar dukungan tersedia.")] = False
):
	"""
	
	STDL (Scraping Tools and Downloaders) adalah sebuah program yang dapat digunakan untuk mengunduh atau mendapatkan informasi dari website yang tersedia di STDL.
	
	Untuk dukungan, tambahkan flag --support.
	Untuk memulai program dengan tambahan halaman intro, tambahkan flag --intro.
	
	"""
	if support:
		from time import sleep

		from rich.align import Align
		from rich.console import Console
		from rich.panel import Panel

		console = Console()

		with console.screen(style="bold cyan") as screen:
			text = Align.center("[blink]Kamu akan diarahkan ke Facebook![/blink]", vertical="middle")
			screen.update(Panel(text))
			sleep(3)
		os.system("start https://facebook.com/sndyarz")
		return
		
	Applications().run_program(loading = intro)
	
	
typer.run(CLI)