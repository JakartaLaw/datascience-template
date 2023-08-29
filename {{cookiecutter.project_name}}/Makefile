# VARIABLES

# change conda env to correct one
CONDA_ENV = "base"

# PIPELINES 
all: run-code compile-manuscript
	@echo "All tasks completed"

### Build
build:
	conda run -n $(CONDA_ENV) python src/example.py

### Analysis
analysis:
	@echo "Here your analysis should be"

### Running all code:
run-code: build analysis
	@echo "This should build your data set. Now just runs some example code"

### Compile document
compile-manuscript:
	@cd manuscript && pdflatex main.tex

### Removes annoying files
clean-latex-aux-files:
	@cd manuscript && rm main.aux main.bcf main.log main.idx main.run.xml main.toc main.bbl main.blg main.fdb_latexmk main.fls main.ilg main.ind main.synctex.gz

# scaffolds the project
scaffold:
	echo "Scaffolds project"
	mkdir -p output
	mkdir -p output/tables
	mkdir -p output/figures
	touch output/tables/.gitkeep
	touch output/figures/.gitkeep
	mkdir -p data
	mkdir -p data/raw
	mkdir -p data/processed
	mkdir -p data/analysis
	mkdir -p presentations
	touch presentations/.gitkeep

DATE := $(shell date +%Y-%m-%d)

new-presentation:
	mkdir -p presentations/$(DATE)
	touch presentations/$(DATE)/presentation.tex

# Example of how to run a notebook using Make -> you have to activate your conda env 
#run-analysis:
#	@jupyter nbconvert --to notebook --execute src/analysis.ipynb
