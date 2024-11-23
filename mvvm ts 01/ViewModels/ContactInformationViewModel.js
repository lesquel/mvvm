import { Contact } from "../Models/Contact.js"
export class ContactInformationViewModel {
    constructor() {
        this._isDarkMode = false;
        this.Contacts = [];
        this.propertyChangedCallbacks = [];

        // Cargar contactos desde JSON
        this.loadContacts();
    }
    async loadContacts() {
        try {
            const res = await fetch("/baseContactos.json");
            const data = await res.json();
            data.forEach(contact => {
                this.Contacts.push(new Contact(contact.Name, contact.LastName, contact.PhoneNumber, contact.Gender));
            });
            this.OnPropertyChanged("Contacts");
        } catch (err) {
            console.error(err);
        }
    }
    

    get isDarkMode() {
        return this._isDarkMode;
    }

    set isDarkMode(value) {
        this._isDarkMode = value;
        this.OnPropertyChanged("isDarkMode"); // Notificar cambio
    }

    // Alternar modo oscuro
    toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
    }

    // Registrar observadores
    bind(callback) {
        this.propertyChangedCallbacks.push(callback);
    }

    // Notificar cambios
    OnPropertyChanged(propertyName) {
        this.propertyChangedCallbacks.forEach(callback => callback(propertyName, this));
    }
}
