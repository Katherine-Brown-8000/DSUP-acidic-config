# DSUP-acidic-config
Code and data use in research into DSUP changing structure

Methodology:
- [Calculate pI for DSUP](Calculate-isoelectric-point/)
- [Generating a plot for DSUP Net Charge vs. pH](https://github.com/Katherine-Brown-8000/DSUP-acidic-config/tree/main/Net-charge-plot)
- [DSUP electrostatic potential diagram](https://github.com/Katherine-Brown-8000/DSUP-acidic-config/tree/main/DSUP%20electrostatic%20potential%20diagram)

- Net charge vs pH
- MD simulations
- Disorder prediction
- Electrostatics
- Aggregation
- Structural comparison


## Calculating PI or eletrostatic potential

## Generating a plot for DSUP at Net Charge vs. pH

## DSUP electrostatic potential diagram
![Alt](https://github.com/Katherine-Brown-8000/DSUP-acidic-config/blob/main/DSUP_config_figure_1.png)
This figure was generated using ChimeraX from the DSUP files for pH 5.5, 7.4 and 11.5
- A) is DSUP at pH 5.5
- B) is DSUP at pH 7.4
- C) is DSUP at pH 11.5
- D) is DSUP at all three difference pHs overlapped

  ### Intructions

 - 1 Use AlphaFold3 to generate a fold prediction for the DSUP protein sequence. This produces a CIF structure file (fold_analysis_dsup_model_1.cif).

 - 2 Open the CIF file in ChimeraX and export it as a PDB file named dsup_model_0.pdb.

 - 3 Upload the PDB file to the PDB2PQR Server to generate .pqr and .in files at pH 5.5, 7.4, and 11.5.

 - 4 Run the .pqr and .in files through APBS to compute electrostatic potential maps (.dx files).

 - 5 Load both the .pqr and .dx files into ChimeraX to visualize and export electrostatic surfaces for each pH condition.


## Programs and websites used were:
 - [AlphaFold3](https://alphafoldserver.com/welcome)
 - [ChimeraX](https://www.cgl.ucsf.edu/chimerax/)
 - [PDB2QR online server](https://server.poissonboltzmann.org/pdb2pqr)
 - [APBS online server](https://server.poissonboltzmann.org/apbs)
