# Copilot Instructions for This Codebase

## Overview
This project is a collection of HTML and CSS files, organized into folders by topic and language (e.g., "French site", "Week 2"). It appears to be an educational or portfolio project, possibly for language learning or interactive books.

## Key Structure
- **Top-level HTML files**: `html pic book 1.html`, `html pic book 2.html`, etc. Each is a standalone HTML page, likely with its own visual or interactive content.
- **French site/**: Contains a subfolder `style.css/` (despite the name, this is a directory), which holds HTML files and an `images/` directory with assets (PNG, JPG) and more HTML files. CSS is likely embedded or inlined, as no `.css` file is visible.
- **French tokens/**: Contains Python scripts, suggesting some automation or tokenization related to the French content.
- **Week 2/Week 3/**: Contain HTML and documentation files, possibly for weekly assignments or modules.

## Patterns & Conventions
- **No build system**: Files are static; open HTML files directly in a browser for preview. No npm, Python, or other build/test commands are required.
- **CSS organization**: CSS is embedded in HTML or in misnamed folders (e.g., `style.css/`). There is no global stylesheet; styles are per-page or per-folder.
- **Image usage**: Images are referenced from `French site/style.css/images/`.
- **Animations**: Custom CSS animations (e.g., `.archi` uses `@keyframes float`) are used for visual effects.
- **No JavaScript detected**: All interactivity is via CSS or HTML.

## How to Extend or Edit
- To add a new page, copy an existing HTML file and update its content.
- To add images, place them in the relevant `images/` folder and reference with a relative path.
- To update styles, edit the `<style>` block in the HTML file or the relevant CSS in the folder.

## Examples
- The `.archi` class in CSS creates a floating, rounded rectangle (see attached CSS for details).
- The `book-container` and `illustration` classes are used for layout and visual grouping.

## Recommendations for AI Agents
- When generating new HTML/CSS, follow the folder structure and naming conventions (e.g., place French content in `French site/`).
- Avoid introducing build tools or frameworks unless explicitly requested.
- Use relative paths for images and assets.
- If adding Python scripts, place them in the `French tokens/` directory.

## Key Files & Directories
- `html pic book 1.html`, `html pic book 2.html`, ...: Main HTML pages
- `French site/style.css/images/`: Image assets and additional HTML files
- `French tokens/`: Python scripts for tokenization or automation
- `Week 2/`, `Week 3/`: Weekly content and documentation

---
If any section is unclear or missing important project-specific details, please provide feedback for further refinement.
