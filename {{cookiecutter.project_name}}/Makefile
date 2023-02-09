# VARIABLES
CONDA_ENV = "prob-ml"

# PIPELINES 

### Build

### Analysis

### Compile document

# COMMANDS
hello:
	echo "This is the makefile that you manage the project with"

scaffold:
	echo "Scaffolds project"
	mkdir -p figures
	touch figures/.gitkeep
	mkdir -p tables
	touch tables/.gitkeep
	mkdir -p data
	mkdir -p data/raw
	mkdir -p data/processed
	mkdir -p data/analysis

build:
	conda run -n $(CONDA_ENV) python project-utilities/hello.py

clean:
	echo "Cleans Project"