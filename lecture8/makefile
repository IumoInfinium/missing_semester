paper.pdf: paper.tex plot-data.png
	pdflatex $<

plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@

.PHONY: clean

clean:
	rm -f paper.pdf paper.aux paper.log plot-data.png
