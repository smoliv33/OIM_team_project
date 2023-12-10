import os
import numpy as np
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import subprocess

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def perform_boolean_operation(mesh1, mesh2, operation):
    if operation == "union":
        return mesh1.union(mesh2, engine='blender')
    elif operation == "difference":
        return mesh1.difference(mesh2, engine='blender')
    elif operation == "intersection":
        return mesh1.intersection(mesh2, engine='blender')
    else:
        raise ValueError("Invalid boolean operation")
    
def parse_command(command):
    try:
        tokens = command.lower().split()
        if "cube" in tokens:
            side_length = float(tokens[tokens.index("side") + 1])
            return "cube", side_length
        elif "sphere" in tokens:
            radius = float(tokens[tokens.index("radius") + 1])
            return "sphere", radius
        elif "cylinder" in tokens:
            height = float(tokens[tokens.index("height") + 1])
            radius = float(tokens[tokens.index("radius") + 1])
            return "cylinder", (height, radius)
        elif "rectangular" in tokens and "prism" in tokens:
            length = float(tokens[tokens.index("length") + 1])
            width = float(tokens[tokens.index("width") + 1])
            height = float(tokens[tokens.index("height") + 1])
            return "rectangular_prism", (length, width, height)
        elif "triangular" in tokens and "pyramid" in tokens:
            side_length = float(tokens[tokens.index("side") + 1])
            return "triangular_pyramid", side_length
        elif "square" in tokens and "pyramid" in tokens:
            base_length = float(tokens[tokens.index("base") + 1])
            height = float(tokens[tokens.index("height") + 1])
            return "square_pyramid", (base_length, height)
        elif "triangular" in tokens and "prism" in tokens:
            length = float(tokens[tokens.index("length") + 1])
            base = float(tokens[tokens.index("base") + 1])
            height = float(tokens[tokens.index("height") + 1])
            return "triangular_prism", (length, base, height)
        elif "cone" in tokens:
            radius = float(tokens[tokens.index("radius") + 1])
            height = float(tokens[tokens.index("height") + 1])
            return "cone", (radius, height)
    except ValueError as e:
        print("Error: Numeric value for dimensions not found.", e)
    except IndexError as e:
        print("Error: Required keywords for dimensions not found.", e)
    return None, None

def generate_mesh(shape, dimensions):
    if shape == "cube":
        return create_cube_mesh(dimensions)
    elif shape == "sphere":
        return create_sphere_mesh(dimensions)
    elif shape == "cylinder":
        height, radius = dimensions
        return create_cylinder_mesh(height, radius)
    elif shape == "boolean":
        shape1_type, shape1_dims, shape2_type, shape2_dims, operation = dimensions
        mesh1 = generate_mesh(shape1_type, shape1_dims)
        mesh2 = generate_mesh(shape2_type, shape2_dims)
        return perform_boolean_operation(mesh1, mesh2, operation)
    elif shape == "rectangular_prism":
        length, width, height = dimensions
        return create_rectangular_prism_mesh(length, width, height)
    elif shape == "triangular_pyramid":
        side_length = dimensions
        return create_triangular_pyramid_mesh(side_length)
    elif shape == "square_pyramid":
        base_length, height = dimensions
        return create_square_pyramid_mesh(base_length, height)
    elif shape == "triangular_prism":
        length, base, height = dimensions
        return create_triangular_prism_mesh(length, base, height)
    elif shape == "cone":
        radius, height = dimensions
        return create_cone_mesh(radius, height)
    return None


