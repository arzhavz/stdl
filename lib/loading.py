import random
from datetime import datetime
from time import sleep

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.live import Live
from rich.markdown import Markdown

console = Console()
    
class LoadingMonitor:
    def __init__(self, name: str = None):
        self.layout = self.make_layout()
        self.job_progress = self.make_job_progress()
        self.overall_progress = self.make_overall_progress()
        self.name = name

    def make_layout(self) -> Layout:
        """Define the layout."""
        layout = Layout(name="root")

        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=7),
        )
        layout["main"].split_row(
            Layout(name="side"),
            Layout(name="body", ratio=2, minimum_size=60),
        )
        layout["side"].split(Layout(name="box1"), Layout(name="box2"))
        return layout

    def make_sponsor_message(self) -> Panel:
        """Some example content."""
        sponsor_message = Table.grid(padding=1)
        sponsor_message.add_column(no_wrap=True)
        sponsor_message.add_row(
            """[blink][yellow]
			Arigatou, sayonara.
			[/]""",
        )

        message = Table.grid(padding=1)
        message.add_column()
        message.add_column(no_wrap=True)
        message.add_row(sponsor_message)

        message_panel = Panel(
            Align.center(
                Group("\n", Align.center(sponsor_message)),
                vertical="middle",
            ),
            box=box.ROUNDED,
            padding=(1, 2),
            title=f"[b red]Hello {self.name} ><",
            border_style="bright_blue",
        )
        return message_panel

    def make_job_progress(self) -> Progress:
        job_progress = Progress(
            "{task.description}",
            SpinnerColumn(),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        job_progress.add_task("[green]Building ...", total=13)
        job_progress.add_task("[yellow]Initializing ...", total=24)
        job_progress.add_task("[blue]Loading ...", total=43)
        return job_progress

    def make_overall_progress(self) -> Progress:
        total = sum(task.total for task in self.job_progress.tasks)
        overall_progress = Progress()
        overall_task = overall_progress.add_task("All Progress", total=int(total))
        return overall_progress, overall_task

    def make_syntax(self) -> Syntax:
        code = """\
class Transformer(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout):
        super(Transformer, self).__init__()
        self.multihead_attention = nn.MultiheadAttention(d_model, n_heads, dropout=dropout)
        self.dropout1 = nn.Dropout(p=dropout)
        self.layer_norm1 = nn.LayerNorm(d_model)
        
        self.feed_forward = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            nn.Linear(d_ff, d_model)
        )
        self.dropout2 = nn.Dropout(p=dropout)
        self.layer_norm2 = nn.LayerNorm(d_model)
        
    def forward(self, x):
        attn_output, _ = self.multihead_attention(x, x, x)
        x = x + self.dropout1(attn_output)
        x = self.layer_norm1(x)
        
        ff_output = self.feed_forward(x)
        x = x + self.dropout2(ff_output)
        x = self.layer_norm2(x)
        
        return x
        """
        syntax = Syntax(code, "python", line_numbers=True)
        return syntax

    def update_progress(self):
        while not self.overall_progress[0].finished:
            sleep(0.1)
            for job in self.job_progress.tasks:
                if not job.finished:
                    self.job_progress.advance(job.id)

            completed = sum(task.completed for task in self.job_progress.tasks)
            self.overall_progress[0].update(self.overall_progress[1], completed=completed)

    def start_monitoring(self):
        self.layout["header"].update(self.Header())
        self.layout["body"].update(self.make_sponsor_message())
        self.layout["box2"].update(Panel(self.make_syntax(), border_style="green"))
        self.layout["box1"].update(Panel(self.layout.tree, border_style="red"))
        self.layout["footer"].update(self.make_progress_table())

        with Live(self.layout, refresh_per_second=10, screen=True):
            self.update_progress()

    class Header:
        """Display header with clock."""

        def __rich__(self) -> Panel:
            grid = Table.grid(expand=True)
            grid.add_column(justify="center", ratio=1)
            grid.add_column(justify="right")
            grid.add_row(
                "[b]STDL - Scraping Tools and Downloader[/b]",
                datetime.now().ctime().replace(":", "[blink]:[/]"),
            )
            return Panel(grid, style="white on magenta")

    def make_progress_table(self):
        progress_table = Table.grid(expand=True)
        progress_table.add_row(
            Panel(
                self.overall_progress[0],
                title="Overall Progress",
                border_style="green",
                padding=(2, 2),
            ),
            Panel(self.job_progress, title="[b]Progress", border_style="red", padding=(1, 2)),
        )
        return progress_table

    
def LoadingTask(ver, task_input, task):
    #console.print(Markdown(f"# {ver}"), style="bold cyan")
    with console.status(f"[bold yellow]Loading, please wait a minute [blink]...[/]", spinner=random.choice(["aesthetic", "shark", 'pong', 'material'])) as status:
        while True:
            data = task(task_input)
            return data