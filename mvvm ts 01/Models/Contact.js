export class Contact {
    constructor(name, lastName, phoneNumber, gender) {
        this._Name = name;
        this._Lastname = lastName;
        this._PhoneNumber = phoneNumber;
        this._Gender = gender;
    }

    get Name() {
        return this._Name;
    }

    set Name(name) {
        this._Name = name;
    }

    get LastName() {
        return this._Lastname;
    }

    set LastName(lastName) {
        this._Lastname = lastName;
    }

    get PhoneNumber() {
        return this._PhoneNumber;
    }

    set PhoneNumber(phoneNumber) {
        this._PhoneNumber = phoneNumber;
    }

    get Gender() {
        return this._Gender;
    }

    set Gender(gender) {
        this._Gender = gender;
    }
}