def create_cube_mesh(side_length):
    """
    Create a mesh for a cube given the side length.

    Parameters:
    side_length (float): The length of each side of the cube.

    Returns:
    trimesh.base.Trimesh: A trimesh object representing a cube.
    """
    vertices = np.array([
        [-1, -1, -1],
        [+1, -1, -1],
        [+1, +1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
        [+1, -1, +1],
        [+1, +1, +1],
        [-1, +1, +1]
    ]) * side_length / 2
    faces = np.array([
        [0, 3, 1], [1, 3, 2], [0, 4, 7], [0, 7, 3], [4, 5, 6],
        [4, 6, 7], [5, 1, 2], [5, 2, 6], [2, 3, 6], [3, 7, 6],
        [0, 1, 5], [0, 5, 4]
    ])
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def create_sphere_mesh(radius):
    """
    Create a mesh for a sphere given the radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    trimesh.base.Trimesh: A trimesh object representing a sphere.
    """
    return trimesh.creation.icosphere(subdivisions=3, radius=radius)

def create_cylinder_mesh(height, radius):
    """
    Create a mesh for a cylinder given the height and radius.

    Parameters:
    height (float): The height of the cylinder.
    radius (float): The radius of the base of the cylinder.

    Returns:
    trimesh.base.Trimesh: A trimesh object representing a cylinder.
    """
    return trimesh.creation.cylinder(radius=radius, height=height)

def create_rectangular_prism_mesh(length, width, height):
    """
    Create a mesh for a rectangular prism given length, width, and height.
    Parameters:
    length (float): The length of the rectangular prism.
    width (float): The width of the rectangular prism.
    height (float): The height of the rectangular prism.
    Returns:
    trimesh.base.Trimesh: A trimesh object representing a rectangular prism.
    """
    # Vertices of a rectangular prism
    vertices = np.array([
        [0, 0, 0],
        [length, 0, 0],
        [length, width, 0],
        [0, width, 0],
        [0, 0, height],
        [length, 0, height],
        [length, width, height],
        [0, width, height]
    ])
    # Faces of the rectangular prism
    faces = np.array([
        [0, 1, 2], [0, 2, 3],
        [0, 3, 7], [0, 7, 4],
        [1, 5, 6], [1, 6, 2],
        [4, 5, 6], [4, 6, 7],
        [2, 6, 7], [2, 7, 3],
        [0, 4, 5], [0, 5, 1]
    ])
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def create_triangular_pyramid_mesh(side_length):
    # Height of the pyramid
    height = np.sqrt(2 / 3) * side_length
    vertices = np.array([
        [0, 0, height],
        [0, side_length / 2, 0],
        [side_length * np.sqrt(3) / 2, -side_length / 2, 0],
        [-side_length * np.sqrt(3) / 2, -side_length / 2, 0]
    ])
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 1],
        [1, 3, 2]
    ])
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def create_square_pyramid_mesh(base_length, height):
    half_base = base_length / 2
    vertices = np.array([
        [0, 0, height],
        [-half_base, -half_base, 0],
        [half_base, -half_base, 0],
        [half_base, half_base, 0],
        [-half_base, half_base, 0]
    ])
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 4],
        [0, 4, 1],
        [1, 4, 3],
        [3, 2, 1]
    ])
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def create_triangular_prism_mesh(length, base, height):
    half_base = base / 2
    vertices = np.array([
        [0, -half_base, 0],
        [0, half_base, 0],
        [height, 0, 0],
        [0, -half_base, length],
        [0, half_base, length],
        [height, 0, length]
    ])
    faces = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [0, 3, 4],
        [4, 1, 0],
        [1, 4, 5],
        [5, 2, 1],
        [2, 5, 3],
        [3, 0, 2]
    ])
    return trimesh.Trimesh(vertices=vertices, faces=faces)

def create_cone_mesh(radius, height):
    return trimesh.creation.cone(radius=radius, height=height, sections=32)

def visualize_mesh(mesh):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for faces in mesh.faces:
        vertices = mesh.vertices[faces]
        mesh_collection = Poly3DCollection([vertices], alpha=0.5, edgecolor='k', linewidths=1.0, facecolor='cyan')
        ax.add_collection3d(mesh_collection)

    scale = np.concatenate([mesh.vertices[:, 0:1], mesh.vertices[:, 1:2], mesh.vertices[:, 2:3]]).flatten()
    ax.auto_scale_xyz(scale, scale, scale)

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()

def open_in_prusa_slicer(filename):
    prusa_slicer_executable = "C:\\Program Files\\Prusa3D\\PrusaSlicer\\prusa-slicer.exe"
    subprocess.run([prusa_slicer_executable, filename])

def main():
    print("SeeCube Generator")
    print("Type 'help' for instructions or 'exit' to quit.")
    output_directory = "STL_Files"
    create_directory(output_directory)

    while True:
        user_input = input("Enter your command: ")
        if user_input.lower() == 'help':
            print("\nHelp: Enter a command to create a 3D shape and export it as an STL file.")
            print("Example commands:")
            print("  create cube with side 40")
            print("  create sphere with radius 20")
            print("  create cylinder with height 40 radius 20")
            print("  create rectangular prism with length 40 width 30 height 20")
            print("  create triangular pyramid with side 30")
            print("  create square pyramid with base 40 height 30")
            print("  create triangular prism with length 40 base 30 height 20")
            print("  create cone with radius 20 height 40\n")
            continue
        elif user_input.lower() == 'exit':
            break

        shape, dimensions = parse_command(user_input)
        if shape and dimensions:
            try:
                mesh = generate_mesh(shape, dimensions)
                if mesh:
                    dim_str = "_".join(map(str, dimensions if isinstance(dimensions, tuple) else [dimensions]))
                    filename = os.path.join(output_directory, f'{shape}_{dim_str}.stl')
                    mesh.export(filename)
                    print(f"{shape.capitalize()} with dimensions {dim_str} exported as {filename}")

                    visualize_mesh(mesh)

                    # Ask user to open in PrusaSlicer
                    user_choice = input("Open this model in PrusaSlicer? (yes/no): ")
                    if user_choice.lower() == 'yes':
                        open_in_prusa_slicer(filename)

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()