from typing import Callable
from Models.Contact import Contacto
from baseConstactos import Datos
class ContactInformationViewModel:
    def __init__(self) -> None:
        # Inicializar listas vacías
        self.Constacts: list[Contacto] = []
        self.propertyChangedCallbacks: list[Callable[[str], None]] = []
        self._isDark = False
        self.LoadContact()

    def LoadContact(self):
        # Verificar que Datos sea iterable
        try:
            for contact_data in Datos():
                # Crear una instancia de Contacto por cada dato
                self.Constacts.append(Contacto(contact_data["name"], contact_data["lastName"], contact_data["phone"], contact_data["gender"]))
            self.OnPropertyChanged("Constacts")  # Notificar cambio
        except Exception as e:
            print(f"Error al cargar los contactos: {e}")

    @property
    def isDarkMode(self) -> bool:
        return self._isDark

    @isDarkMode.setter
    def isDarkMode(self, value: bool):
        if self._isDark != value:
            self._isDark = value
            self.OnPropertyChanged("isDarkMode")

    def toggleDarkMode(self):
        # Alternar el estado de modo oscuro
        self.isDarkMode = not self.isDarkMode

    def bind(self, func: Callable[[str], None]):
        # Registrar un callback
        self.propertyChangedCallbacks.append(func)

    def OnPropertyChanged(self, propertyName: str):
        # Notificar a todos los observadores
        for callback in self.propertyChangedCallbacks:
            try:
                callback(propertyName)
            except Exception as e:
                print(f"Error en el callback de {propertyName}: {e}")
