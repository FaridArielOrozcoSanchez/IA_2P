class Frame:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.actions = []
    
    def add_attribute(self, attribute_name, value):
        """Agrega un atributo al marco."""
        self.attributes[attribute_name] = value
    
    def add_action(self, action):
        """Agrega una acción al marco."""
        self.actions.append(action)

    def display(self):
        """Muestra el marco, sus atributos y acciones."""
        print(f"Marco: {self.name}")
        print("Atributos:")
        for attr, value in self.attributes.items():
            print(f"  {attr}: {value}")
        print("Acciones:")
        for action in self.actions:
            print(f"  - {action}")

# Uso de un marco
event_frame = Frame("Evento de Cumpleaños")
event_frame.add_attribute("Lugar", "Casa de Juan")
event_frame.add_attribute("Fecha", "15 de Noviembre")
event_frame.add_action("Invitar amigos")
event_frame.add_action("Comprar pastel")
event_frame.add_action("Preparar decoración")

event_frame.display()
