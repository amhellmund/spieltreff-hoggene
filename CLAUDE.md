# spieltreff-hoggene

Static website for the Spieltreff Hoggene board-game club. Jinja2 templates
(`templates/`) and YAML data (`data/`) are rendered by `build.py` /
`generator/` into static HTML in `.build/`.

## Build

```
uv run build-page
```

Every change must be verified by running `build-page` successfully before
being considered done.
