MAIN=main

all:
	latexmk -pdf $(MAIN).tex

clean:
	latexmk -C $(MAIN).tex
	rm -f *.bbl *.blg *.aux *.log *.out *.toc *.fls *.fdb_latexmk
