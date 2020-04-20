from ChemistryTool.ChemistryTool.periodictable.element import Element
from .abc import MoleculeABC
from ..algorithms import Isomorphism


class Molecule(Isomorphism, MoleculeABC):
    def get_atom(self, number: int) -> Element:
        pass

    def get_bond(self, start_atom: int, end_atom: int) -> int:
        pass

    def add_atom(self, element: Element, number: int):
        pass

    def add_bond(self, start_atom: int, end_atom: int, bond_type: int):
        pass

    def delete_atom(self, number: int):
        pass

    def delete_bond(self, start_atom: int, end_atom: int):
        pass

    def update_atom(self, element: Element, number: int):
        pass

    def update_bond(self, start_atom: int, end_atom: int, bond_type: int):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __str__(self):
        pass

    ...


__all__ = ['Molecule']
