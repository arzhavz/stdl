import re
import os

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
from lib.utils import Validation

from lib.scraper.samehadaku import Samehadaku, SamehadakuSearch

	
class App:
	def __init__(self):
		self.db = Database()
		self.theme = Themes.loads(self.db.read(self.db.id)["user"]["theme"])

	def _download(self, link: str = "nothing"):
		try:
			if link == "nothing":
				link = input_dialog(
					title=Messages.title,
					text=HTML("Mohon masukkan link anime dari Samehadaku.\nExample: <ansimagenta>https://samehadaku.email/anime/sousou-no-frieren/</ansimagenta>"),
					style=self.theme,
				).run()
			
			smhd_regex = re.compile(
				r'^https?://'
				r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
				r'samehadaku|'
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
			
			if link is None:
				self.run_program()
				
			if not Validation(smhd_regex).URL(link):
				message_dialog(
					title=Messages.title,
					text=HTML(
						f"Tautan <ansigreen>{link}</ansigreen> tidak valid!"
					),
					style=self.theme,
				).run()
				self._download()
				
			smhd_data = LoadingTask(Messages.title, link, Samehadaku)
			anim = smhd_data.info
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
				teks = []
				for detail in smhd_data.detail_items:
					teks.append(f"{detail.capitalize().replace('_', ' ')}: {anim['details'][detail]}")

				message_dialog(
					title=Messages.title,
					text=(
						f"{anim['title']}\n\n" + "\n".join(teks)
					),
					style=self.theme,
				).run()
				self._download(link)
			elif result == "download":
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
				elif action == "batch":
					formatnya = radiolist_dialog(
						title=Messages.title,
						text="Silahkan pilih format dari video yang ingin kamu unduh.",
						style=self.theme,
						values=[
							("mp4", "MP4"),
							("mkv", "MKV"),
							("x265", "x265")
						],
					).run()
					if formatnya is None:
						self._download(link)
					res_list: list 
					if formatnya == "mp4":
						res_list = [
							("360p", "360P"),
							("480p", "480P"),
							("MP4HD", "MP4HD"),
							("FULLHD", "FULLHD")
						] 
					elif formatnya == "mkv":
						res_list = [
							("360p", "360P"),
							("480p", "480P"),
							("720p", "720P"),
							("1080p", "1080P")
						] 
					elif formatnya == "x265":
						res_list = [
							("480p", "480P"),
							("720p", "720P"),
							("1080p", "1080P")
						] 
					resonya = radiolist_dialog(
						title=Messages.title,
						text=HTML(
						f"Silahkan pilih resolusi video yang ingin kamu unduh di bawah."
						),
						style=self.theme,
						values=res_list,
					).run()
					if resonya is None:
						self._download(link)
					dl_list = anim["batch"][formatnya][resonya]
					linknya = radiolist_dialog(
						title=Messages.title,
						text=HTML(
						f"Silahkan pilih file hosting yang ingin digunakan."
						),
						style=self.theme,
						values=dl_list,
					).run()
					if linknya is not None:
						os.system(f"start {linknya}")
						return True
					else:
						self._download(link)
				elif action == "episode":
					episode = radiolist_dialog(
						title=Messages.title,
						text="Silahkan pilih episode yang ingin kamu unduh di bawah.",
						style=self.theme,
						values=smhd_data.eps_tuple,
					).run()
					if episode is None:
						self._download(link)
					eps_data = {}
					for ep in anim["episode"]:
						if ep["title"] == episode:
							eps_data = ep
					formatnya = radiolist_dialog(
						title=Messages.title,
						text="Silahkan pilih format dari video yang ingin kamu unduh.",
						style=self.theme,
						values=[
							("mp4", "MP4"),
							("mkv", "MKV"),
							("x265", "x265")
						],
					).run()
					if formatnya is None:
						self._download(link)
					res_list: list 
					if formatnya == "mp4":
						res_list = [
							("360p", "360P"),
							("480p", "480P"),
							("MP4HD", "MP4HD"),
							("FULLHD", "FULLHD")
						] 
					elif formatnya == "mkv":
						res_list = [
							("360p", "360P"),
							("480p", "480P"),
							("720p", "720P"),
							("1080p", "1080P")
						] 
					elif formatnya == "x265":
						res_list = [
							("480p", "480P"),
							("720p", "720P"),
							("1080p", "1080P")
						] 
					resonya = radiolist_dialog(
						title=Messages.title,
						text=HTML(
						f"Silahkan pilih resolusi video yang ingin kamu unduh di bawah."
						),
						style=self.theme,
						values=res_list,
					).run()
					if resonya is None:
						self._download(link)
					dl_list = eps_data["download"][formatnya][resonya]
					linknya = radiolist_dialog(
						title=Messages.title,
						text=HTML(
						f"Silahkan pilih file hosting yang ingin digunakan."
						),
						style=self.theme,
						values=dl_list,
					).run()
					if linknya is not None:
						os.system(f"start {linknya}")
						return True
					else:
						self._download(link)
		except Exception as e:
			message_dialog(
				title=Messages.title,
				text=HTML(f"Terjadi kesalahan: <ansired>{e}</ansired>\nKlik tombol <ansiyellow>OK</ansiyellow> di bawah untuk keluar."),
				style=self.theme
			).run()

	def _search(self):
		result = input_dialog(
			title=Messages.title,
			text=HTML("Mohon masukkan judul anime yang ingin kamu cari di Samehadaku.\nExample: <ansicyan>Frieren</ansicyan>"),
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

		data = LoadingTask(Messages.title, result, SamehadakuSearch)
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

			if url is None:
				return self._search()
				
			self._download(link=url)

	def _single_download(self):
		link = input_dialog(
			title=Messages.title,
			text=HTML("Mohon masukkan link anime dari Samehadaku.\nExample: <ansigreen>https://samehadaku.email/sousou-no-frieren-episode-1/</ansigreen> or <ansiyellow>https://samehadaku.email/batch/sousou-no-frieren-episode-1-28-batch/</ansiyellow>"),
			style=self.theme,
		).run()
			
		smhd_regex = re.compile(
			r'^https?://'
			r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
			r'samehadaku|'
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
			self._single_download()
			
		if link is None:
			self.run_program()
				
		if not Validation(smhd_regex).URL(link):
			message_dialog(
				title=Messages.title,
				text=HTML(
					f"Tautan <ansigreen>{link}</ansigreen> tidak valid!"
				),
				style=self.theme,
			).run()
			self._single_download()
		else:
			data = LoadingTask(Messages.title, link, Samehadaku().get_download_data)
			formatnya = radiolist_dialog(
				title=Messages.title,
				text=HTML(f"Download <ansiyellow>{data[1]}</ansiyellow>\nSilahkan pilih format dari video yang ingin kamu unduh."),
				style=self.theme,
				values=[
					("mp4", "MP4"),
					("mkv", "MKV"),
					("x265", "x265")
				],
			).run()
			if formatnya is None:
				self._single_download()
			res_list: list 
			if formatnya == "mp4":
				res_list = [
					("360p", "360P"),
					("480p", "480P"),
					("MP4HD", "MP4HD"),
					("FULLHD", "FULLHD")
				] 
			elif formatnya == "mkv":
				res_list = [
					("360p", "360P"),
					("480p", "480P"),
					("720p", "720P"),
					("1080p", "1080P")
				] 
			elif formatnya == "x265":
				res_list = [
					("480p", "480P"),
					("720p", "720P"),
					("1080p", "1080P")
				] 
			resonya = radiolist_dialog(
				title=Messages.title,
				text=HTML(
				f"Silahkan pilih resolusi video yang ingin kamu unduh di bawah."
				),
				style=self.theme,
				values=res_list,
			).run()
			if resonya is None:
				self._single_download()
			dl_list = data[0][formatnya][resonya]
			linknya = radiolist_dialog(
				title=Messages.title,
				text=HTML(
				f"Silahkan pilih file hosting yang ingin digunakan."
				),
				style=self.theme,
				values=dl_list,
			).run()
			if linknya is not None:
				os.system(f"start {linknya}")
				return True
			else:
				self._single_download()
			

	def run_program(self):
		uid = self.db.id
		data = self.db.read(uid)
		username = data["user"]["name"]
		result = radiolist_dialog(
			title=Messages.title,
			text=HTML(
				f"Halo <ansiyellow>{username}</ansiyellow>, silahkan pilih menu yang tersedia di bawah."
			),
			style=self.theme,
			values=[
				("download", "Download Anime"),
				("download_batch", "Download Batch"),
				("download_eps", "Download Eps"),
				("search", "Search"),
				("exit", "Exit"),
			],
		).run()
		if result == "search":
			self._search()
		elif result == "download":
			self._download()
		elif result == "download_batch" or result == "download_eps":
			self._single_download()
		elif result == "exit":
			return message_dialog(
				title=Messages.title,
				text=HTML(f"Sayonara <ansiyellow>{username}</ansiyellow>!"),
				style=self.theme,
			).run()
		