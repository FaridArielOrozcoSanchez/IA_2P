import numpy as np
import pandas as pd

class DecisionTreeID3:
    def __init__(self, data, target_column):
        self.data = data
        self.target_column = target_column
        self.tree = self.build_tree(data)

    def entropy(self, target):
        """Calcula la entropía de la variable objetivo."""
        value_counts = target.value_counts()
        probabilities = value_counts / len(target)
        return -np.sum(probabilities * np.log2(probabilities))

    def gain(self, data, split_column):
        """Calcula la ganancia de información al dividir por un atributo."""
        original_entropy = self.entropy(data[self.target_column])
        values = data[split_column].unique()
        weighted_entropy = 0

        for value in values:
            subset = data[data[split_column] == value]
            weighted_entropy += (len(subset) / len(data)) * self.entropy(subset[self.target_column])

        return original_entropy - weighted_entropy

    def best_split(self, data):
        """Encuentra el mejor atributo para dividir el conjunto de datos."""
        splits = data.columns.drop(self.target_column)
        gains = {split: self.gain(data, split) for split in splits}
        return max(gains, key=gains.get)

    def build_tree(self, data):
        """Construye el árbol de decisión recursivamente."""
        target = data[self.target_column]
        
        if len(target.unique()) == 1:
            return target.unique()[0]  # Retorna la clase única

        if len(data.columns) == 1:  # Si no quedan más atributos
            return target.mode()[0]  # Retorna la clase más frecuente

        best_split_column = self.best_split(data)
        tree = {best_split_column: {}}

        for value in data[best_split_column].unique():
            subset = data[data[best_split_column] == value]
            subtree = self.build_tree(subset.drop(columns=[best_split_column]))
            tree[best_split_column][value] = subtree

        return tree

    def print_tree(self, tree=None, depth=0):
        """Imprime el árbol de decisión."""
        if tree is None:
            tree = self.tree
        
        for key, value in tree.items():
            print("  " * depth + str(key))
            if isinstance(value, dict):
                self.print_tree(value, depth + 1)
            else:
                print("  " * (depth + 1) + "-> " + str(value))

# Ejemplo de uso
data = pd.DataFrame({
    'color': ['rojo', 'rojo', 'verde', 'verde', 'rojo'],
    'forma': ['circulo', 'cuadrado', 'circulo', 'cuadrado', 'cuadrado'],
    'clase': ['fruta', 'fruta', 'vegetal', 'vegetal', 'fruta']
})

# Crear el árbol de decisión
tree = DecisionTreeID3(data, target_column='clase')

tree.print_tree()
