# 🌳 Radix

> "Start every project from its Radix."

A foundational template application built with the [Textual](https://github.com/Textualize/textual) TUI framework, designed to serve as a starting point for terminal-based user interface projects.

---

## 🚀 Getting Started

### Installation

**1. Install Core Dependencies (Required)**

Install Textual with syntax highlighting support powered by Tree-sitter:

```bash
pip install textual "textual[syntax]"
```

**2. Install Development Tools (Optional)**

For development and debugging workflows, install the Textual developer tools:

```bash
pip install textual-dev
```

---

## 📦 Building a Executable

You can compile this project into a single, portable executable using [Nuitka](https://nuitka.net/).

### Build Instructions

**1. Install Nuitka**

```bash
pip install nuitka
```

**2. Compile the Application**

Due to Textual's dynamic loading of Tree-sitter language parsers for syntax highlighting, all language packages must be explicitly included during compilation.

Choose the appropriate command for your platform:

#### Windows
```bash
nuitka main.py --onefile \
--windows-icon-from-ico=icons/icon.ico \
```

#### macOS
```bash
nuitka main.py --standalone \
--macos-create-app-bundle \
--macos-app-icon=icons/icon.icns \
```

#### Linux (No Icon)
```bash
nuitka main.py --onefile \
```

**Add these common flags to all platforms:**

```bash
--output-dir=build \
--output-filename=radix \
--include-package=Pygments \
--include-package=rich \
--include-package=textual \
--include-package=tree_sitter \
--include-package=tree_sitter_bash \
--include-package=tree_sitter_css \
--include-package=tree_sitter_go \
--include-package=tree_sitter_html \
--include-package=tree_sitter_java \
--include-package=tree_sitter_javascript \
--include-package=tree_sitter_json \
--include-package=tree_sitter_markdown \
--include-package=tree_sitter_python \
--include-package=tree_sitter_regex \
--include-package=tree_sitter_rust \
--include-package=tree_sitter_sql \
--include-package=tree_sitter_toml \
--include-package=tree_sitter_xml \
--include-package=tree_sitter_yaml
```

**Output:** The compiled executable will be generated in the `build` directory:
- Windows: `radix.exe`
- macOS: `radix.app` (application bundle)
- Linux: `radix`

---

## ⚙️ Platform-Specific Configuration

### Windows: Enable Long Path Support

Windows restricts file paths to 260 characters by default, which can cause issues when compiling projects with deeply nested dependencies. To prevent build failures, enable Long Path support:

**Steps:**

1. Open the Registry Editor by running `regedit` as Administrator
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
3. Locate the `LongPathsEnabled` entry
4. Change its value from `0` to `1` (Hexadecimal)
5. Restart your computer for changes to take effect

> **⚠️ Warning:** Modifying the Windows Registry can affect system stability. Always create a backup before making changes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

This project uses [Textual](https://github.com/Textualize/textual), which is also licensed under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

For questions or support, please open an issue in this repository.

---

**Built with [Textual](https://github.com/Textualize/textual) • A modern framework for building TUI applications**