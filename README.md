# Smart Campus Information System

<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=36BCF7&height=200&section=header&text=SMART%20CAMPUS&fontSize=70&animation=fadeIn&fontAlignY=35&desc=Academic%20Record%20Management%20%26%20Data%20Analytics%20Integration&descAlignY=55&descSize=20" width="100%" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3500&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Student+Record+Management;Data-Driven+Performance+Insights;Modular+Python+Architecture;Academic+Process+Automation" alt="Typing SVG" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/subhamsje/SMART-CAMPUS-INFORMATION-SYSTEM?style=flat-square&color=36BCF7" alt="Stars" />
  <img src="https://img.shields.io/github/forks/subhamsje/SMART-CAMPUS-INFORMATION-SYSTEM?style=flat-square&color=36BCF7" alt="Forks" />
  <img src="https://img.shields.io/github/last-commit/subhamsje/SMART-CAMPUS-INFORMATION-SYSTEM?style=flat-square&color=36BCF7" alt="Last Commit" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python Version" />
</p>

---

## 🎥 System Demonstration

<p align="center">
  <img src="assets/demo.gif" alt="System Demo" width="800" />
  <br>
  <i>Note: Replace this with a recording of your terminal session using tools like 'Terminalizer' or 'ScreenToGif'.</i>
</p>

---

## 📖 Project Overview

The **Smart Campus Information System** is a command-line utility designed to streamline academic administrative tasks and provide quantitative insights into student performance. This project serves as a practical implementation of modular programming, persistent file storage, and data analysis using the Python ecosystem.

### Key Functionalities:
- **Record Management:** CRUD operations for student profiles and course enrollments.
- **Academic Evaluation:** Automated grade calculation based on subject averages.
- **Data Analytics:** Statistical analysis of class performance using NumPy and Pandas.
- **Visualization:** Generation of performance distribution graphs via Matplotlib.
- **System Utilities:** Automated directory scanning and persistent text-based storage.

---

## 🏗 Engineering Architecture

This system follows a modular layered architecture, ensuring separation of concerns between user interaction, business logic, and data persistence.

```mermaid
graph TD
    subgraph UI_Layer [User Interface]
        Main[CLI Dashboard / main.py]
    end

    subgraph Service_Layer [Business Logic]
        Reg[Registration Module]
        Enroll[Course Module]
        Fin[Fee Management]
        FileSys[File System Handler]
    end

    subgraph Analytics_Layer [Data Engine]
        NP[NumPy Statistical Ops]
        PD[Pandas Data Manipulation]
        PLT[Matplotlib Visualization]
    end

    subgraph Data_Layer [Persistence]
        Store[(student_records.txt)]
    end

    Main --> Service_Layer
    Service_Layer --> Analytics_Layer
    Service_Layer --> Data_Layer
    Analytics_Layer --> UI_Layer

    style UI_Layer fill:#e1f5fe,stroke:#01579b
    style Service_Layer fill:#fff3e0,stroke:#e65100
    style Analytics_Layer fill:#f1f8e9,stroke:#33691e
    style Data_Layer fill:#ede7f6,stroke:#311b92
```

---

## 📊 Data Flow Diagram

The diagram below illustrates the lifecycle of student data from initial input to final analytical output.

```mermaid
flowchart LR
    In[[User Input]] --> Val{Validation}
    Val -->|Valid| Proc[Process Logic]
    Proc --> Persist[(Disk Storage)]
    Proc --> Stats[Compute Statistics]
    Stats --> DF[Pandas DataFrame]
    DF --> Plot[Generate Chart]
    Plot --> Disp((CLI / Plot Display))

    style In fill:#f5f5f5
    style Disp fill:#f5f5f5
    style Val fill:#fff9c4
```

---

## 🖼 Program Evidence

### Actual Application Interface

<p align="center">
  <img src="assets/dashboard.png" alt="Dashboard Screenshot" width="400" />
  <img src="assets/registration.png" alt="Registration Screenshot" width="400" />
