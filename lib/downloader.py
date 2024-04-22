import os
import shutil
import requests

from rich.console import Group
from rich.panel import Panel
from rich.live import Live
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
)

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class MangaDownloader:
    def __init__(self, data: dict = None):
        self.data = data

        self.current_app_progress = Progress(
            TimeElapsedColumn(),
            TextColumn("{task.description}"),
        )

        self.steps_progress = Progress(
            TextColumn("  "),
            TimeElapsedColumn(),
            TextColumn("[bold purple]{task.description}"),
            SpinnerColumn("aesthetic"),
        )

        self.app_steps_progress = Progress(
            TextColumn("[bold blue]Mengunduh {task.fields[name]}: {task.percentage:.0f}%"),
            BarColumn(),
            TextColumn("({task.completed} dari {task.total} halaman selesai)"),
        )

        self.overall_progress = Progress(
            TimeElapsedColumn(), BarColumn(), TextColumn("{task.description}")
        )

        self.progress_group = Group(
            Panel(
                Group(self.current_app_progress, self.steps_progress, self.app_steps_progress)
            ),
            self.overall_progress,
        )

    def download_manga(self):
        data = self.data
        try:
            os.mkdir("Downloads")
        except Exception as e:
            pass

        os.chdir("Downloads")

        judul = data[0]["title"].split("Chapter")[0].strip()
        os.mkdir(judul)
        os.chdir(judul)

        overall_task_id = self.overall_progress.add_task("", total=len(data))

        with Live(self.progress_group):
            for idx, chapter in enumerate(data):
                top_descr = "[bold #AAAAAA](%d dari %d chapter terunduh)" % (
                    idx,
                    len(data),
                )
                self.overall_progress.update(overall_task_id, description=top_descr)

                current_task_id = self.current_app_progress.add_task(
                    "Mengunduh %s" % chapter["title"]
                )

                app_steps_task_id = self.app_steps_progress.add_task(
                    "",
                    total=len(chapter["img"]),
                    name=chapter["title"],
                )

                steps_task_id = self.steps_progress.add_task(
                    "Menambahkan gambar pada halaman",
                    total=len(chapter["img"]),
                    name=chapter["title"],
                )

                PDFCanvas = canvas.Canvas(
                    f"{chapter['title']}.pdf", pagesize=A4
                )

                for i, URL in enumerate(chapter["img"]):
                    if "bin" in URL["src"]:
                        continue
                    Name = f"{URL['alt']}.jpeg"
                    with requests.get(URL["src"], stream=True) as IMG:
                        with open(Name, "wb") as output:
                            shutil.copyfileobj(IMG.raw, output)
                            PDFCanvas.drawImage(
                                Name, 0, 0, A4[0], A4[1]
                            )
                            PDFCanvas.showPage()
                            self.steps_progress.update(steps_task_id, advance=1)
                    os.unlink(Name)
                    self.app_steps_progress.update(app_steps_task_id, advance=1)

                PDFCanvas.save()

                self.app_steps_progress.update(
                    app_steps_task_id, visible=False
                )
                self.steps_progress.update(
                    app_steps_task_id, visible=False
                )
                self.current_app_progress.stop_task(current_task_id)
                self.current_app_progress.update(
                    current_task_id,
                    description="[bold green]%s terunduh!" % chapter["title"],
                )

                self.overall_progress.update(overall_task_id, advance=1)

            self.overall_progress.update(
                overall_task_id,
                description="[bold green]%s chapter terunduh, selesai!" % len(data),
            )
            
        return True


