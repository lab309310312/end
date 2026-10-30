# Interactive Web Projects

A collection of 5 standalone, frontend applications developed with vanilla HTML5, CSS3, and modern JavaScript (ES6+). Each project is self-contained with its own markup, styling, and logic.

## Projects Summary

| Project | Name | Description | Key Features |
|---|---|---|---|
| [`01-portfolio/`](01-portfolio/) | Developer Portfolio | Personal academic and project portfolio | Dynamic typewriter effect, responsive navigation menu, animated skill bars, contact form validation |
| [`02-task-board/`](02-task-board/) | Task Board App | Interactive productivity task tracker | Priority tagging (Low / Medium / High), status filtering (All / Active / Done), persistent storage via `localStorage` |
| [`03-calculator/`](03-calculator/) | Web Calculator | Functional arithmetic calculator | Operations (`+`, `-`, `*`, `/`), percentages, decimal calculations, backspace deletion, display history |
| [`04-chai-and-co-menu/`](04-chai-and-co-menu/) | Chai & Co. Menu | Cafe / restaurant ordering interface | Category filtering tabs (Tea, Snacks, Sweets), real-time search, interactive cart drawer with live subtotal calculation |
| [`05-networking-quiz/`](05-networking-quiz/) | Networking Quiz | Timed computer networking quiz | 5 networking questions, 15-second per-question countdown timer, animated progress bar, instant feedback, score calculation |

## How to Run
All projects run directly in any modern browser without requiring build steps or external dependencies.
Simply double-click the `index.html` file inside any project folder, or serve locally with:

```bash
# Using Python's built-in HTTP server:
python -m http.server 8000
```
Then navigate to `http://localhost:8000/web-projects/<project-folder>/`.
