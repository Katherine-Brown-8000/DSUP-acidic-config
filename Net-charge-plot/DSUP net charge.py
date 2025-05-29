import numpy as np
import matplotlib.pyplot as plt
from Bio.SeqUtils import ProtParam


def calculate_charge(sequence, pH_values):
    # Define pKa values for ionizable groups
    pKa_values = {
        'C_term': 3.1, 'D': 3.9, 'E': 4.1, 'H': 6.0, 'C': 8.3, 'Y': 10.1,
        'N_term': 8.0, 'K': 10.5, 'R': 12.5
    }

    # Count occurrences of each ionizable residue
    aa_counts = {aa: sequence.count(aa) for aa in pKa_values.keys() if aa in sequence}

    net_charges = []
    for pH in pH_values:
        charge = 0
        # Compute charge contribution from N-terminus
        charge += (10 ** pKa_values['N_term']) / (10 ** pKa_values['N_term'] + 10 ** pH)
        # Compute charge contribution from C-terminus
        charge -= (10 ** pH) / (10 ** pKa_values['C_term'] + 10 ** pH)

        # Compute charge contribution from amino acids
        for aa, count in aa_counts.items():
            if aa in ['D', 'E', 'C', 'Y']:  # Negatively charged groups
                charge -= count * (10 ** pH) / (10 ** pKa_values[aa] + 10 ** pH)
            elif aa in ['H', 'K', 'R']:  # Positively charged groups
                charge += count * (10 ** pKa_values[aa]) / (10 ** pKa_values[aa] + 10 ** pH)

        net_charges.append(charge)

    return net_charges


# DSUP protein sequence (provided by user)
dsup_sequence = "MASTHQSSTEPSSTGKSEETKKDASQGSGQDSKNVTVTKGTGSSATSAAIVKTGGSQGKDSSTTAGSSSTQGQKFSTTPTDPKTFSSDQKEKSKSPAKEVPSGGDSKSQGDTKSQSDAKSSGQSQGQSKDSGKSSSDSSKSHSVIGAVKDVVAGAKDVAGKAVEDAPSIMHTAVDAVKNAATTVKDVASSAASTVAEKVVDAYHSVVGDKTDDKKEGEHSGDKKDDSKAGSGSGQGGDNKKSEGETSGQAESSSGNEGAAPAKGRGRGRPPAAAKGVAKGAAKGAAASKGAKSGAESSKGGEQSSGDIEMADASSKGGSDQRDSAATVGEGGASGSEGGAKKGRGRGAGKKADAGDTSAEPPRRSSRLTSSGTGAGSAPAAAKGGAKRAASSSSTPSNAKKQATGGAGKAAATKATAAKSAASKAPQNGAGAKKKGGKAGGRKRK"

# Define pH range
pH_values = np.linspace(0, 14, 100)

# Calculate net charge across pH values
net_charges = calculate_charge(dsup_sequence, pH_values)

# Plot charge vs. pH
plt.figure(figsize=(8, 5))
plt.plot(pH_values, net_charges, label='DSUP Net Charge', color='b')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(9.76, color='r', linestyle='--', label='Isoelectric Point (pI=9.76)')
plt.xlabel('pH')
plt.ylabel('Net Charge')
plt.title('DSUP Net Charge vs. pH')
plt.legend()
plt.grid()
plt.show()
