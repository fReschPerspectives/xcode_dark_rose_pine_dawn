# xcode_dark_rose_pine_dawn
VS Code theme with xcode dark ui elements but a rose pine style editor pane

## Making text bold

There are two ways to make text bold in VS Code when using this theme:

1) Global editor font weight (all editor text)

- Open your user or workspace settings (Ctrl+,)
- Add or update this setting:

```json
"editor.fontWeight": "bold"
```

Note: The font you are using must include a bold weight to see a difference. If it doesn't, use a font with bold support or choose a numeric weight like "600".

2) Bold specific syntax tokens (keywords, functions, etc.)

- This theme already sets common scopes to bold (Keywords, Function Names, and Class Names). If you want to tweak or add more rules, use the VS Code `editor.tokenColorCustomizations` in your settings or modify the theme's `tokenColors` entry. Example for settings:

```json
"editor.tokenColorCustomizations": {
	"textMateRules": [
		{
			"scope": "keyword",
			"settings": {
				"fontStyle": "bold"
			}
		}
	]
}
```

Or edit `themes/xcode-dark-rose-pine-dawn.json` and add `"fontStyle": "bold"` to the token you want to emphasize.

After changes, reload the window (Developer: Reload Window) and verify the theme is active.
