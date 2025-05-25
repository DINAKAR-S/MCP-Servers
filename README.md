```markdown
# HR Management MCP Server Suite

This repository contains two versions of an **HR Management Micro Control Program (MCP) server** built with Python, designed for conversational interfaces and intelligent automation. The two variants are:

- `server_claude_desktop`: Designed for integration with **Claude Desktop**
- `server_cursor_ide`: Designed for use within **Cursor IDE's MCP environment**

---

## 📁 Repository Structure

```

.
├── server\_claude\_desktop/
│   ├── main.py
│   ├── .venv/
│   ├── README.md
│   └── other project files
├── server\_cursor\_ide/
│   ├── main.py
│   ├── .venv/
│   ├── README.md
│   └── other project files
└── README.md

````

---

## 🧠 Project Features (Common to Both Servers)

- ✅ View employee leave balance
- ✅ Apply leave for employees
- ✅ Grant salary hikes
- ✅ Update employee roles
- ✅ Get summarized employee details
- ✅ Built with `FastMCP` (or equivalent MCP toolset)
- ✅ Uses dummy employee data for simulation

---

## 🖥️ Server 1: Claude Desktop MCP Server

### 📍 Path
```bash
server_claude_desktop/main.py
````

### 🔧 Setup Steps

1. Create virtual environment

   ```bash
   cd Server 1 Cluade Desktop
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install MCP tools

   ```bash
   pip install mcp[cli]
   pip install typer
   ```

3. Install the MCP server

   ```bash
   uv run mcp install main.py
   ```

4. Open Claude Desktop and begin asking:

   ```
   > Show leave balance for EMP005
   > Apply 10% hike to EMP001
   > Update role of EMP007 to HR Manager
   ```

---

## 🧑‍💻 Server 2: Cursor IDE MCP Server

### 📍 Path

```bash
server_cursor_ide/main.py
```

### 🔧 Setup Steps

1. Open project in Cursor IDE.
2. Ensure MCP plugin is installed and running.
3. Run MCP server by executing:

   ```bash
   uv run mcp install main.py
   ```
4. Interact with the tools inside the Cursor AI interface.

---

## 📋 Sample Dummy Employee Record

```json
{
  "emp_id": "EMP001",
  "name": "John Doe",
  "role": "Software Engineer",
  "salary": 60000,
  "leave_balance": 15
}
```

---

## 📎 Requirements

* Python 3.10+
* `mcp` CLI or IDE extension
* `typer`, `uv`, `FastMCP` (or compatible MCP package)

---

## 📌 License

This project is for educational and demonstration purposes. Feel free to adapt and extend it as per your use case.

---

## 🤝 Contributions

Pull requests and feedback are welcome. Fork the repo, make your changes, and submit a PR!

---

## 📞 Contact

Maintainer: Dinakar S
