import { ContactInformationViewModel } from "../ViewModels/ContactInformationViewModel.js";

class HomeView {
    constructor() {
        this.viewModel = new ContactInformationViewModel();
        this.viewModel.bind(this.updatePage.bind(this)); // Vincular correctamente la función

        this.startComponents();

        this.updatePage("Contacts"); // Corregido el nombre de la propiedad
    }

    startComponents() {
        this.$btnMode = document.querySelector(".mode");
        this.$contacts = document.querySelector("#contacts");
        this.$body = document.querySelector("body");

        this.$btnMode.addEventListener("click", () => {
            this.viewModel.toggleDarkMode()
            this.updatePage("isDarkMode")
        })
    }

    updatePage(propertyName) {
        if (propertyName === "Contacts") { // Corregido el nombre de la propiedad
            if (!this.$contacts) return;

            this.$contacts.innerHTML = ""; // Limpiar la lista

            this.viewModel.Contacts.forEach(contact => {
                this.$contacts.innerHTML += `
                    <li>
                        <span>${contact.Name}</span>
                        <span>${contact.LastName}</span>
                        <span>${contact.PhoneNumber}</span>
                        <span>${contact.Gender}</span>
                    </li>`;
            });
        }
        else if (propertyName === "isDarkMode") {

            this.$body.style.background = (this.viewModel.isDarkMode) ? "#000" : "#fff";
            this.$body.style.color = (this.viewModel.isDarkMode) ? "#fff" : "#000";
        }
    }
}

const view = new HomeView();
