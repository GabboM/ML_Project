from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit import RDConfig
from rdkit.Chem.FeatMaps import FeatMaps
from rdkit.Chem import Descriptors
from rdkit.Chem import Crippen
from rdkit.Chem import rdchem

def atom_number(smile):
    '''
	Given the Smile, this function counts the number of atoms for each chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- number of atoms (int): number of atoms in the chemical
	'''
    return sum(1 for c in smile if c.isupper())


def alone_atom_number(smile):
    '''
	Given the Smile, this function counts the number of atoms, which are seperated from other atoms, in each chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- number of separeted atoms (int): number of separeted atoms in the chemical 
	''' 
    return smile.count('[') 


def count_doubleBond(smile):
    '''
	Given the smile, this function count the number of double bonds for each chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- number of double bonds (int): number of double bonds in the chemical 
	'''
    return smile.count('=') 


def count_tripleBond(smile):
    '''
	Given the smile, this function count the number of triple bonds for each chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- number of triple bonds (int): number of triple bonds in the chemical 
	'''
    return smile.count('#') 

    
def bonds_number(smile):
    '''
	Given the smile, this function count the number of bonds for each chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- bonds number (int): number of bonds in the chemical (NaN if not found)
	'''
    m = Chem.MolFromSmiles(smile)
    try:
        return rdchem.Mol.GetNumBonds(m)
    except:
        return 'NaN'

    
def ring_number(smile):
    '''
	Given the smile, this function count the number of ring in each Chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- ring_number (int): number of ring in the chemical (NaN if not found)
	'''
    m = Chem.MolFromSmiles(smile)
    try:
        f = rdchem.Mol.GetRingInfo(m)
        return f.NumRings()
    except:
        return 'NaN'


def Mol(smile):
    '''
	Given the smile, this function compute the Mol for each Chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- Mol (float): mol number of the chemical (NaN if not found)
	'''
    smile = str(smile)
    try:
        m = Chem.MolFromSmiles(smile)
        return Descriptors.MolWt(m)
    except:
        return 'NaN'  
	
    
def MorganDensity(smile):
    '''
	Given the Smile, this function compute the Morgan density for each Chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- Morgan Density (float): Morgan density of the chemical (NaN if not found)
	'''
    smile = str(smile)
    m = Chem.MolFromSmiles(smile)
    try:
        return Descriptors.FpDensityMorgan1(m)
    except:
        return 'NaN'

def LogP(smile):
    '''
	Given the Smile, this function compute the partition coefficient for each Chemical
    Inputs:
        - smile (string): original SMILES code
    Outputs:
		- LogP (float): partition coefficient of the chemical (NaN if not found)
	'''
    smile = str(smile)
    try:
        m = Chem.MolFromSmiles(smile)
        return Crippen.MolLogP(m)
    except:
        return 'NaN'    
    
def to_cas(num):
    ''' 
	Transform an integer CAS into a CAS Registry Number (format XXXXX-XX-X)
    Inputs:
        - num (int): CAS in integer format
    Outputs:
		- Cas_number (string): cas in format XXXXXX-XX-X
	'''
    Cas_number = str(num)
    Cas_number = Cas_number[:-3]+ '-' + Cas_number[-3:-1] +'-' + Cas_number[-1]
    return Cas_number