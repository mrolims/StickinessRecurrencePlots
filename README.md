# StickinessRecurrencePlots

Code repository accompanying the publication "*Stickiness and recurrence plots: an entropy based approach*".

This project contains the code to generate and plot the data from all figures. It uses the [pyunicorn package](http://www.pik-potsdam.de/~donges/pyunicorn/) to create the recurrence plots and obtain the recurrence quantificators.

## Requirements

The required packages are listed in ``` requirements.txt ```. To install please execute ``` pip install -r requirements.txt ```.

To solve the "No module named 'setup'" when importing ``` pyunicorn ```, please check [https://github.com/pik-copan/pyunicorn/issues/129](https://github.com/pik-copan/pyunicorn/issues/129).

## Figure 1

To obtain the data used in Figure 1, execute ``` python fig1.py ```, and then ``` python plot_fig1.py ``` to plot the data.

## Figure 2

To obtain the data used in Figure 2, execute ``` python fig2.py ```, and then ``` python plot_fig2.py ``` to plot the data.

## Figure 3

To obtain the data used in Figure 3, execute ``` python fig3.py ```, and then ``` python plot_fig3.py ``` to plot the data.

## Figure 4

To obtain the data used in Figures 4(a) and 4(b), execute ``` python fig4ab.py a ``` and ``` python fig4ab.py b ```, and to obtain the data used in Figure 4(c), execute ``` python fig4ab.py c ```. To obtain the data used in Figures 4(d) and 4(e), execute ``` python fig4de.py d ``` and ``` python fig4de.py e ```, and to obtain the data used in Figure 4(f), execute ``` python fig4f.py ```. Then execute ``` python plot_fig4abc.py ``` and ``` python plot_fig4def.py ``` to plot the data.

## Figure 5

To obtain the data used in Figure 5, execute ``` python fig5a.py 1e10 ```, ``` python fig5a.py 1e10 ``` and ``` python fig5bc_6a.py 1e9 ```. Then execute ``` python plot_fig5.py ``` to plot the data.

## Figure 6

To obtain the data used in Figure 6, execute ``` python fig5a.py 1e11 ```, ``` python fig5a.py 1e10 ``` and ``` python fig6b.py ```. Then execute ``` python plot_fig6.py ``` to plot the data.