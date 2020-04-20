from collections import Counter
from .abc import MoleculeABC
from ..algorithms import Isomorphism
from ..periodictable.element import Element

class Molecule(Isomorphism, MoleculeABC):

    def get_atom(self, number: int) -> Element:
        if not isinstance(number, int):
            raise TypeError('Number must be int')
        elif number not in self._atoms:
            raise KeyError('Atom doesnt exist')
        else:
            return self._atoms[number]

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        if not isinstance(start_atom, int) or not isinstance(end_atom, int):
            raise TypeError('Atoms must be int')
        elif (start_atom or end_atom) not in self._atoms:
            raise KeyError('Atom doesnt exist')
        elif start_atom == end_atom:
            raise ValueError('Bond doesnt exist')
        else:
            return self._bonds[start_atom][end_atom]

    def delete_atom(self, number: int):
        if not isinstance(number, int):
            raise TypeError('Number must be int')
        elif number not in self._atoms:
            raise KeyError('Atom no longer exists')
        else:
            del self._atoms[number]

    def delete_bond(self, start_atom: int, end_atom: int):
        if not isinstance(start_atom, int) or not isinstance(end_atom, int):
            raise TypeError('Atoms must be int')
        elif (start_atom or end_atom) not in self._atoms:
            raise KeyError('Atom doesnt exist')
        elif start_atom == end_atom:
            raise ValueError('Bond doesnt exist')
        else:
            del self._bonds[start_atom][end_atom]

    def update_atom(self, element: Element, number: int):
        if not isinstance(element, Element):
            raise TypeError('Element must be Element-type')
        elif not isinstance(number, int):
            raise TypeError('Number must be int')
        elif number not in self._atoms:
            raise KeyError('Atom doesnt exist, you should add it to update')
        else:
            self._atoms[number] = element

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if not isinstance(start_atom, int) or not isinstance(end_atom, int) or not isinstance(bond_type, int):
            raise TypeError('Arguments must be int')
        elif (start_atom or end_atom) not in self._atoms:
            raise KeyError('Atom doesnt exist')
        elif bond_type not in (1, 2, 3, 4):  # single/double/triple/aromatic
            raise ValueError('This type of bonds cannot be updated')
        elif start_atom == end_atom:
            raise ValueError('Bond cannot be updated')
        elif bond_type not in (self._bonds[start_atom][end_atom] or self._bonds[end_atom][start_atom]):
            raise KeyError('Bond doesnt exist, you should add it to update')
        else:
            self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type

    def __enter__(self):
        self._backup_atoms = self._atoms.copy()
        self._backup_bonds = {k: v for k, v in self._bonds.items()}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._atoms = self._backup_atoms
            self._bonds = self._backup_bonds
            del self._backup_atoms
            del self._backup_bonds
        else:
            del self._backup_atoms
            del self._backup_bonds

    def __str__(self):
        c = Counter([self._atoms.values()])
        return 'Brutto-formula is {}{}'.format('{e for e in c.keys()}', '{n for n in c.values()}')


    def add_atom(self, element: Element, number: int):
        if not isinstance(element, Element):
            raise TypeError('Element must be Element-type')
        elif not isinstance(number, int):
            raise TypeError('Number must be int')
        elif number in self._atoms:
            raise IndexError('Number exists')
        else:
            self._atoms[number] = element

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        if not isinstance(start_atom, int) or not isinstance(end_atom, int) or not isinstance(bond_type, int):
            raise TypeError('Arguments must be int')
        elif (start_atom or end_atom) not in self._atoms:
            raise KeyError('Atom doesnt exist')
        elif bond_type not in (1, 2, 3, 4):  # single/double/triple/aromatic
            raise ValueError('This type of bonds cannot be added')
        elif start_atom == end_atom:
            raise ValueError('Bond cannot be added')
        else:
            self._bonds[start_atom][end_atom] = self._bonds[end_atom][start_atom] = bond_type



__all__ = ['Molecule']
