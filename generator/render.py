"""Jinja2 environment setup and per-page render/write helpers."""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / ".build"

_env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))


def render_page(template_name, output_filename, site, nav, footer, **extra_context):
    template = _env.get_template(f"pages/{template_name}")
    depth = output_filename.count("/")
    html = template.render(
        site=site,
        nav=nav,
        footer=footer,
        current_page=output_filename,
        asset_prefix="../" * depth,
        page_title=extra_context.pop("page_title", None),
        **extra_context,
    )
    output_path = OUTPUT_DIR / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"wrote {output_filename}")