</p>

### Sample Analytics Output

#### 🔹 NumPy Statistical Summary
```text
===== ANALYTICS =====
Highest Average : 94.5
Lowest Average  : 62.0
Class Average   : 78.25
```

#### 🔹 Pandas Data representation
| USN | Name | Average | Grade |
| :--- | :--- | :--- | :--- |
| 1DS22CS001 | Alice Johnson | 94.5 | A+ |
| 1DS22CS002 | Bob Smith | 72.0 | B |

#### 🔹 Matplotlib Visualization
<p align="center">
  <img src="assets/graph.png" alt="Performance Graph" width="600" />
</p>

---

## 🚀 Future Roadmap

- [x] Core CRUD Operations
- [x] File Persistence (Text-based)
- [x] Statistical Analytics Integration
- [x] Basic Data Visualization
- [ ] **Phase 2:** SQLite/PostgreSQL Database Integration
- [ ] **Phase 3:** Multi-user Authentication System
- [ ] **Phase 4:** Flask/FastAPI Web Dashboard
- [ ] **Phase 5:** Automated Report Export (PDF/CSV)

---

## 💻 Development Workflow

### Technical Implementation Details
1. **Data Structures:** Uses a list of dictionaries for in-memory data management during sessions.
2. **Sorting Logic:** Implements Python's Timsort (via `sorted()`) with lambda keys for ranking students by GPA/Average.
3. **Analytics Engine:** 
   - **NumPy:** Leverages vectorized operations to calculate class-wide metrics.
   - **Pandas:** Converts raw dictionaries into DataFrames for structured reporting.
4. **Persistence:** Implements a comma-separated text storage system with exception handling for file availability and permission errors.

### Educational Value
This project demonstrates proficiency in:
- Modular function design
- Error and Exception handling
- File I/O operations
- Data manipulation with external libraries
- Operating system interactions (OS module)

---

## 🛠 Setup & Requirements

### System Requirements
- **OS:** Windows 10/11, macOS, or Linux.
- **Python:** 3.8 or higher.
- **Memory:** 512MB RAM (Minimum).
- **Disk:** 10MB available space.

### Installation
```bash
# Clone the repository
git clone https://github.com/subhamsje/SMART-CAMPUS-INFORMATION-SYSTEM.git

# Initialize environment
cd SMART-CAMPUS-INFORMATION-SYSTEM
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

### Troubleshooting
- **ModuleNotFoundError:** Ensure the virtual environment is active and `pip install` was successful.
- **Matplotlib Backend:** If running on a headless server (WSL without X-server), Matplotlib may require a non-interactive backend (e.g., `Agg`).
- **File Permissions:** Ensure the application has write access to the directory for `student_records.txt`.

---

## 📂 Repository Structure

```text
.
├── main.py               # Application entry point & CLI logic
├── requirements.txt      # List of Python dependencies
├── .gitignore            # Git exclusion rules
├── assets/               # Screenshots, GIFs, and media
│   └── .gitkeep
└── README.md             # Project documentation
```

---

## 📈 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=subhamsje&show_icons=true&theme=transparent" alt="GitHub Stats" width="400" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=subhamsje&layout=compact&theme=transparent" alt="Top Languages" width="300" />
</p>

---

## 🤝 Contribution & License

Contributions are welcome! If you'd like to improve the system or add new features, please fork the repository and create a pull request.

**License:** Distributed under the MIT License. See `LICENSE` for more information.

<p align="center">
  <b>Developed by <a href="https://github.com/subhamsje">Subham</a></b><br>
  <a href="https://www.linkedin.com/in/subhamsje">LinkedIn</a> • <a href="https://github.com/subhamsje/SMART-CAMPUS-INFORMATION-SYSTEM">Repository</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/kyechan99/capsule-render/master/utils/wave.svg?color=36BCF7&height=50" width="100%" />
</p>
