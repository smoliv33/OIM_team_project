# app.py

from flask import Flask, render_template, request
import os
import subprocess

from seecube import parse_command, generate_mesh, visualize_mesh, open_in_prusa_slicer, create_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['userInput']
    output_directory = "STL_Files"
    create_directory(output_directory)

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

                # Open this model in PrusaSlicer
                open_in_prusa_slicer(filename)

                return render_template('result.html', result=f"{shape.capitalize()} with dimensions {dim_str} exported as {filename}")

        except Exception as e:
            error_message = f"An unexpected error occurred: {e}"
            print(error_message)
            return render_template('result.html', result=error_message)

    return render_template('result.html', result="Invalid command or an error occurred.")

if __name__ == '__main__':
    app.run(debug=True)
