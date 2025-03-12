import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import os

# Cylinder Geometry Identifier
myShellName = "IW1_dummy"

# Length, Radius, and Thickness of the cylinder
#myLength = 13.15169183      # Z = 50
#myLength = 18.59930096     # Z = 100
#myLength = 26.30338367     # Z = 200
#myLength = 37.19860192     # Z = 400
#myLength = 49.20912489     # Z = 700
#myLength = 58.81615391    # Z = 1000
#myLength = 72.03478286    # Z = 1500
#myLength = 83.17860255    # Z = 2000
#myLength = 101.8725669     # Z = 3000
#myLength = 131.5169183     # Z = 5000
#myLength = 185.993     # Z = 10000
myRadius = 33.0
myThickness = 0.1
myLength = 100.0

# Number of Nodes in axial and circumferential direction
na = 111
nc = 230

# Fourier approach (1 - phase shift, 2 - cos , 3 - sin)
case = 2

# Define desired maximum w values
scale_v = [0.5]

# Shells to process
Shells = ["IW1_16","IW1_17","IW1_18","IW1_19","IW1_20","IW1_21","IW1_22","IW1_23",
          "IW1_24","IW1_25","IW1_26","IW1_27","IW1_28","IW1_29","IW1_30",
          "IW1_31","IW1_32","IW1_33","IW1_34","IW1_35","IW1_36","IW1_37",
          "IW1_38","IW1_39","IW1_40","IW1_41","IW1_42","IW1_43","IW1_44",
          "IW1_45","IW1_46","IW1_47"]

#Shells = ["ST_1","ST_2","ST_3","ST_4","ST_5","ST_6","B_1", "B_2","B_3", "B_4"]

#Shells = ["N_6", "N_9", "N_11"]

#Shells = ["Z07","Z08","Z10","Z11","Z12","Z15","Z17","Z18","Z20","Z21","Z22","Z23","Z24","Z25","Z26"]

#Shells = ["Z1_1","Z1_2","Z1_3","Z1_4","Z1_5","Z1_6","Z2_1","Z2_2","Z2_3","Z2_4","Z2_5","Z2_6"]

# Load Fourier Coefficients
myFC_A_v = []
myFC_B_v = []

# for i in Shells:
#     A = np.loadtxt(f"{i}_measured.FC_A")
#     B = np.loadtxt(f"{i}_measured.FC_B")
#     myFC_A_v.append(A)
#     myFC_B_v.append(B)

for i in Shells:
    A = np.loadtxt(f"{i}-FC_A.txt")
    B = np.loadtxt(f"{i}-FC_B.txt")
    myFC_A_v.append(A)
    myFC_B_v.append(B)


n1, n2 = A.shape
n_imp = len(myFC_A_v)

# Create a new directory to store the results
output_dir = "Simulation_Results"
os.makedirs(output_dir, exist_ok=True)

# Vectorized computation of displacement field
def compute_w_vectorized(phim_mean, eps_mean, na, nc, myLength, myRadius, myThickness, case):
    x = np.linspace(0, myLength, na)
    y = np.linspace(0, 2.0 * np.pi * myRadius, nc)
    X, Y = np.meshgrid(x, y, indexing='ij')  # Use 'ij' indexing for correct dimensions
    
    w = np.zeros((na, nc))
    if case == 1:
        for k in range(n1):
            for l in range(n2):
                w += A[k, l] * np.cos(k * np.pi * X / myLength) * np.cos(l * Y / myRadius - B[k, l])
    elif case == 2:
        for k in range(n1):
            for l in range(n2):
                w += np.cos(k * np.pi * X / myLength) * (phim_mean[k, l] * np.cos(l * Y / myRadius) + eps_mean[k, l] * np.sin(l * Y / myRadius))
    elif case == 3:
        for k in range(n1):
            for l in range(n2):
                w += np.sin(k * np.pi * X / myLength) * (phim_mean[k, l] * np.cos(l * Y / myRadius) + eps_mean[k, l] * np.sin(l * Y / myRadius))
    
    return w * myThickness

