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
from lib.utils import KeyListCreator, Validation

from lib.scraper.kusonime import Kusonime, KusonimeSearch

	
class App:
	def __init__(self):
		self.db = Database()
		self.theme = Themes.loads(self.db.read(self.db.id)["user"]["theme"])

	def _download(self, link: str = "nothing"):
		if link == "nothing":
			link = input_dialog(
				title=Messages.title,
				text=HTML("Mohon masukkan link anime dari Kusonime."),
				style=self.theme,
			).run()
			
			kuso_regex = re.compile(
				r'^https?://'
				r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
				r'kusonime|'
				r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
				r'(?::\d+)?'
				r'(?:/?|[/?]\S+)$', re.IGNORECASE
			)
			
			if link == "":
				message_dialog(
					title=Messages.title,
					text=HTML(
						f"Mohon masukkan tautan!"
					),
					style=self.theme,
				).run()
				self._download()
			
			if link == None:
				self.run_program()
				
			if not Validation(kuso_regex).URL(link):
				message_dialog(
					title=Messages.title,
					text=HTML(
						f"Tautan <ansigreen>{link}</ansigreen> tidak valid!"
					),
					style=self.theme,
				).run()
				self._download()
			
		else:
			kuso_data = LoadingTask(Messages.title, link, Kusonime)
			anim = kuso_data.get_info
			result = button_dialog(
				title=Messages.title,
				text=anim['title'],
				style=self.theme,
				buttons=[
					("Detail", "detail"),
					("Download", "download"),
					("Batalkan", "cancel"),
				],
			).run()

			if result == "cancel":
				self._download()
			elif result == "detail":
				message_dialog(
					title=Messages.title,
					text=(
						f"{anim['title']}\n\n"
						f"Jepang: {anim['info']['japanese']}\n"
						f"Views: {anim['info']['views']}\n"
						f"Genres: {(anim['info']['genres'])}\n"
						f"Seasons: {anim['info']['seasons']}\n"
						f"Producers: {(anim['info']['producers'])}\n"
						f"Type: {anim['info']['type']}\n"
						f"Status: {anim['info']['status']}\n"
						f"Episodes: {anim['info']['episodes']}\n"
						f"Scores: {anim['info']['scores']}\n"
						f"Duration: {anim['info']['duration']}\n"
						f"Release: {anim['info']['release']}"
					),
					style=self.theme,
				).run()
				self._download(link)
			else:
				resolutions = KeyListCreator(kuso_data.all_res).create_key_list()
				selected_reso = radiolist_dialog(
					title=Messages.title,
					text=HTML(
						f"Silahkan pilih resolusi yang ingin kamu unduh."
					),
					style=self.theme,
					values=resolutions,
				).run()
				if selected_reso == None:
					self._download(link)
				else:
					reso_data = kuso_data.get_url(selected_reso)
					hosts = KeyListCreator(reso_data).create_sub_key_list()
					selected_host = radiolist_dialog(
						title=Messages.title,
						text="Silahkan pilih file hosting yang tersedia.",
						values=hosts,
						style=self.theme
					).run()
					if selected_host == None:
						self._download(link)
					else:
						host_data = reso_data[selected_host]
						return os.system(f"start {host_data}")

	def _search(self):
		result = input_dialog(
			title=Messages.title,
			text=HTML("Mohon masukkan judul anime yang ingin kamu cari di Kusonime."),
			style=self.theme,
		).run()
		
		if result == "":
			message_dialog(
				title=Messages.title,
				text=HTML(
					f"Mohon masukkan kueri!"
				),
				style=self.theme,
			).run()
			self._search()
		
		if result == None:
			self.run_program()

		data = LoadingTask(Messages.title, result, KusonimeSearch)
		if len(data) <= 0:
			message_dialog(
				title=Messages.title,
				text=HTML(
					f"Anime dengan kueri <ansigreen>{result}</ansigreen> tidak ditemukan!"
				),
				style=self.theme,
			).run()
			self._search()
		else:
			url = radiolist_dialog(
				title=Messages.title,
				text=HTML(
					f"Silahkan pilih judul dari hasil pencarian dengan kueri <ansigreen>{result}</ansigreen> di bawah."
				),
				style=self.theme,
				values=data,
			).run()

			if url == None:
				self._search()
			else:
				self._download(link=url)

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
				("Search", "search"),
				("Exit", "exit"),
			],
		).run()
		if result == "search":
			self._search()
		elif result == "download":
			self._download()
		else:
			return message_dialog(
				title=Messages.title,
				text=HTML(f"Sayonara <ansiyellow>{username}</ansiyellow>!"),
				style=self.theme,
			).run()