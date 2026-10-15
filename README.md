# CS238 Labs

Weekly labs for **CS238: Intro to Generative AI** at Walla Walla University, taught from the textbook *Illustrating Generative AI*. Each week's lab is a folder with a `README.md` (the directions) and the Python files it asks you to run.

New labs appear here week by week during the quarter.

---

## Getting Started (once, in Week 1)

You'll keep all of this quarter's lab work in one folder, `cs238`, managed by `uv`, a fast all-in-one tool for Python projects.

1. **Skip this step if you're on a campus computer; `uv` is already installed.** On your own laptop, install [uv](https://docs.astral.sh/uv/). On macOS or Linux:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   On Windows (PowerShell):
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
   Then close the terminal and open a new one so the `uv` command is found.
2. Install the Python version the course uses. `uv` downloads and manages it for you, separate from any other Python on your machine:
   ```bash
   uv python install 3.13
   ```
3. Make a folder for the course and turn it into a `uv` project that uses Python 3.13:
   ```bash
   mkdir cs238
   ```
   ```bash
   cd cs238
   ```
   ```bash
   uv init --python 3.13 --vcs none
   ```
4. Download the labs into your course folder:
   ```bash
   git clone https://github.com/abuach/cs238-labs
   ```
5. Install every Python package the labs use (including the book's companion library, `genai`) and point `genai` at the class Ollama server, `ollama2.cs.wallawalla.edu`. The models all live on that server, so there's nothing big to download.

   On a campus computer (Linux), run the setup script, then load the new setting into the terminal you have open:
   ```bash
   bash cs238-labs/setup.sh
   ```
   ```bash
   source ~/.bashrc
   ```
   The script installs everything in `cs238-labs/requirements.txt` and adds `OLLAMA_HOST`, the variable Ollama's tools (and `genai`) read to find their server, to your `~/.bashrc`, so every new terminal picks it up automatically. It's safe to run again.

   On your own laptop (macOS or Windows), do the same two things by hand. First install the packages:
   ```bash
   uv add -r cs238-labs/requirements.txt
   ```
   Then set `OLLAMA_HOST`. On macOS:
   ```bash
   echo 'export OLLAMA_HOST=http://ollama2.cs.wallawalla.edu:11434' >> ~/.zshrc
   ```
   On Windows (PowerShell):
   ```bash
   setx OLLAMA_HOST "http://ollama2.cs.wallawalla.edu:11434"
   ```
   Then **close the terminal, open a new one, and `cd` back into `cs238`**.
<!--
6. Check which server `genai` will use (the first run takes a little while):
   ```bash
   uv run python -c "from genai import get_host; print(get_host())"
   ```
   It should print `http://ollama2.cs.wallawalla.edu:11434`.
-->

The class server is shared, so please follow the [server guidelines](https://github.com/abuach/genai-course-public/blob/main/resources/ollama-server-guidelines.md).

---

## Every Week

1. Get the new lab. From your `cs238` folder:
   ```bash
   cd cs238-labs
   ```
   ```bash
   git pull
   ```
   **Or, in VS Code:** open your `cs238` folder (File → Open Folder), then open the Command Palette (Ctrl+Shift+P), type `Git: Pull`, and press Enter. You can also click the Source Control icon on the left (Ctrl+Shift+G), open the `···` menu, and choose **Pull**. If it lists more than one repository, pick `cs238-labs`.
2. Install anything new the labs need (it's quick when nothing has changed):
   ```bash
   uv add -r requirements.txt
   ```
   If you pulled in VS Code, open its terminal (Terminal → New Terminal), which starts in your `cs238` folder, and run this instead:
   ```bash
   uv add -r cs238-labs/requirements.txt
   ```
3. Go into the week's folder and follow its `README.md`. For example:
   ```bash
   cd week02
   ```
4. Run each script from inside that folder with `uv run`:
   ```bash
   uv run temperature.py
   ```

A few things that hold for every lab:

- **Edit only your files.** Files whose names start with `my_` are yours to change, and so is each week's results file (`lab1_results.txt`, `lab2_results.txt`, …). Leave the other files as they are, so `git pull` never trips over your edits.
- **Charts** open in their own window and are also saved as a `.png` in the week's folder. Close the chart window to let the script continue.
- **Model output changes from run to run**, so your answers won't match the book word for word. What should hold is the *shape* of each result.
- **Submit** your results file on D2L/Brightspace each week. If you worked with a partner, both partners upload a copy.

---

## Working Off Campus

The class server may only be reachable from the campus network. Off campus, either connect to the university VPN, or run the models on your own laptop instead:

1. Install [Ollama](https://ollama.com) and open the app.
2. Point this terminal (just this one) back at your laptop. On macOS or Linux:
   ```bash
   export OLLAMA_HOST=http://localhost:11434
   ```
   On Windows (PowerShell):
   ```bash
   $env:OLLAMA_HOST = "http://localhost:11434"
   ```
3. Download the week's models from the schedule below, for example:
   ```bash
   ollama pull gemma4
   ```

Run `ollama pull` *after* step 2. Otherwise `ollama` sends the download to the class server instead of your laptop. A new terminal goes back to the class server automatically.

To switch servers inside a single script instead, put these two lines at the top: `from genai import set_host` and `set_host("http://localhost:11434")`.

---

## Ollama Model Schedule

The models each lab uses are all on the class server; the optional extras may not be. If you're working locally, pull the models for the week you're on. Sizes are approximate downloads.

| Week | Lab dates | Topic | Models the lab uses | Optional extras |
|---|---|---|---|---|
| 1 | Sep 29 & Oct 1 | The Prediction Machine | `gemma4` (10 GB), `llama3.2` (2 GB) | `llama3.2:1b` (1.3 GB) |
| 2 | Oct 6 & 8 | Prompting | `gemma4`, `llama3.2` | |
| 3 | Oct 13 & 15 | Tokens | `gemma4` | |
| 4 | Oct 20 & 22 | Semantics | `nomic-embed-text` (0.3 GB) | `gemma4` |
| 5 | Oct 27 & 29 | Retrieval-Augmented Generation | `gemma4`, `nomic-embed-text` | |
| 6 | Nov 3 & 5 | Giving the Model Hands | `gemma4` | `qwen3` (5.2 GB), `llama3.2` |
| 7 | Nov 10 & 12 | Thinking Models | `qwen3:4b` (2.5 GB), `qwen2.5-coder` (4.7 GB) | `deepseek-r1` (5 GB) |
| 8 | Nov 17 & 19 | Giving the Model Eyes | `gemma4` | `llava` (4.7 GB) |
| 9 | Nov 24 | Where Did the Time Go? | **runs on your own laptop:** `llama3.2`, `llama3.2:1b`, `qwen3:4b` | `llama3.2:1b-instruct-q4_K_M`, `-q8_0`, `-fp16` |
| 10 | Dec 1 & 3 | Break It, Then Guard It | `gemma4:e2b` (4.6 GB), `gemma4`, `llama3.2`, `nomic-embed-text` | |

A few optional exercises also download a model to your laptop the first time they run (BERT in Week 1, for example). Each lab says when.
