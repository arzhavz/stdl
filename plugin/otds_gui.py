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
from lib.messages import Messages
from lib.theme import Themes
from lib.utils import KeyListCreator, Validation

from lib.scraper.otakudesu import OtakudesuInfo, OtakudesuSearch
from lib.loading import LoadingTask


class OtakudesuGUI:
	def __init__(self):
		self.db = Database()
		self.theme = Themes.loads(self.db.read(self.db.id)["user"]["theme"])

	def _download(self, link: str = "nothing"):
		if link == "nothing":
			link = input_dialog(
				title=Messages.title,
				text=HTML("Mohon masukkan link anime dari Otakudesu."),
				style=self.theme,
			).run()
			
			otds_regex = re.compile(
				r'^https?://'
				r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
				r'otakudesu|'
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
			
			if not Validation(otds_regex).URL(link):
				message_dialog(
					title=Messages.title,
					text=HTML(
						f"Tautan <ansigreen>{link}</ansigreen> tidak valid!"
					),
					style=self.theme,
				).run()
				self._download()
			
		if link == None:
			message_dialog(
				title=Messages.title,
				text=HTML(
					f"Mohon masukkan URL!"
				),
				style=self.theme,
			).run()
			self._download()
		else:
			anim = LoadingTask(Messages.title, link, OtakudesuInfo)
			result = button_dialog(
				title=Messages.title,
				text=anim['info']['title'],
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
						f"{anim['info']['title']}\n\n"
						f"Jepang: {anim['info']['japanese']}\n"
						f"Genres: {(anim['info']['genres'])}\n"
						f"Producers: {(anim['info']['producer'])}\n"
						f"Type: {anim['info']['types']}\n"
						f"Studio: {anim['info']['studio']}\n"
						f"Episodes: {anim['info']['total_episodes']}\n"
						f"Scores: {anim['info']['score']}\n"
						f"Duration: {anim['info']['duration']}\n"
						f"Release: {anim['info']['release']}"
					),
					style=self.theme,
				).run()
				self._download(link)
			else:
				pilihan = [
					("Cancel", "cancel"),
					("Episode", "episode")
				]
				if anim["batch"] != {}:
					pilihan.append(("Batch", "batch"))
				action = button_dialog(
					title=Messages.title,
					text=("Silahkan pilih apa yang ingin kamu unduh."),
					style=self.theme,
					buttons=pilihan[::-1],
				).run()
				if action == "cancel":
					self._download()
				elif action == "episode":
					eps = anim["episode"]
					tup_eps = []
					for i, ep in enumerate(eps):
						tup_eps.append((f"ep_{i}", ep["title"]))
					episodenya = radiolist_dialog(
						title=Messages.title,
						text=(
								"Silahkan pilih episode di bawah."
						),
						style=self.theme,
						values=tup_eps,
					).run()
					
					if episodenya == None:
						message_dialog(
							title=Messages.title,
							text=HTML(
								f"Operasi dibatalkan oleh user."
							),
							style=self.theme,
						).run()
						self._download()
					else:
						selected_eps = anim["episode"][int(episodenya.split("_")[1])]
						reso = radiolist_dialog(
							title=Messages.title,
							text=(
								"Silahkan pilih episode di bawah."
							),
							style=self.theme,
							values=[
								("sd_360p", "360P SD {}".format(selected_eps['download']['sd_360p'][0]['size'])),
								("sd_480p", "480P SD {}".format(selected_eps['download']['sd_480p'][0]['size'])),
								("hd_720p", "720P HD {}".format(selected_eps['download']['hd_720p'][0]['size']))
							],
						).run()
						if reso == None:
							message_dialog(
								title=Messages.title,
								text=HTML(
									f"Operasi dibatalkan oleh user."
								),
								style=self.theme,
							).run()
							self._download()
						else:
							res_tup = []
							for ress in selected_eps["download"][reso]:
								res_tup.append((ress['url'], ress['name']))
							selected_host = radiolist_dialog(
								title=Messages.title,
								text=(
									"Silahkan pilih episode di bawah."
								),
								style=self.theme,
								values=res_tup,
							).run()
							if selected_host == None:
								message_dialog(
									title=Messages.title,
									text=HTML(
										f"Operasi dibatalkan oleh user."
									),
									style=self.theme,
								).run()
								self._download()
							else:
								message_dialog(
									title=Messages.title,
									text=HTML(
										f"Membuka tautan <ansigreen>{selected_host}</ansigreen> pada browser."
									),
									style=self.theme,
								).run()
								os.system(f"start {selected_host}")
								exit()

	def _search(self):
		result = input_dialog(
			title=Messages.title,
			text=HTML("Mohon masukkan judul anime yang ingin kamu cari di Otakudesu."),
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

		data = LoadingTask(Messages.title, result, OtakudesuSearch)
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
			message_dialog(
				title=Messages.title,
				text=HTML(f"Sayonara <ansiyellow>{username}</ansiyellow>!"),
				style=self.theme,
			).run()
			exit()