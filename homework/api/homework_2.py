import pint

a = 5

def printEquation(tag, value, digits):
    print(f"\\noindent\\[{tag} = {value:.{digits}Lx}\\]")

def printBoxedEquation(tag, value, digits):
    print("\\noindent\\[\\boxed{", f"{tag} = {value:.{digits}Lx}", "}\\]")
