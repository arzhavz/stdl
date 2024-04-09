from prompt_toolkit.styles import Style


class Themes:
	dark_default = Style.from_dict(
		{
			# Main background color
			"window": "bg:#1d1f21 #ffffff",
			# Dialog and message box color
			"dialog": "bg:#1d1f21",
			"dialog.border": "bg:#c5c8c6",
			"dialog.body": "bg:#1d1f21 #ffffff",
			"dialog.title": "bg:#1d1f21 #c5c8c6",
			"dialog shadow": "bg:#1d1f21",
			# Button color
			"button": "bg:#373b41 #ffffff",
			"button.border": "bg:#c5c8c6",
			"button.focus": "bg:#1d1f21 #c5c8c6",
			"button.selected": "bg:#373b41 #ffffff",
			"button.selected.border": "bg:#c5c8c6",
			"button.disabled": "bg:#373b41 #999999",
			# Label and frame color
			"frame.label": "bg:#1d1f21 #c5c8c6",
			"frame.border": "bg:#1d1f21 #c5c8c6",
			# Menu color
			"menu-bar": "bg:#1d1f21 #c5c8c6",
			"menu": "bg:#1d1f21 #ffffff",
			"menu.border": "bg:#1d1f21 #c5c8c6",
			"menu.shadow": "bg:#1d1f21",
			"selected-menu-item": "bg:#373b41 #ffffff",
			"separator": "bg:#c5c8c6",
			# Radio color
			"radio": "bg:#1d1f21 #c5c8c6",
			"radio.border": "bg:#c5c8c6",
			"radio.focus": "bg:#1d1f21 #c5c8c6",
			"radio.selected": "bg:#373b41 #c5c8c6",
			"radio.selected.border": "bg:#c5c8c6",
			"radio.disabled": "bg:#1d1f21 #999999",
			# Input
			"text-area": "bg:#1d1f21 #c5c8c6",
			"text-area.border": "bg:#c5c8c6",
			"text-area.focus": "bg:#1d1f21 #c5c8c6",
			"text-area.cursor": "fg:#c5c8c6 bg:#c5c8c6",
			"text-area.selection": "bg:#373b41 #c5c8c6",
			"text-area.line": "bg:#1d1f21",
			"text-area.prompt": "fg:#c5c8c6",
			"text-area.status-bar": "bg:#1d1f21 #c5c8c6",
			"text-area.status-bar.current-position": "bg:#373b41 #c5c8c6",
			"text-area.status-bar.mode": "bg:#1d1f21 #c5c8c6 fg:#c5c8c6",
		}
	)
	dark_green = Style.from_dict(
		{
			# Main background color
			"window": "bg:#000000 #00ff00",
			# Dialog and message box color
			"dialog": "bg:#000000",
			"dialog.border": "bg:#00ff00",
			"dialog.body": "bg:#000000 #00ff00",
			"dialog.title": "bg:#000000 #00ff00",
			"dialog shadow": "bg:#000000",
			# Button color
			"button": "bg:#000000 #00ff00",
			"button.border": "bg:#00ff00",
			"button.focus": "bg:#000000 #00ff00",
			"button.selected": "bg:#000000 #00ff00",
			"button.selected.border": "bg:#00ff00",
			"button.disabled": "bg:#000000 #999999",
			# Label and frame color
			"frame.label": "bg:#000000 #00ff00",
			"frame.border": "bg:#000000 #00ff00",
			# Menu color
			"menu-bar": "bg:#000000 #00ff00",
			"menu": "bg:#000000 #00ff00",
			"menu.border": "bg:#000000 #00ff00",
			"menu.shadow": "bg:#000000",
			"selected-menu-item": "bg:#000000 #00ff00",
			"separator": "bg:#00ff00",
			# Radio color
			"radio": "bg:#000000 #00ff00",
			"radio.border": "bg:#00ff00",
			"radio.focus": "bg:#000000 #00ff00",
			"radio.selected": "bg:#000000 #00ff00",
			"radio.selected.border": "bg:#00ff00",
			"radio.disabled": "bg:#000000 #999999",
			# Input
			"text-area": "bg:#000000 #00ff00",
			"text-area.border": "bg:#00ff00",
			"text-area.focus": "bg:#000000 #00ff00",
			"text-area.cursor": "fg:#00ff00 bg:#00ff00",
			"text-area.selection": "bg:#000000 #00ff00",
			"text-area.line": "bg:#000000",
			"text-area.prompt": "fg:#00ff00",
			"text-area.status-bar": "bg:#000000 #00ff00",
			"text-area.status-bar.current-position": "bg:#000000 #00ff00",
			"text-area.status-bar.mode": "bg:#000000 #00ff00 fg:#00ff00",
		}
	)
	dark_electric_blue = Style.from_dict(
		{
			# Main background color
			"window": "bg:#000000 #00FFFF",
			# Dialog and message box color
			"dialog": "bg:#000000",
			"dialog.border": "bg:#FF00FF",
			"dialog.body": "bg:#000000 #00FFFF",
			"dialog.title": "bg:#000000 #FF00FF",
			"dialog shadow": "bg:#000000",
			# Button color
			"button": "bg:#00FFFF #000000",
			"button.border": "bg:#FF00FF",
			"button.focus": "bg:#000000 #FF00FF",
			"button.selected": "bg:#00FFFF #000000",
			"button.selected.border": "bg:#FF00FF",
			"button.disabled": "bg:#00FFFF #999999",
			# Label and frame color
			"frame.label": "bg:#000000 #FF00FF",
			"frame.border": "bg:#000000 #FF00FF",
			# Menu color
			"menu-bar": "bg:#000000 #FF00FF",
			"menu": "bg:#000000 #00FFFF",
			"menu.border": "bg:#000000 #FF00FF",
			"menu.shadow": "bg:#000000",
			"selected-menu-item": "bg:#00FFFF #000000",
			"separator": "bg:#FF00FF",
			# Radio color
			"radio": "bg:#000000 #FF00FF",
			"radio.border": "bg:#FF00FF",
			"radio.focus": "bg:#000000 #FF00FF",
			"radio.selected": "bg:#00FFFF #FF00FF",
			"radio.selected.border": "bg:#FF00FF",
			"radio.disabled": "bg:#000000 #999999",
			# Input
			"text-area": "bg:#000000 #FF00FF",
			"text-area.border": "bg:#FF00FF",
			"text-area.focus": "bg:#000000 #FF00FF",
			"text-area.cursor": "fg:#FF00FF bg:#FF00FF",
			"text-area.selection": "bg:#00FFFF #FF00FF",
			"text-area.line": "bg:#000000",
			"text-area.prompt": "fg:#FF00FF",
			"text-area.status-bar": "bg:#000000 #FF00FF",
			"text-area.status-bar.current-position": "bg:#00FFFF #FF00FF",
			"text-area.status-bar.mode": "bg:#000000 #FF00FF fg:#FF00FF",
		}
	)
	backrooms = Style.from_dict(
		{
			# Main background color
			"window": "bg:#39f52c #000000",
			# Dialog and message box color
			"dialog": "bg:#39f52c",
			"dialog.border": "bg:#000000",
			"dialog.body": "bg:#39f52c #000000",
			"dialog.title": "bg:#39f52c #000000",
			"dialog shadow": "bg:#39f52c",
			# Button color
			"button": "bg:#222222 #00ff00",
			"button.border": "bg:#00ff00",
			"button.focus": "bg:#39f52c #00ff00",
			"button.selected": "bg:#222222 #00ff00",
			"button.selected.border": "bg:#00ff00",
			"button.disabled": "bg:#222222 #999999",
			# Label and frame color
			"frame.label": "bg:#39f52c #000000",
			"frame.border": "bg:#39f52c #000000",
			# Menu color
			"menu-bar": "bg:#39f52c #000000",
			"menu": "bg:#39f52c #000000",
			"menu.border": "bg:#39f52c #000000",
			"menu.shadow": "bg:#39f52c",
			"selected-menu-item": "bg:#222222 #000000",
			"separator": "bg:#000000",
			# Radio color
			"radio": "bg:#39f52c #000000",
			"radio.border": "bg:#000000",
			"radio.focus": "bg:#39f52c #000000",
			"radio.selected": "bg:#222222 #000000",
			"radio.selected.border": "bg:#000000",
			"radio.disabled": "bg:#39f52c #999999",
			# Input
			"text-area": "bg:#39f52c #000000",
			"text-area.border": "bg:#000000",
			"text-area.focus": "bg:#39f52c #000000",
			"text-area.cursor": "fg:#000000 bg:#000000",
			"text-area.selection": "bg:#222222 #000000",
			"text-area.line": "bg:#39f52c",
			"text-area.prompt": "fg:#000000",
			"text-area.status-bar": "bg:#39f52c #000000",
			"text-area.status-bar.current-position": "bg:#222222 #000000",
			"text-area.status-bar.mode": "bg:#39f52c #000000 fg:#000000",
		}
	)
	dark_pink = Style.from_dict(
		{
			# Main background color
			"window": "bg:#1d1f21 #ffffff",
			# Dialog and message box color
			"dialog": "bg:#1d1f21",
			"dialog.border": "bg:#c5c8c6",
			"dialog.body": "bg:#1d1f21 #ffffff",
			"dialog.title": "bg:#1d1f21 #c5c8c6",
			"dialog shadow": "bg:#ff6ec7",  
			# Button color
			"button": "bg:#ff6ec7 #ffffff", 
			"button.border": "bg:#c5c8c6",
			"button.focus": "bg:#1d1f21 #c5c8c6",
			"button.selected": "bg:#ff6ec7 #ffffff",
			"button.selected.border": "bg:#c5c8c6",
			"button.disabled": "bg:#373b41 #999999",
			# Label and frame color
			"frame.label": "bg:#1d1f21 #c5c8c6",
			"frame.border": "bg:#1d1f21 #c5c8c6",
			# Menu color
			"menu-bar": "bg:#1d1f21 #c5c8c6",
			"menu": "bg:#1d1f21 #ffffff",
			"menu.border": "bg:#1d1f21 #c5c8c6",
			"menu.shadow": "bg:#ff6ec7",  
			"selected-menu-item": "bg:#ff6ec7 #ffffff",
			"separator": "bg:#c5c8c6",
			# Radio color
			"radio": "bg:#1d1f21 #c5c8c6",
			"radio.border": "bg:#c5c8c6",
			"radio.focus": "bg:#1d1f21 #c5c8c6",
			"radio.selected": "bg:#ff6ec7 #c5c8c6",
			"radio.selected.border": "bg:#c5c8c6",
			"radio.disabled": "bg:#1d1f21 #999999",
			# Input
			"text-area": "bg:#1d1f21 #c5c8c6",
			"text-area.border": "bg:#c5c8c6",
			"text-area.focus": "bg:#1d1f21 #c5c8c6",
			"text-area.cursor": "fg:#c5c8c6 bg:#c5c8c6",
			"text-area.selection": "bg:#ff6ec7 #c5c8c6",
			"text-area.line": "bg:#1d1f21",
			"text-area.prompt": "fg:#ff6ec7",  
			"text-area.status-bar": "bg:#1d1f21 #c5c8c6",
			"text-area.status-bar.current-position": "bg:#ff6ec7 #c5c8c6",
			"text-area.status-bar.mode": "bg:#1d1f21 #c5c8c6 fg:#ff6ec7",  
		}
	)	
	dark_yellow = Style.from_dict(
		{
			# Main background color
			"window": "bg:#1d1f21 #ffffff",
			# Dialog and message box color
			"dialog": "bg:#1d1f21",
			"dialog.border": "bg:#c5c8c6",
			"dialog.body": "bg:#1d1f21 #ffffff",
			"dialog.title": "bg:#1d1f21 #c5c8c6",
			"dialog shadow": "bg:#ffd700", 
			# Button color
			"button": "bg:#ffd700 #ffffff",  
			"button.border": "bg:#c5c8c6",
			"button.focus": "bg:#1d1f21 #c5c8c6",
			"button.selected": "bg:#ffd700 #ffffff", 
			"button.selected.border": "bg:#c5c8c6",
			"button.disabled": "bg:#373b41 #999999",
			# Label and frame color
			"frame.label": "bg:#1d1f21 #c5c8c6",
			"frame.border": "bg:#1d1f21 #c5c8c6",
			# Menu color
			"menu-bar": "bg:#1d1f21 #c5c8c6",
			"menu": "bg:#1d1f21 #ffffff",
			"menu.border": "bg:#1d1f21 #c5c8c6",
			"menu.shadow": "bg:#ffd700",  
			"selected-menu-item": "bg:#ffd700 #ffffff",  
			"separator": "bg:#c5c8c6",
			# Radio color
			"radio": "bg:#1d1f21 #c5c8c6",
			"radio.border": "bg:#c5c8c6",
			"radio.focus": "bg:#1d1f21 #c5c8c6",
			"radio.selected": "bg:#ffd700 #c5c8c6", 
			"radio.selected.border": "bg:#c5c8c6",
			"radio.disabled": "bg:#1d1f21 #999999",
			# Input
			"text-area": "bg:#1d1f21 #c5c8c6",
			"text-area.border": "bg:#c5c8c6",
			"text-area.focus": "bg:#1d1f21 #c5c8c6",
			"text-area.cursor": "fg:#c5c8c6 bg:#c5c8c6",
			"text-area.selection": "bg:#ffd700 #c5c8c6", 
			"text-area.line": "bg:#1d1f21",
			"text-area.prompt": "fg:#ffd700",  
			"text-area.status-bar": "bg:#1d1f21 #c5c8c6",
			"text-area.status-bar.current-position": "bg:#ffd700 #c5c8c6", 
			"text-area.status-bar.mode": "bg:#1d1f21 #c5c8c6 fg:#ffd700", 
		}
	)
	dusk = Style.from_dict(
        {
            # Main background color
            "window": "bg:#5c415d #f3e8ee",
            # Dialog and message box color
            "dialog": "bg:#5c415d",
            "dialog.border": "bg:#ffc2c2",
            "dialog.body": "bg:#5c415d #f3e8ee",
            "dialog.title": "bg:#5c415d #ffc2c2",
            "dialog shadow": "bg:#f39c12",  
            # Button color
            "button": "bg:#f39c12 #ffffff", 
            "button.border": "bg:#ffc2c2",
            "button.focus": "bg:#5c415d #ffc2c2",
            "button.selected": "bg:#f39c12 #ffffff",
            "button.selected.border": "bg:#ffc2c2",
            "button.disabled": "bg:#373b41 #999999",
            # Label and frame color
            "frame.label": "bg:#5c415d #ffc2c2",
            "frame.border": "bg:#5c415d #ffc2c2",
            # Menu color
            "menu-bar": "bg:#5c415d #ffc2c2",
            "menu": "bg:#5c415d #f3e8ee",
            "menu.border": "bg:#5c415d #ffc2c2",
            "menu.shadow": "bg:#f39c12",  
            "selected-menu-item": "bg:#f39c12 #ffffff",
            "separator": "bg:#ffc2c2",
            # Radio color
            "radio": "bg:#5c415d #ffc2c2",
            "radio.border": "bg:#ffc2c2",
            "radio.focus": "bg:#5c415d #ffc2c2",
            "radio.selected": "bg:#f39c12 #ffc2c2",
            "radio.selected.border": "bg:#ffc2c2",
            "radio.disabled": "bg:#5c415d #999999",
            # Input
            "text-area": "bg:#5c415d #ffc2c2",
            "text-area.border": "bg:#ffc2c2",
            "text-area.focus": "bg:#5c415d #ffc2c2",
            "text-area.cursor": "fg:#ffc2c2 bg:#ffc2c2",
            "text-area.selection": "bg:#f39c12 #ffc2c2",
            "text-area.line": "bg:#5c415d",
            "text-area.prompt": "fg:#f39c12",  
            "text-area.status-bar": "bg:#5c415d #ffc2c2",
            "text-area.status-bar.current-position": "bg:#f39c12 #ffc2c2",
            "text-area.status-bar.mode": "bg:#5c415d #ffc2c2 fg:#f39c12",  
        }
    )
	
	def loads(theme: str):
		if theme == "Dark Default": return Themes.dark_default
		elif theme == "Dark Green": return Themes.dark_green
		elif theme == "Dark Electric Blue": return Themes.dark_electric_blue
		elif theme == "Backrooms": return Themes.backrooms
		elif theme == "Dark Pink": return Themes.dark_pink
		elif theme == "Dark Yellow": return Themes.dark_yellow
		elif theme == "Dusk": return Themes.dusk