for idx, shell_name in enumerate(Shells):
    phim_mean = myFC_A_v[idx]
    eps_mean = myFC_B_v[idx]

    for desired_max_w in scale_v:
        w = compute_w_vectorized(phim_mean, eps_mean, na, nc, myLength, myRadius, myThickness, case)
        
        # Scale the displacement field
        actual_max_w = np.max(np.abs(w))
        scale_factor = desired_max_w / actual_max_w if actual_max_w > 0 else 1.0
        w *= scale_factor

        # Create cylindrical coordinates
        z_cylinder = np.linspace(0, myLength, na)
        phi_cylinder = np.linspace(0, 2.0 * np.pi * myRadius, nc)
        Z, Phi = np.meshgrid(z_cylinder, phi_cylinder, indexing='ij')  # Use 'ij' indexing for correct dimensions
        X_cylinder = myRadius * np.cos(Phi / myRadius)
        Y_cylinder = myRadius * np.sin(Phi / myRadius)

        # Ensure w has the correct shape for facecolors
        w_colors = w  # w is already in the correct shape (na, nc)

        # Plot the displacement field on the cylinder
        fig = plt.figure(figsize=(16, 6))
        ax = fig.add_subplot(121, projection='3d')
        contour_cylinder = ax.plot_surface(X_cylinder, Y_cylinder, Z, facecolors=cm.jet(w_colors / np.max(np.abs(w_colors))), rstride=1, cstride=1)
        ax.set_title(f"Cylinder Displacement Field (w) for Scale {desired_max_w:.3f}")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Plot the 2D Contourplot of w
        ax2 = fig.add_subplot(122)
        contour = ax2.contourf(np.linspace(0, 2.0 * np.pi * myRadius, nc), np.linspace(0, myLength, na), w, levels=50, cmap="jet")
        plt.colorbar(contour, ax=ax2, label="Radial Displacement [mm]")
        ax2.set_title(f"2D Contourplot of w for Scale {desired_max_w:.3f}")
        ax2.set_xlabel('Circumferential Position [mm]')
        ax2.set_ylabel('Axial Position [mm]')
        ax2.set_aspect('auto')

        # Save the combined plot
        combined_plot_filename = f"{output_dir}/{shell_name}_combined_plot_{desired_max_w:.3f}.png"
        plt.savefig(combined_plot_filename, dpi=300)
        print(f"Generated: {combined_plot_filename}")

        # Show the plot in Spyder
        plt.show()

        # Calculate coordinates xyz
        xyz = np.zeros((na * nc, 3))
        
        # Create phi_cylinder and z_cylinder
        phi_cylinder = np.linspace(0, 2.0 * np.pi * myRadius, nc)
        z_cylinder = np.linspace(0, myLength, na)
        
        # Repeat phi_cylinder and z_cylinder to match the length of w.flatten()
        phi_cylinder_repeated = np.tile(phi_cylinder, na)  # Repeat phi_cylinder for each axial position
        z_cylinder_repeated = np.repeat(z_cylinder, nc)  # Repeat z_cylinder for each circumferential position
        
        # Ensure (myRadius - w.flatten()) is always positive
        w_flattened = w.flatten()
        radius_minus_w = myRadius - w_flattened
        radius_minus_w[radius_minus_w < 0] = 0  # Set negative values to zero
        
        # Calculate coordinates xyz
        xyz = np.zeros((na * nc, 3))  # Reset xyz array
        for i in range(0, na, 1):
            for j in range(0, nc, 1):
                y = 2.0 * np.pi * myRadius * (j) / (nc)
                x = myLength * (i) / (na)
                xyz[(i) * nc + j][0] = (myRadius - w[i][j]) * np.cos(y / myRadius)
                xyz[(i) * nc + j][1] = (myRadius - w[i][j]) * np.sin(y / myRadius)
                xyz[(i) * nc + j][2] = x * 1.016666671
        
        # Write scaled nodes to file
        scaledFileName = f"{output_dir}/{shell_name}_scaled_nodes_{desired_max_w:.3f}.txt"
        np.savetxt(scaledFileName, np.column_stack((np.arange(1, len(xyz) + 1), xyz)), fmt='%i, %10.5f, %10.5f, %10.5f')
        print(f"Generated: {scaledFileName}")
        
        # Generate elements file
        rows = nc * na
        rows2 = rows - nc
        
        data = []
        for i in range(1, rows2 + 1):
            if i == rows2:
                # Handle the last row of elements
                row = [i, i, nc * na - 2 * nc + 1, nc * na - nc + 1, i + nc]
            elif i % nc == 0:
                # Handle the last element in each circumferential row
                row = [i, i, i - nc + 1, i + 1, i + nc]
            else:
                # Handle all other elements
                row = [i, i, i + 1, i + nc + 1, i + nc]
            data.append(row)
        
        elementFileName = f"{output_dir}/{shell_name}_scaled_elements_{desired_max_w:.3f}.txt"
        np.savetxt(elementFileName, data, fmt='%6i , %6i , %6i , %6i , %6i')
        print(f"Generated: {elementFileName}")