import os
import re

from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import (
	button_dialog,
	message_dialog,
	input_dialog,
	radiolist_dialog,
)

from lib.connector import Database
from lib.loading import LoadingTask
from lib.messages import Messages
from lib.theme import Themes
from lib.downloader import MangaDownloader

from lib.scraper.komiku import Komiku

	
class App:
	def __init__(self):
		self.db = Database()
		self.theme = Themes.loads(self.db.read(self.db.id)["user"]["theme"])

	def _download(self):
		judul = input_dialog(
				title=Messages.title,
				text=HTML("Mohon masukkan judul dari manga yang ingin kamu unduh."),
				style=self.theme,
		).run()

		try: 
			data = LoadingTask(Messages.title, judul, Komiku)
			MangaDownloader(data).download_manga()
			return message_dialog(
				title=Messages.title,
				text=HTML("Selesai mengunduh! Silahkan periksa folder <ansiyellow>Downloads</ansiyellow>!"),
				style=self.theme,
			).run()
		except Exception as e:
			message_dialog(
				title=Messages.title,
				text=HTML(f"Terjadi kesalahan: <ansired>{e}</ansired>\nKlik tombol <ansiyellow>OK</ansiyellow> di bawah untuk keluar."),
				style=self.theme
			).run()

	def run_program(self):
		uid = self.db.id
		data = self.db.read(uid)
		username = data["user"]["name"]
		result = button_dialog(
			title=Messages.title,
			text=HTML(
				f"Halo <ansiyellow>{username}</ansiyellow>, silahkan pilih menu yang tersedia di bawah."
			),
			style=self.theme,
			buttons=[
				("Download", "download"),
				("Exit", "exit"),
			],
		).run()
		if result == "download":
			self._download()
		else:
			return message_dialog(
				title=Messages.title,
				text=HTML(f"Sayonara <ansiyellow>{username}</ansiyellow>!"),
				style=self.theme,
			).run()