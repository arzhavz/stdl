import re
import requests

from bs4 import BeautifulSoup as soup
from urllib.parse import quote

from lib.utils import Validation


class Samehadaku:
	"""
	Title: Samehadaku scraper
	Author: Sandy Pratama
	"""
	def __init__(self, url: str = None):
		self.url = url
		self.episodes = []
		self.eps_tuple = []
		self.detail_items = []
		if url is not None:
			self.info = self.scrape()
		
	def _search(self, data, query):
		for d in data:
			found = d.find(string=lambda text: query in str(text))
			if found:
				return d
		
	def get_download_data(self, url) -> dict:
		""" Get download URLs """
		
		struct = {
			"mp4": {},
			"mkv": {},
			"x265": {}
		}
		data = requests.get(url)
		html = soup(data.text, "html.parser")
		article = html.find("article")
		title = article.find("h1").text.strip()
		download_eps = article.find_all("div", {"class": "download-eps"})
			
		download_mp4 = self._search(download_eps, "MP4")
		download_mkv = self._search(download_eps, "MKV")
		download_x265 = self._search(download_eps, "x265")
			
		mp4_reso = download_mp4.find_all("li")
		for mp4_res in mp4_reso:
			struct["mp4"][mp4_res.find("strong").text.strip()] = []
			links = mp4_res.find_all("a")
				
			for link in links:
				struct["mp4"][mp4_res.find("strong").text.strip()].append((link.get("href"), link.text))
			
		mkv_reso = download_mkv.find_all("li")
		for mkv_res in mkv_reso:
			struct["mkv"][mkv_res.find("strong").text.strip()] = []
			links = mkv_res.find_all("a")
				
			for link in links:
				struct["mkv"][mkv_res.find("strong").text.strip()].append((link.get("href"), link.text))
					
		x265_reso = download_x265.find_all("li")
		for x265_res in x265_reso:
			struct["x265"][x265_res.find("strong").text.strip()] = []
			links = x265_res.find_all("a")
				
			for link in links:
				struct["x265"][x265_res.find("strong").text.strip()].append((link.get("href"), link.text))
				
		return (struct, title)
		
	def get_all_eps_data(self) -> dict:
		""" Get all episodes data """
		results = []
		
		for episode in self.episodes:
			data = requests.get(episode[0])
			html = soup(data.text, "html.parser")
			details = {
				"title": episode[1],
				"download": self.get_download_data(episode[0])[0]
			}
			results.append(details)
		return results
	
	def scrape(self) -> dict:
		""" Getting info from url """
		
		try:
			smhd_regex = re.compile(
				r'^https?://'
				r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
				r'samehadaku|'
				r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
				r'(?::\d+)?'
				r'(?:/?|[/?]\S+)$', re.IGNORECASE
			)
			if not Validation(smhd_regex).URL(self.url):
				return {"status": "False", "message": "Invalid URL!"}
			
			data = requests.get(self.url)
			html = soup(data.text, "html.parser")
			article = html.find("article")
			listeps = article.find("div", {"class": "listeps"}).find("ul")
			episodes = listeps.find_all("li")[::-1]
			for episode in episodes:
				eps = episode.find("div", {"class": "epsleft"}).find("a")
				self.episodes.append((eps.get("href"), eps.text))
				self.eps_tuple.append((eps.text, eps.text))
			rating_area = article.find("div", {"class": "rating-area"})
			rating = {"user": "N/A" if rating_area.find("i") is None else rating_area.find("i").text, "rating": "N/A" if rating_area.find("span", {"itemprop": "ratingValue"}) is None else rating_area.find("span", {"itemprop": "ratingValue"}).text}
			genre_info = article.find("div", {"class": "genre-info"}).find_all("a")
			genres = []
			for genre in genre_info:
				genres.append(genre.text.strip())
			anime = article.find("div", {"class": "anime"}).find("div", {"class": "spe"})
			ani = {}
			anim_span = anime.find_all("span")
			for span in anim_span:
				ani[span.find("b").text.strip().lower().replace(" ", "_").replace(":", "")] = span.get_text(separator=' ', strip=True).replace(span.find('b').get_text(separator=' ', strip=True), '').strip()
				self.detail_items.append(span.find("b").text.strip().lower().replace(" ", "_").replace(":", ""))
			batch = article.find("div", {"class": "listbatch"})
			results = {
				"title": article.find("h1").text,
				"details": {
					"rating": f"{rating['rating']} / {rating['user']} users",
					"genre": ", ".join(genres),
					**ani
					
				},
				"batch": self.get_download_data(batch.find("a").get("href"))[0] if batch.find("a") is not None else {},
				"episode": self.get_all_eps_data()
			}
			
			return results
		except Exception as e:
			raise e
		

def SamehadakuSearch(query: str = None) -> dict:
	try:
		results = []
		url = f"https://samehadaku.email/?s={quote(query)}"
		data = requests.get(url)
		html = soup(data.text, "html.parser")
		articles = html.find_all("article")
		for article in articles:
			animposx = article.find("div", {"class": "animposx"})
			a = animposx.find("a")
			results.append((a.get("href"), a.get("title")))
		return results[::-1]
	except Exception as e:
		raise e