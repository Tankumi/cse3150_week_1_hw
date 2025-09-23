import os, subprocess

def run_program():
    exe = "math_program.exe" if os.name == "nt" else "./math_program"
    result = subprocess.run([exe], capture_output=True, text=True, check=True)
    return result.stdout.strip().splitlines()

def test_add():
    output = run_program()
    assert output[0] == "a + b = 7"

def test_multiply():
    output = run_program()
    assert output[1] == "a * b = 12"

def test_square():
    output = run_program()
    assert output[2] == "square(a) = 9"